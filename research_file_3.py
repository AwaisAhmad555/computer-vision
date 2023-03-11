import cv2 as opencv
import numpy as np
import pandas as pd
import os
import pickle


def load_training_samples(root_folder_name : str):

    full_training_samples_list = []

    folders_list = os.listdir(root_folder_name)

    labels = []

    training_samples_list = []

    label_variable = int

    for sub_directory_name in folders_list:

        sub_directory_path = os.path.join(root_folder_name, sub_directory_name)

        if os.path.isfile(sub_directory_path):

            pass

        else:

            sample_folders = os.listdir(sub_directory_path)

            # print(sample_folders)

            for folder_name in sample_folders:

                label_variable = int(folder_name)

                folder_name_path = os.path.join(sub_directory_path, folder_name)

                images_names_list = os.listdir(folder_name_path)

                # print("\n")

                for image_name in images_names_list:
                    image_address = os.path.join(folder_name_path, image_name)

                    # print(image_address)

                    image = opencv.imread(image_address)

                    image = opencv.resize(image, (200, 200), None)

                    parameter, image = opencv.threshold(image, 200, 255, opencv.THRESH_BINARY)

                    training_samples_list.append([image, label_variable])

                    pass

                pass

            pass

        pass

    full_training_samples_list = training_samples_list

    return full_training_samples_list
    pass


def load_features(training_samples_array):


    SIFT_features_list = []

    for idx in range(training_samples_array.shape[0]):

        image_1 = training_samples_array[idx, 0]


        sift = opencv.xfeatures2d.SIFT_create()

        # parameter, image_1 = opencv.threshold(image_1,150,255,opencv.THRESH_BINARY,None)

        keypoints, training_sample_SIFT_features = sift.detectAndCompute(image_1, None)

        ########## Appending all sample SIFT features in features list

        SIFT_features_list.append(training_sample_SIFT_features)

        ####################################################################
        keypoints, training_sample_descriptors = sift.detectAndCompute(image_1, None)

        # print(len(score))

        # result = opencv.drawMatchesKnn(img1=test_sample,keypoints1=test_sample_keypoints,img2=image_1,keypoints2=keypoints,matches1to2=score,outImg=None)

        # opencv.imshow("result",result)

        pass

     # opencv.imshow(" " + str (training_samples_array[112,1]) ,training_samples_array[112,0])


    return SIFT_features_list


def generate_text(query_image,training_labels,training_features):




    return
    pass



######################################################################################


root_folder_name = "dataset"


#training_samples_list = load_training_samples(root_folder_name=root_folder_name)

#pickle.dump(training_samples_list, open("dataset\\training_samples_dataset.pkl", "wb"))

training_samples_list = pickle.load(open("dataset\\training_samples_dataset.pkl", "rb"))

print(np.array(training_samples_list).shape)


#opencv.imshow(" " + str (np.array(training_samples_list)[29][1]),np.array(training_samples_list)[29][0])

training_samples_array = np.array(training_samples_list)


#pickle.dump(training_samples_array, open("sample_images\\training_samples_array.pkl", "wb"))


matching_score = []



test_sample = opencv.imread("temporary\\segment_images\\33.png")

test_sample = opencv.resize(test_sample, (200, 200), None)

parameter, test_sample = opencv.threshold(test_sample, 200, 255, opencv.THRESH_BINARY)



#test_sample = opencv.resize(test_sample, (200, 200), None)

opencv.imshow("test",test_sample)




sift = opencv.xfeatures2d.SIFT_create()


#################test image Scale invarient features


test_sample_keypoints, test_sample_descriptors = sift.detectAndCompute(test_sample, None)




#SIFT_features_list = load_features(training_samples_array=training_samples_array)

#pickle.dump(SIFT_features_list, open("dataset\\training_samples_SIFT_Features.pkl", "wb"))

SIFT_features_list = pickle.load(open("dataset\\training_samples_SIFT_Features.pkl", "rb"))




index_params = dict(algorithm=0, trees=5)
search_params = dict()
flann = opencv.FlannBasedMatcher(index_params, search_params)


for single_sample_feature in SIFT_features_list:

    matches = flann.knnMatch(test_sample_descriptors, single_sample_feature, k=2)

    score = []

    for m, n in matches:

        if m.distance < 0.44 * n.distance:
            score.append([m])

            pass

        pass

    matching_score.append(len(score))


    pass



print()
print(training_samples_array.shape[0])

matching_score_array = np.array(matching_score)

print()

print(matching_score_array.shape)

print()

maximum_match_score = np.argmax(matching_score_array)

print()

print(matching_score_array)

print()

maximum_match_score_index = training_samples_array[maximum_match_score,1]

print(maximum_match_score_index)

opencv.imshow("matched_image",training_samples_array[maximum_match_score,0])


text_dataframe = pd.read_csv("dataset\\dataset.csv")
vals=text_dataframe.values

v=vals[maximum_match_score_index]

print(v)
abc=np.where(vals==maximum_match_score_index)


#result=text_dataframe.where(text_dataframe==maximum_match_score)


maximum_match_score

print(np.array(text_dataframe)[maximum_match_score_index,1])

for j in range(len(np.array(text_dataframe)[:,1])):

    if int (np.array(text_dataframe)[j,1]) == maximum_match_score_index:

        image_text = np.array(text_dataframe)[j,0]

        pass


    pass

print(image_text)


opencv.waitKey(0)
opencv.destroyAllWindows()



