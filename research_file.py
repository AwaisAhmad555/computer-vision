
#########################################image preprocessing program######################################

import cv2 as opencv
import os
import numpy as np
import pandas as pd


class preprocessing:

    def __init__(self,image):

        self.image = opencv.cvtColor(image,opencv.COLOR_RGB2GRAY,None)

        pass

    def projection(self,img, type: str):

        if type == 'horizontal':

            projections = np.sum(img, axis=1).astype('int32')

        elif type == 'vertical':

            projections = np.sum(img, axis=0).astype('int32')
            pass

        return projections
        pass

###########################################################################################################
    #function to calculate the horizontal projection histogram scores to find best angle of rotation
###########################################################################################################

    def projection_score_calculation(self,blank_image,horizontal_projection_list):

        height = len(blank_image[:, 0])
        width = len(blank_image[0, :])

        (center_X, center_Y) = (width // 2, height // 2)



        # Syntax: cv2.line(image, start_point, end_point, color, thickness)

        for row in range(height):

            opencv.line(img=blank_image, pt1=(0, row), pt2=(int(horizontal_projection_list[row] * width / height), row), color=(255, 255, 255), thickness=1)


            pass

        score = np.sum((horizontal_projection_list[1:] - horizontal_projection_list[:-1]) ** 2)


        return score
        pass

###########################################################################################################
#                                         skew correction function
###########################################################################################################



    def image_deskew(self,binary_image):


        height = len(binary_image[:, 0])
        width = len(binary_image[0, :])

        # calculating center of image as rotation point for rotation then rotation matrix

        (center_X, center_Y) = (width // 2, height // 2)

        blankImage = np.zeros((height, width, 1), np.uint8)


        #creating angles list for calculating the horizontal projections score
        #[-10  -9  -8  -7  -6  -5  -4  -3  -2  -1   0   1   2   3   4   5   6   7   8   9  10]


        counter_size = 1

        initial_value = 20

        angle_list = np.arange(-initial_value, initial_value + counter_size, counter_size)


        scorelist = []



        for angle in angle_list:


            #calculating different histograms on all angles in angle list to find maximum horizontal projection
            #histogram value

            rotation_matrix = opencv.getRotationMatrix2D((center_X, center_Y), angle=angle, scale=1.0)
            rotated_image = opencv.warpAffine(binary_image, rotation_matrix, (width, height))

            horizontal_projection_list = self.projection(rotated_image, type='horizontal')

            #calculating best horizontal projection histogram score

            score = self.projection_score_calculation(blank_image=blankImage,
                                              horizontal_projection_list=horizontal_projection_list)


            scorelist.append(score)


            pass


        best_score = np.argmax(np.array(scorelist))

        best_score_angle = angle_list[best_score]


        #print(best_score_angle)

        rotation_matrix = opencv.getRotationMatrix2D((center_X, center_Y), angle=best_score_angle, scale=1.0)
        rotated_image = opencv.warpAffine(binary_image, rotation_matrix, (width, height))



        return rotated_image
        pass

###########################################################################################################
#                                         Image binarization function
###########################################################################################################

    def image_binarization(self):


        kernel = np.ones((1, 1), np.uint8)

        binary_image = self.image

        param, binary_image = opencv.threshold(binary_image,200,255,opencv.THRESH_BINARY_INV,None)

        binary_image = opencv.dilate(binary_image, kernel, iterations=1)

        #binary_image = opencv.GaussianBlur(binary_image, (1, 1), sigmaX=1, sigmaY=1)


        binary_image = binary_image/255

        return binary_image


    pass

