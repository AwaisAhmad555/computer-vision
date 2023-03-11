import skimage
import os
from PIL import Image
import arabic_reshaper
from bidi.algorithm import get_display
import cv2

import glob

images_name_list = []
images_names = []

address_list = []

folder_list = os.listdir("urdu_chars_dataset")

for folder in folder_list:

    images_directories = os.listdir("urdu_chars_dataset/" + str(folder))

    for single_image_directory in images_directories:
        images_name_list.append(single_image_directory)

        pass

    pass

for single_image_name in images_name_list:



    images_names.append(os.path.splitext(single_image_name)[0])



    pass


print(images_names)

print()

print(folder_list)


"""

path = 'upti.png'

image = opencv.imread(path)

image = opencv.cvtColor(image,opencv.COLOR_RGB2GRAY)

parameters, threshold_image = opencv.threshold(image,0,255,opencv.THRESH_BINARY_INV + opencv.THRESH_OTSU)

opencv.imshow("Binarized Image",threshold_image)

opencv.waitKey(0)

opencv.destroyAllWindows()

"""