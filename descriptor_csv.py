import os
import pandas as pd
import numpy as np
import cv2 as openCV


values = ["one","two","three","four"]

values_array = np.array(values)

print(values_array)

dataframe = pd.DataFrame(values_array)

print()

print(dataframe)

dataframe.to_csv("my_csv.csv")


#capture = openCV.VideoCapture(0)

#while True:

    #success, image = capture.read()

    #openCV.imshow("webcam",image)
    #openCV.waitKey(1)