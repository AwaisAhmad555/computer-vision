import pandas as pd
import numpy as np
import os
import cv2 as openCV

image_1 = openCV.imread("test.png")

image_2 = openCV.imread("test 2.jpg")

#image_2 = openCV.imread("hamza.png")

image_1 = openCV.imread("test/13.png")

image_2 = openCV.imread("test/14.png")




sift = openCV.xfeatures2d.SIFT_create()

keypoints, descriptors = sift.detectAndCompute(image_1, None)


new_word_image = openCV.drawKeypoints(image_1, keypoints, None, color=(0, 255, 0), flags=0)


keypoints_2, descriptors_2 = sift.detectAndCompute(image_2, None)


new_word_image_2 = openCV.drawKeypoints(image_2, keypoints_2, None, color=(0, 255, 0), flags=0)


index_params = dict(algorithm=0, trees=5)
search_params = dict()
flann = openCV.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(descriptors, descriptors_2, k=2)

score = []

for m,n in matches:

    if m.distance < 0.75 * n.distance:

        score.append([m])

        pass

    pass

print(len(score))

result = openCV.drawMatchesKnn(image_1,keypoints,image_2,keypoints_2,score,None)

openCV.imshow("new_word_image",new_word_image)


openCV.imshow("new_word_image_2",new_word_image_2)

openCV.imshow("Correlation", result)

print(descriptors.shape)

openCV.waitKey(0)

openCV.destroyAllWindows()
