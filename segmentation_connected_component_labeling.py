import cv2 as opencv
import numpy as np
from numpy.distutils.system_info import openblas_info


def extracting_connected_components(image):

    ########### image preprocessing (converting to grayscale and binarizing image ###############
    img = image

    img = 255 - img

    img = opencv.cvtColor(img, opencv.COLOR_RGB2GRAY)

    threshold_img = opencv.threshold(img, 0, 255, opencv.THRESH_BINARY + opencv.THRESH_OTSU)[1]

    threshold_img = np.pad(threshold_img, ((10, 10), (10, 10)), constant_values=0)

    num_labels, labels = opencv.connectedComponents(threshold_img)

    label_hue = np.uint8(179 * labels / np.max(labels))

    blank_ch = 255 * np.ones_like(label_hue)

    labeled_img = opencv.merge([label_hue, blank_ch, blank_ch])

    # Converting cvt to BGR
    labeled_img = opencv.cvtColor(labeled_img, opencv.COLOR_HSV2BGR)

    # set bg label to black
    labeled_img[label_hue == 0] = 255

    #opencv.imshow("label image", labeled_img)

    labeled_img[label_hue == 0] = 0

    #print(np.unique(label_hue))

    segment_image = labeled_img


    return num_labels, label_hue, segment_image
    pass



############################################################################

