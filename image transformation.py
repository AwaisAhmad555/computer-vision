import cv2 as opencv

import numpy as np
import matplotlib.pyplot as plt

import pywt
import pywt.data
from skimage.feature import hog


image = opencv.imread("character.png")

image = opencv.resize(image,(100,100),None)

image = opencv.cvtColor(image, opencv.COLOR_RGB2GRAY, None, None)

threshold_value , image = opencv.threshold(image,200,255,opencv.THRESH_BINARY)


LL, (LH, HL, HH) = pywt.dwt2(image,'bior1.3')

test_features, test_hog_image = hog(image, orientations=4, block_norm='L2', pixels_per_cell=(8, 8),
                                        cells_per_block=(2, 2), visualize=True, multichannel=False)


opencv.imshow("image",image)


opencv.imshow("test_hog_image",test_hog_image)

print(len(test_features))

opencv.waitKey(0)
opencv.destroyAllWindows()