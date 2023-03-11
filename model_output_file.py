import cv2 as openCV
import pandas as pd
import numpy as np
import pickle
from skimage.feature import hog
import random
from sklearn.neighbors import KNeighborsClassifier

import os



#full_path = r"C:\Users\shahzad com\PycharmProjects\urdu_ocr\data_samples"

#directory = os.listdir(full_path)


#dataset_list = []

#X = []
#Y = []

"""
for folders in directory:

    folder_name = str (folders)

    new_path = os.path.join(full_path,folders)

    for idx, imgs in enumerate(os.listdir(new_path)):
        image = openCV.imread(os.path.join(new_path, imgs))

        image = openCV.cvtColor(image, openCV.COLOR_RGB2GRAY, None, None)

        fd, hog_image = hog(image, orientations=4, block_norm='L2', pixels_per_cell=(8, 8),
                            cells_per_block=(2, 2), visualize=True, multichannel=False)

        #openCV.imshow(""+folder_name+" - "+str(idx),np.hstack((image,hog_image)))

        label = int(os.path.splitext(imgs)[0])

        #print(label)

        X.append(fd.tolist())
        Y.append(label)

        dataset_list.append([label,fd.tolist()])


        pass

    pass



random.shuffle(dataset_list)


array_new = np.array(dataset_list)
"""



#result = loaded_model.score(X=array_new[:,1].tolist(),y=array_new[:,0].tolist())
#print(result)


#sample_array = array_new[:,1].tolist()

#images_labels_list = array_new[:,0].tolist()

print()

#print("Labels ",images_labels_list[1:12])


full_path = r"C:\Users\shahzad com\PycharmProjects\urdu_ocr\temporary\segment_images"

test_images = []
test_images_features_list = []
test_images_labels = []


for indx,images in enumerate(os.listdir(full_path)):

    image_name = os.path.join(full_path,images)

    test_image = openCV.imread(image_name)


    test_image = openCV.cvtColor(test_image, openCV.COLOR_RGB2GRAY, None, None)

    threshold_value , test_image = openCV.threshold(test_image,100,255,openCV.THRESH_BINARY)

    openCV.imshow("" + str(images), test_image)

    test_features, test_hog_image = hog(test_image, orientations=4, block_norm='L2', pixels_per_cell=(8, 8),
                                        cells_per_block=(2, 2), visualize=True, multichannel=False)

    openCV.imshow("hog image " + str(images), test_hog_image)
    test_images.append(test_image)

    test_images_features_list.append(test_features)

    print(test_features.shape)

    test_images_labels.append(os.path.splitext(images)[0])



    pass


print("Labels ",test_images_labels)


for label_index,labels in enumerate(test_images_labels):

    test_images_labels[label_index] = int (labels)

    pass



print()

print()
print("Labels ",test_images_labels)

loaded_model = pickle.load(open('finalized_model.sav', 'rb'))

result = loaded_model.predict(test_images_features_list)

result = result.tolist()

print()


print("test images results : ",result)

score = 0
score_list = []
urdu_word_list = []


output_dataFrame = pd.read_csv("new_urdu_words_1.csv",encoding="utf-8-sig",index_col=None)

urdu_words_array = np.array(output_dataFrame)

for j in range(len(result)):

    if test_images_labels[j] == result[j]:

        score_list.append(1)

        #urdu_word_list.append(urdu_words_array[result[j], 0])

    else:
        score_list.append(0)

    urdu_word_list.append(urdu_words_array[result[j], 0])
    pass

print()

print("score : " ,score_list)


print()
print("urdu words list : ",urdu_word_list)

print()
print()
print()

openCV.waitKey(0)
openCV.destroyAllWindows()
