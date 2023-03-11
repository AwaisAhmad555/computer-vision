import cv2 as openCV
import numpy as np
import pandas as pd


image  = openCV.imread("character.png")

openCV.imshow("1",image)

new_image = image.copy()

pixel_list = []

image = openCV.cvtColor(image,openCV.COLOR_RGB2GRAY)

parameter, threshold_image = openCV.threshold(image,200,250,openCV.THRESH_BINARY,None)

openCV.imshow("2",image)

print(len(image[:,0]))
print()
print(len(image[0,:]))

print()
print(image.shape)



print(image)

new_image[:,:,:] = 0

for i in range(len(threshold_image[:,0])):

    for j in range(len(threshold_image[i,:])-1):

        if threshold_image[i,j] - threshold_image[i,j+1] != 0:

            new_image[i,j,:] = 255

            pass

        pass

    pass


for j in range(len(threshold_image[0,:])):

    for i in range(len(threshold_image[:,j])-1):

        if threshold_image[i,j] - threshold_image[i+1,j] != 0:

            new_image[i,j,:] = 255

            pass

        pass

    pass

openCV.imshow("new",threshold_image)
openCV.imshow("new",new_image)

openCV.waitKey(0)
openCV.destroyAllWindows()