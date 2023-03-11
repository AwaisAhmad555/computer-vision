import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from bidi.algorithm import get_display
import arabic_reshaper


urdu_text = "یشن"

urdu_text = arabic_reshaper.reshape(urdu_text)

urdu_text = get_display(urdu_text[::-1])

img = cv.imread('test.png',0)
img2 = cv.imread("urdu_word_result.jpg",0)

print(urdu_text)
cv.imshow("2",img2)
# Initiate ORB detector

#detector = cv.FastFeatureDetector_create()
sift =  cv.xfeatures2d.SIFT_create()
# find the keypoints with ORB
keypoints, descriptors = sift.detectAndCompute(img,None)

keypoints2, descriptors2 = sift.detectAndCompute(img2,None)
# compute the descriptors with ORB
#kp, des = detector.compute(img, kp)
# draw only keypoints location,not size and orientation
img = cv.drawKeypoints(img, keypoints, None, color=(0,255,0), flags=0)

img2 = cv.drawKeypoints(img2, keypoints2, None, color=(0,255,0), flags=0)

plt.imshow(img), plt.show()
plt.imshow(img2), plt.show()

cv.imshow("",img)
cv.imshow("2",img2)


brute_force_match = cv.BFMatcher()

matches = brute_force_match.knnMatch(descriptors,descriptors2,k=2)

good = []

for m,n in matches:

    if m.distance < 0.75 * n.distance:

        good.append([m])

        pass

    pass

print("Matching score : ",len(good))

print(keypoints)
print()
print(descriptors)
print()
print(descriptors.shape)

img3 = cv.drawMatchesKnn(img,keypoints,img2,keypoints2,good,None,flags=2)

cv.imshow("matches",img3)
cv.waitKey(0)
cv.destroyAllWindows()


