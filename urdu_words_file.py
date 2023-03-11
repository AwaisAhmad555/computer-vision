import numpy as np
import PIL
from PIL import Image
import cv2 as openCV
import os
from urdu_images_file import words_generation

img_list = []
label_list = []
directory_list = []

for i in range(0,27):

    for j in range(0,40):
        directory_name, label, img = words_generation(i, j)
        img_list.append(img)
        label_list.append(label)
        directory_list.append(directory_name)
    pass

pass

for idx,image in enumerate(img_list):

    #openCV.imshow(label_list[idx],image)

    #+""+str(idx)

    print(str(idx)+" <----> "+label_list[idx])

    my_image = Image.fromarray(image)

    my_image.save("urdu_chars_dataset\\" + str(directory_list[idx]) + "\\" + str(label_list[idx]) + ".jpg")

    pass

openCV.waitKey(0)
openCV.destroyAllWindows()

for names in directory_list:

        print(names)
        print()

        pass
