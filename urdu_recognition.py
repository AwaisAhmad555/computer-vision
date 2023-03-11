import cv2 as opencv
import numpy as np
import pandas as pd
import os
import pickle
import arabic_reshaper
from bidi.algorithm import get_display
from features_extraction import *
from contour_based_segmentation import contour_based_subwords_segmentation
from features_extraction import *





def load_query_images(path):

    query_images_list = []

    images_names = os.listdir(path=path)


    sorted_images_names = sorted(images_names,key=lambda x: int (os.path.splitext(x)[0]))


    for single_image_name in sorted_images_names:

        #print()

        #print(int (os.path.splitext(single_image_name)[0]))

        #print()

        image_path = os.path.join(path,single_image_name)

        image = opencv.imread(image_path)

        #param, threshold_image = opencv.threshold(image,200,255,opencv.THRESH_BINARY)

        query_images_list.append(image)


        pass


    return query_images_list
    pass


def word_generator(query_image, text_dataframe : pd.DataFrame, loaded_model):

    single_sub_word_images = contour_based_subwords_segmentation(query_image)

    feature_list = []

    for idx, single_image in enumerate(single_sub_word_images):


        #opencv.imshow("" + str(idx), single_image)

        crop_image = cut_extra_height(img=single_image)

        query_image_features = get_features(img=crop_image)

        feature_list.append(query_image_features)

        pass



    y_predictions = loaded_model.predict(feature_list)

    #print(y_predictions)



    text_list = []

    for prediction in y_predictions:
        # print()
        # print(prediction)
        # print()

        text = text_generator(text_dataFrame=text_dataframe, y_predict=prediction)

        text_list.append(text)
        # print()

        pass

    # f = open("output.txt", "w",encoding="utf-8-sig")

    paragraph_text = ""

    for word in text_list:
        paragraph_text = paragraph_text + word

        pass

    return paragraph_text
    pass


#########################################################

def text_generator(text_dataFrame : pd.DataFrame, y_predict):


    text = np.array(text_dataFrame)[y_predict, 0]

    return text
    pass


#####################################################

def text_recognition_function():


    query_images_path = "temporary\\segment_words_images"

    query_images_list = load_query_images(query_images_path)

    print(len(query_images_list))

    text_dataframe = pd.read_csv("dataset\\dataset.csv")

    filename = 'custom_features_model.sav'

    loaded_model = pickle.load(open(filename, 'rb'))

    words_list = []

    for each_query_image in query_images_list:
        word_text = word_generator(each_query_image, text_dataframe, loaded_model=loaded_model)

        words_list.append(word_text)

        pass

    paragraph = ""

    for single_word in words_list:
        paragraph = paragraph + " " + single_word

        pass

    print(paragraph)

    f = open("paragraph_output.txt", "w", encoding="utf-8-sig")

    f.write(paragraph)
    f.close()



    pass




#opencv.waitKey(0)

#opencv.destroyAllWindows()