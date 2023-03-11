import numpy as np
import cv2 as openCV
import matplotlib.pyplot as plot


class segmentation:

    def __init__(self,image):

        self.image = image
        self.type : str

        self.copy = image.copy()

        self.line_start_index_list = []
        self.line_last_index_list = []


        pass

    def projection(self):

        if self.type == 'horizontal':

            projections = np.sum(self.image, 1).astype('int32')
        elif self.type == 'vertical':

            projections = np.sum(self.image, 0).astype('int32')
            pass

        return projections
        pass

    def preprocessing(self):

        gray_img = openCV.cvtColor(self.image, openCV.COLOR_RGB2GRAY)

        parameter, threshold_img = openCV.threshold(gray_img, 220, 255, openCV.THRESH_BINARY_INV)

        threshold_img = openCV.GaussianBlur(threshold_img, (1, 1), sigmaX=1, sigmaY=1)

        return threshold_img

    def line_segmentation(self, projections_list):

        start = -1
        end_flag = 0

        start_index = 0
        end_index = 0

        text_lines = []

        for idx, horizontal_projection in enumerate(projections_list):

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
                line_img = np.pad(self.image[start_index:end_index, :], ((10, 10), (0, 0), (0, 0)), mode='constant',
                                  constant_values=255)
                text_lines.append(line_img)

                end_flag = 0

                self.line_start_index_list.append(start_index)
                self.line_last_index_list.append(end_index)

                pass

        return text_lines

    def word_segmentation(self,projections_list, line_image, line_start_index, line_end_index):

        flag = 0
        start = -1
        end = 0
        gap_flag = 0

        words_list = []

        for idx, single_projection in enumerate(projections_list):

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

            if gap_flag == 1:
                end_index = idx
                start = start + 1
                gap_flag = 0

                pass

            if start == 1:
                # openCV.imshow(""+str(idx),img[:,start_index:end_index])
                self.copy[line_start_index:line_end_index, start_index:end_index, 2] = 0
                words_list.append(line_image[:, start_index:end_index])

                start = -1

            pass

        return words_list




    pass


segmentation = segmentation()