def extracting_ligatures(num_labels, label_hue, segment_image):

    bounding_boxes_list = []

    for i in range(num_labels):

        single_label = np.unique(label_hue)[i]

        segment_image = opencv.cvtColor(segment_image, opencv.COLOR_HSV2BGR)

        segment_image[label_hue != single_label] = 0

        segment_image[label_hue == single_label] = 255

        ###########################      finding contours

        grayscale_segment_image = opencv.cvtColor(segment_image, opencv.COLOR_RGB2GRAY)

        thresh_segment_image = \
        opencv.threshold(grayscale_segment_image, 0, 255, opencv.THRESH_BINARY + opencv.THRESH_OTSU)[1]

        contours, hierarchy = opencv.findContours(thresh_segment_image, opencv.RETR_EXTERNAL,
                                                  opencv.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            x, y, w, h = opencv.boundingRect(contour)

            rect = opencv.rectangle(segment_image, (x, y), (x + w, y + h), (0, 255, 0), 1)

            pass

        first_index = x
        last_index = x + w
        first_y_index = y
        last_y_index = y + h

        if i > 0:
            bounding_boxes_list.append([first_index, last_index, first_y_index, last_y_index, single_label])

            pass

        pass


    return bounding_boxes_list
    pass


def separating_diacritics(new_list):


    last_y_index_list = []

    for k in range(len(new_list)):

        last_y_index_list.append(new_list[k][3] - new_list[k][2])

        pass

    #print(last_y_index_list)

    #print(max(last_y_index_list))

    max_height = max(last_y_index_list)

    diacritics_list = []

    for j in range(len(new_list)):

        segment_label = new_list[j][len(new_list[j]) - 1]

        ligature_height = new_list[j][3] - new_list[j][2]

        if ligature_height / max_height < 0.28:
            first_index = new_list[j][0]
            last_index = new_list[j][1]
            first_y_index = new_list[j][2]
            last_y_index = new_list[j][3]
            diacritic_label = new_list[j][4]

            diacritics_list.append([first_index, last_index, first_y_index, last_y_index, diacritic_label])

            pass

        pass

    #print()
    #print("Diacritics list : ")
    #print(diacritics_list)





    return diacritics_list,max_height
    pass


def ligature_association(new_list,diacritics_list,label_hue,max_height):


    for a in range(len(new_list)):

        ligature_height = new_list[a][3] - new_list[a][2]

        ################ label association will be done here |  |
        #                                                    |  |
        #                                                    |  |
        #                                                   \|  |/
        #                                                    \  /
        #                                                     \/

        if ligature_height / max_height > 0.28:

            #new list is the list having main ligature bodies with height at least 25% of
            # maximum height among all ligatures

            first_index = new_list[a][0]
            last_index = new_list[a][1]
            first_y_index = new_list[a][2]
            last_y_index = new_list[a][3]
            ligature_label = new_list[a][4]

            for index in range(len(diacritics_list)):

                diacritic_start_index = diacritics_list[index][0]
                diacritic_label = diacritics_list[index][4]

               # LOGIC = start index of diacritic will always be greater than first index of
                # ligature body i.e little bit ahead of starting index
               # whereas the diacritic start index will always remain less than the last index
                # of ligature main body i.e behind the last index of main body

                #                \        --        /
                #                 \________________/
                #      start(first_index)        end(last_index)

                if diacritic_start_index >= first_index and diacritic_start_index <= last_index:
                    segment_label = new_list[a][len(new_list[a]) - 1]

                    label_hue[label_hue == diacritic_label] = segment_label

                    pass

                pass

            pass

        pass



    return label_hue
    pass


def ligature_segmentation(label_hue,max_height,segment_image):

    complete_ligature_list = []

    ligature_max_height = max_height

    new_label_list = np.unique(label_hue)

    #print(new_label_list)

    for i in range(len(new_label_list)):

        segment_image[label_hue != new_label_list[i]] = 0

        segment_image[label_hue == new_label_list[i]] = 255

        new_grayscale_segment_image = opencv.cvtColor(segment_image, opencv.COLOR_RGB2GRAY)

        new_grayscale_segment_image = \
        opencv.threshold(new_grayscale_segment_image, 0, 255, opencv.THRESH_BINARY + opencv.THRESH_OTSU)[1]

        ligature_contours = \
        opencv.findContours(new_grayscale_segment_image, opencv.RETR_EXTERNAL, opencv.CHAIN_APPROX_SIMPLE)[0]

        #using contours of ligatures, extracting the initial and final indexes of these ligatures (x,y,x+w,y+h)


        for contour in ligature_contours:

            x, y, w, h = opencv.boundingRect(contour)

            #rect = opencv.rectangle(segment_image, (x, y), (x + w, y + h), (0, 255, 0), 1)

            if h / ligature_max_height > 0.28:

                if new_label_list[i] > 0:
                    first_index = x
                    last_index = x + w
                    first_y_index = y
                    last_y_index = y + h
                    ligature_label = new_label_list[i]

                    complete_ligature_list.append(
                        [first_index, last_index, first_y_index, last_y_index, ligature_label])

                    pass

                pass

            pass

        pass

    complete_ligature_list = sorted(complete_ligature_list, key=lambda z: z[0], reverse=True)


    #extracting each ligature from labelled image and creating new image for each
    # ligature. All these ligatures images are stored in ligature list

    ligature_images_list = []

    for j in range(len(complete_ligature_list)):
        first_index = complete_ligature_list[j][0]
        last_index = complete_ligature_list[j][1]
        first_y_index = complete_ligature_list[j][2]
        last_y_index = complete_ligature_list[j][3]
        complete_ligature_label = complete_ligature_list[j][len(complete_ligature_list[j]) - 1]

        segment_image[label_hue != complete_ligature_label] = 0

        segment_image[label_hue == complete_ligature_label] = 255

        # rect = opencv.rectangle(segment_image, (first_index, first_y_index), (last_index, last_y_index),
        #                        (0, 255, 0), 1)

        # opencv.putText(segment_image, str((last_y_index - first_y_index)/max_height), (first_index + 10, last_y_index + 20), opencv.FONT_HERSHEY_SIMPLEX,
        #               0.4, (36, 255, 12), 1)

        final_segment_image = np.pad(opencv.cvtColor(segment_image, opencv.COLOR_RGB2GRAY)[:, first_index - 0:last_index + 14],
            ((0, 0), (14, 0)), constant_values=0)

        #opencv.imshow("label image No. " + str(j), final_segment_image)

        ligature_images_list.append(final_segment_image)

        pass

    return ligature_images_list
    pass



##################### main program definition

def connected_component_segmentation(img):


    num_labels, label_hue, segment_image = extracting_connected_components(image=img)

    ligatures_list = extracting_ligatures(num_labels, label_hue, segment_image)

    bounding_boxes_list = ligatures_list

    #print()

    new_list = sorted(bounding_boxes_list, key=lambda a: a[0], reverse=True)

    #print(new_list)

    if len(new_list)>0:

        diacritics_list, max_height = separating_diacritics(new_list=new_list)

        label_hue = ligature_association(new_list=new_list, diacritics_list=diacritics_list, label_hue=label_hue,
                                         max_height=max_height)

        #################################################################################

        ligatures_images_list = ligature_segmentation(label_hue, max_height, segment_image)


        pass

    else:

        ligatures_images_list = []

        pass



    return ligatures_images_list
    pass


#image = opencv.imread("upti.png")

#ligatures_images_list = connected_component_segmentation(img=image)


#print("----------------------------------")
#print(len(ligatures_images_list))







"""opencv.waitKey(0)

opencv.destroyAllWindows()"""
