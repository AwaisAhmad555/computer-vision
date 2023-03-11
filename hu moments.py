import cv2 as opencv
import numpy as np
import pandas as pd
import math
from math import copysign
from math import log10


image = opencv.imread("dataset\\urdu_dataset\\61\\67.png")

opencv.imshow("image",image)

image = opencv.cvtColor(image,opencv.COLOR_RGB2GRAY,None)

param, image = opencv.threshold(image,128,255,opencv.THRESH_BINARY,None)


moments = opencv.moments(image)

hu_moments = opencv.HuMoments(moments)

print(moments)

print()

print(hu_moments)



for i in range(len(hu_moments)):

    hu_moments[i] = -1 * copysign(1.0,hu_moments[i]) * log10(abs(hu_moments[i]))

    pass



print()

print("log transformed values : ")

print(hu_moments.reshape(-1).tolist())


opencv.waitKey(0)
opencv.destroyAllWindows()