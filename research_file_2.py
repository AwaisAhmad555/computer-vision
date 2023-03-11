import cv2 as opencv
import numpy as np
import pandas as pd
import os
from research_file import preprocessing


class segmentation:


    def __init__(self,image):

        self.image = image
        self.copy = self.image.copy()
        self.line_start_index_list = []
        self.line_end_index_list = []

        pass


    def projection(self,img, type: str):

        if type == 'horizontal':

            projections = np.sum(img, axis=1).astype('int32')

        elif type == 'vertical':

            projections = np.sum(img, axis=0).astype('int32')
            pass

        return projections
        pass



    def line_segmentation(self,horizontal_projection_list,preprocessed_image):

        start = -1
        end_flag = 0

        start_index = 0
        end_index = 0

        text_lines = []

        for idx, horizontal_projection in enumerate(horizontal_projection_list):

            if horizontal_projection != 0 and start == -1:
                start_index = idx

                start = start + 1

                pass

            if horizontal_projection == 0 and start != -1:
                end_index = idx

                start = -1

                end_flag = 1

                pass

            if end_flag == 1:
                line_img = np.pad(preprocessed_image[start_index:end_index, :], ((0, 0), (0, 0), (0, 0)), mode='constant', constant_values=0)
                #line_img = opencv.erode(line_img,np.zeros(2,2),None)
                text_lines.append(line_img)

                end_flag = 0

                self.line_start_index_list.append(start_index)
                self.line_end_index_list.append(end_index)

                pass


        return text_lines
        pass


    def line_images_indexes_return(self):



        return self.line_start_index_list, self.line_end_index_list
        pass


    def partial_word_segmentation(self,vertical_projections_list,line_image,line_start_index,line_end_index,threshold_value):

        flag = 0
        start = -1
        end = 0
        gap_flag = 0

        words_list = []

        for idx, single_projection in enumerate(vertical_projections_list):

            # print(single_projection)
            # print()

            if single_projection != 0:
                # copy[:, idx, 0] = 0

                pass

            if single_projection != 0 and start == -1:
                start_index = idx
                # openCV.imshow(""+str(idx),img[:,idx:])

                start = start + 1
                pass

            if single_projection == 0 and start != -1:
                gap_flag = gap_flag + 1

                pass

            if single_projection == 0 and gap_flag > threshold_value+1:
                end_index = idx
                start = start + 1
                gap_flag = 0

                pass

            if start == 1:
                # openCV.imshow(""+str(idx),img[:,start_index:end_index])

                words_list.append(line_image[:, start_index:end_index])

                start = -1
                self.copy[line_start_index:line_end_index, start_index:end_index, 2] = 0
                pass


            pass

        return words_list


    def segment_image_display(self):



        return self.copy
        pass



    pass





