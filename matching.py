import numpy as np
import pandas as pd
import cv2 as openCV
import os


data_file = open("urdu_descriptors.csv", 'r',encoding='utf-8-sig')
data_list = data_file.readlines()
data_file.close()

print(len(data_list))

#specify the record number in csv data_list object below
values_array = data_list[10]

values_array = values_array.split(',')

print(values_array)

new_array = []

new_array.append(values_array[1])

for idx in range(2,len(values_array)-1):

    if values_array[idx] != '':

        values_array[idx] = float (values_array[idx])

        new_array.append(values_array[idx])

        pass

    pass

print(values_array)

print(values_array[1])

print()

print(new_array)

print()

print(len(new_array[:-1]))


array_length = len(new_array[1:])/128

array_length = int (array_length)



float_array = np.asfarray(new_array[1:]).reshape(array_length,128)

print()


print(float_array)

print()

print(float_array.shape)

print()

print(array_length)

img = openCV.imread("hamza.png")


sift = openCV.xfeatures2d.SIFT_create()

keypoints, descriptors = sift.detectAndCompute(img, None)

new_img = openCV.drawKeypoints(img,keypoints=keypoints,outImage=None,color=(0,255,0),flags=None)


openCV.imshow("descriptor_img",new_img)

print()
print(descriptors.shape)
print()

print(descriptors)
print()
print()

index_params = dict(algorithm=0, trees=5)
search_params = dict()
flann = openCV.FlannBasedMatcher(index_params, search_params)

matches = flann.knnMatch(descriptors, descriptors, k=2)

score = []

for m,n in matches:

    if m.distance < 0.75 * n.distance:

        score.append([m])

        pass

    pass

print()
print("matching score : ")
print()

print(len(score))

openCV.waitKey(0)

openCV.destroyAllWindows()