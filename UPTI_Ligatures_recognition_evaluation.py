from segmentation_connected_component_labeling import connected_component_segmentation
import numpy as np
import cv2 as openCV
import os
from features_extraction import *
import pickle


UPTI_ligatures_list = []

root_path = "upti\\upti_extracted_images\\"

folders = os.listdir(root_path)

for folder in folders:

    images_folder_path = os.path.join(root_path,folder)


    images_list = os.listdir(images_folder_path)

    for image_name in images_list:

        image_path = os.path.join(images_folder_path,image_name)

        image = openCV.imread(image_path)


        Label = int (folder)


        UPTI_ligatures_list.append([image,Label])


        pass


    pass


UPTI_ligatures_images_dataset = pickle.dump(UPTI_ligatures_list,open("upti\\upti_ligature_images_dataset.pkl", "wb"))


"""openCV.waitKey(0)

openCV.destroyAllWindows()"""