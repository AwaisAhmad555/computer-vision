from segmentation_connected_component_labeling import connected_component_segmentation
import numpy as np
import cv2 as openCV
import os
from features_extraction import *
import pickle


root_path = "upti\\upti_extracted_images\\"

folders_list = os.listdir(root_path)

for folder in folders_list:

    folder_path = os.path.join(root_path,folder)

    files = os.listdir(folder_path)

    for file in files:

        file_extension = file.split(".")[-1]

        print(file_extension)

        if file_extension == "png":

            image_path = os.path.join(folder_path,file)

            image = opencv.imread(image_path)

            #image = np.invert(image)

            opencv.imshow("image",image)

            query_image = image

            label = int (folder)


            pass



        break
        pass

    break

    pass


"""segmented_images = connected_component_segmentation(img=image)

for idx,img in enumerate(segmented_images):

    opencv.imshow(" "+str(idx),img)

    pass"""

filename = 'upti\\upti_custom_features_model.sav'

loaded_model = pickle.load(open(filename, 'rb'))

print(loaded_model)

path = "upti\\upti_extracted_images\\2305\\3.png"

label = path.split("\\")[-2]

print()
print("Annotated Label : " + str(label))


query_image = openCV.imread(path)

openCV.imshow("image",query_image)

query_image = openCV.cvtColor(query_image, openCV.COLOR_RGB2GRAY, None)

thresh, query_image = openCV.threshold(query_image, 200, 255, openCV.THRESH_BINARY, None)

new_crop_image = cut_extra_height(img=query_image)

custom_features = get_features(new_crop_image)

X = custom_features
y = label

result = loaded_model.predict([X])


print()
print("Prediction : ")
print(result.tolist())


opencv.waitKey(0)
opencv.destroyAllWindows()