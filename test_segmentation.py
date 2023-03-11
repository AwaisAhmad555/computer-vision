from segmentation_connected_component_labeling import connected_component_segmentation
import numpy as np
import os
import cv2 as opencv


path = "upti.png"

image = opencv.imread(path)

#image = np.invert(image)

image = opencv.cvtColor(image,opencv.COLOR_RGB2GRAY)

parameter, threshold_image = opencv.threshold(image,0,255,opencv.THRESH_BINARY + opencv.THRESH_OTSU)

image = opencv.cvtColor(threshold_image,opencv.COLOR_GRAY2RGB)

segment_images_list = connected_component_segmentation(image)

for idx,single_image in enumerate(segment_images_list):

    opencv.imshow(""+str(idx),single_image)

    opencv.imwrite("upti\\segmentation_output\\" + str(idx)+".png",single_image)

    pass

opencv.imshow("image",threshold_image)

opencv.waitKey(0)
opencv.destroyAllWindows()