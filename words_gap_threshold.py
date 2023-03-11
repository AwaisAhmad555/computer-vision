import cv2 as opencv
import numpy as np




def threshold_gap_calculation(vertical_projections_list):


    start = -1

    gap_flag = 0

    gap_flag_list = []

    single_gap = []

    intermediate = -1

    for idx, single_projection in enumerate(vertical_projections_list):



        if single_projection != 0 and start == -1:

            start = start + 1
            gap_flag_list.append(gap_flag)
            gap_flag = 0

            pass

        if single_projection == 0 and start != -1:

            gap_flag = gap_flag + 1

            intermediate = 1

            pass

        if single_projection != 0 and intermediate == 1:


            intermediate = -1
            start = -1

            pass



        """if single_projection != 0 and start != -1:

            start = -1

            pass"""



        pass

    sorted_threshold_list = np.sort(gap_flag_list)


    threshold_value_index = np.argmax(abs(sorted_threshold_list[1:] - sorted_threshold_list[:-1]))


    threshold_value = sorted_threshold_list[threshold_value_index]


    return gap_flag_list, threshold_value
    pass