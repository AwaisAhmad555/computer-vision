import cv2 as opencv
import numpy as np
import pandas as pd
import os
import pickle


def feature_matcher(query_image,training_feature,matching_algorithm):

    # calculating SIFT features for each query image

    test_sample_keypoints, query_image_descriptors = sift.detectAndCompute(query_image, None)


    matches = matching_algorithm.knnMatch(query_image_descriptors, training_feature, k=2)

    score = []

    for m, n in matches:

        if m.distance < 0.4 * n.distance:
            score.append([m])

            pass

        pass

    return len(score)
    pass


def text_generator(text_dataFrame : pd.DataFrame,maximum_match_score,training_samples_array):

    maximum_match_score_index = training_samples_array[maximum_match_score, 1]

    text = np.array(text_dataFrame)[maximum_match_score_index, 0]

    return text
    pass


def load_query_images(path : str):

    query_images_list = []

    images_names = os.listdir(path=path)

    for idx,image_name in enumerate(images_names):

        image_address = os.path.join(path,image_name)

        image = opencv.imread(filename=image_address)

        query_images_list.append(image)

        #opencv.imshow("image : " + str (idx) ,image)


        pass


    return query_images_list
    pass


training_samples_list = pickle.load(open("dataset\\training_samples_dataset.pkl", "rb"))


training_samples_array = np.array(training_samples_list)


matching_score = []



"""test_sample = opencv.imread("temporary\\segment_images\\18.png")
"""




sift = opencv.xfeatures2d.SIFT_create()


#################test image Scale invarient features





query_image_path = "temporary\\segment_images"

images_list = load_query_images(path=query_image_path)



SIFT_features_list = pickle.load(open("dataset\\training_samples_SIFT_Features.pkl", "rb"))


text_dataframe = pd.read_csv("dataset\\dataset.csv")

query_image_scores_list = []

index_params = dict(algorithm=0, trees=5)
search_params = dict()
flann = opencv.FlannBasedMatcher(index_params, search_params)


for j,single_query_image in enumerate(images_list):

    #test_sample = opencv.imread("temporary\\segment_images\\18.png")

    #opencv.imshow("test image - " + str(j), single_query_image)


    for single_sample_feature in SIFT_features_list:

        image_matching_score = feature_matcher(query_image=single_query_image, training_feature=single_sample_feature,
                                               matching_algorithm=flann)

        matching_score.append(image_matching_score)

        pass



    matching_score_array = np.array(matching_score)

    maximum_match_score = np.argmax(matching_score_array)

    print(maximum_match_score)

    query_image_scores_list.append(maximum_match_score)

    matching_score = []

    """if j == 1:

        break

        pass"""


    pass






#opencv.imshow("matched_image",training_samples_array[maximum_match_score,0])

for idx,each_maximum_score in enumerate(query_image_scores_list):


    #opencv.imshow("matched_image" + str(each_maximum_score), training_samples_array[each_maximum_score, 0])


    text_string = text_generator(text_dataFrame=text_dataframe, maximum_match_score=each_maximum_score,
                                 training_samples_array=training_samples_array)

    print("\nIMAGE TEXT IS : \n")

    print(text_string)



    pass



opencv.waitKey(0)
opencv.destroyAllWindows()