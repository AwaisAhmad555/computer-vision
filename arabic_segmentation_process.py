import cv2 as opencv
import numpy as np
import pandas as pd
import os
from research_file import preprocessing
from research_file_2 import segmentation
from morphological_operations import *
from contour_based_segmentation import contour_based_subwords_segmentation


####################################### ------ main program ------- ###########################################

image = opencv.imread("testing samples\\arabic\\arabic.png")

#kernel = np.ones((1,1), np.uint8)

#image = opencv.erode(image, kernel, iterations=1)

#image = 255 - image

opencv.imshow("image",image)


###################################### creating image preprocessing class object

preprocessing_object = preprocessing(image=image)

binary_image = preprocessing_object.image_binarization()



opencv.imshow("binary img", binary_image)


deskew_image = preprocessing_object.image_deskew(binary_image)


opencv.imshow("rotation image deskewed",deskew_image)

rgb_image = deskew_image * 255




if os.path.isdir("temporary\\arabic_deskew_image"):
    pass
else:
    os.makedirs("temporary\\arabic_deskew_image")


if os.path.isdir("temporary\\arabic_segment_images"):
    pass
else:
    os.makedirs("temporary\\arabic_segment_images")


if os.path.isdir("temporary\\arabic_segment_lines_images"):
    pass
else:
    os.makedirs("temporary\\arabic_segment_lines_images")


opencv.imwrite("temporary\\arabic_deskew_image\\deskew_img.jpg",deskew_image*255)


###################################################################

################### Deleting already existed previous line images

dir = 'temporary\\arabic_segment_lines_images'

for f in os.listdir(dir):

    os.remove(os.path.join(dir, f))

    pass


######################### creating segmentation class object instance

segmentation_object = segmentation(image=image)



preprocessed_image = opencv.imread("temporary\\arabic_deskew_image\\deskew_img.jpg")

opencv.imshow("preprocessed_image",preprocessed_image)


projection_list = segmentation_object.projection(deskew_image,type="horizontal")



line_images = segmentation_object.line_segmentation(horizontal_projection_list=projection_list,preprocessed_image=preprocessed_image)



line_number = 0
for idx,images in enumerate(line_images):

    line_number = line_number + 1

    images = np.pad(images, ((10, 10), (10, 10), (0, 0)), mode='constant', constant_values=0)


    opencv.imwrite("temporary\\arabic_segment_lines_images\\" + str(line_number) + ".png", images)


    pass


######### deleting all previous segmented images in
######### segment images folder

dir = 'temporary\\arabic_segment_images'
for f in os.listdir(dir):

    os.remove(os.path.join(dir, f))

    pass


############################################################


#vertical projections list word partial word segmentation

line_images_projection_list = []

for single_line_image in line_images:

    #single_line_image = erosion(single_line_image)

    vertical_projection_list = segmentation_object.projection(opencv.cvtColor(single_line_image,opencv.COLOR_RGB2GRAY,None)/255,type="vertical")

    line_images_projection_list.append(vertical_projection_list)

    pass


##############################################################################################

start_index_list , end_index_list = segmentation_object.line_images_indexes_return()


print(start_index_list)

print()

print(end_index_list)



all_words_images_list = []


for idx, line_img in enumerate(line_images):

    words_images_list = segmentation_object.partial_word_segmentation(line_images_projection_list[idx],line_images[idx],line_start_index=start_index_list[idx],line_end_index=end_index_list[idx],threshold_value=0)

    all_words_images_list.append(words_images_list)

    pass


label = 0
for idx,word_image_single_list in enumerate(all_words_images_list):

    word_image_single_list.reverse()


    for img_idx,single_word_image in enumerate(word_image_single_list):



        single_word_image = opencv.cvtColor(single_word_image,opencv.COLOR_RGB2GRAY,None)

        single_word_image = np.pad(single_word_image, ((2, 2), (2, 2)), mode='constant', constant_values=0)


        parameters, single_word_image = opencv.threshold(single_word_image, 200, 255, opencv.THRESH_BINARY, None)

        single_word_image = opencv.cvtColor(single_word_image, opencv.COLOR_GRAY2RGB, None)

        single_word_image = contour_based_subwords_segmentation(single_word_image)


        for each_single_word_image in single_word_image:

            label = label + 1

            #each_single_word_image = np.pad(each_single_word_image, ((5, 5), (5, 5)), mode='constant', constant_values=0)

            opencv.imwrite("temporary\\arabic_segment_images\\" + str(label) + ".png", each_single_word_image)

            pass




        pass

    pass


copy_image = segmentation_object.segment_image_display()

opencv.imshow("segment image",copy_image)







print(projection_list)

opencv.waitKey(0)
opencv.destroyAllWindows()