import cv2 as opencv
import numpy as np
import pandas as pd

image = opencv.imread("urdu_sample.jpg")

opencv.imshow("original image",image)

image = opencv.cvtColor(image,opencv.COLOR_RGB2GRAY,None,None)

image = 255 - image

param, thresh_image = opencv.threshold(image,0,255,opencv.THRESH_BINARY + opencv.THRESH_OTSU,None)

opencv.imshow("threshold image",thresh_image)

opencv.waitKey(0)
opencv.destroyAllWindows()