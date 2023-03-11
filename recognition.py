import cv2 as opencv
import numpy as np
import pandas as pd
import os
import pickle
import arabic_reshaper
from bidi.algorithm import get_display
from features_extraction import *



joiners = ["ب", "پ", "ت", "ٹ", "ث", "ج", "چ", "ح", "خ",
           "س", "ش", "ص", "ض", "ط", "ظ", "ع", "غ", "ف", "ق", "ک", "گ", "ل", "م",
           "ن", "ہ", "ھ", "ی" , "ئ"]


non_joiners = ["ا", "آ", "د", "ڈ", "ذ", "ر", "ڑ", "ز", "ژ",
               "و","ؤ", "ۓ", "ں", "ے"]


reshaper = arabic_reshaper.ArabicReshaper(
        arabic_reshaper.config_for_true_type_font(
            'arial.ttf',
            arabic_reshaper.ENABLE_ALL_LIGATURES
        )
    )

def load_query_images(path):

    query_images_list = []

    images_names = os.listdir(path=path)


    sorted_images_names = sorted(images_names,key=lambda x: int (os.path.splitext(x)[0]))


    for single_image_name in sorted_images_names:

        print()

        print(int (os.path.splitext(single_image_name)[0]))

        print()

        image_path = os.path.join(path,single_image_name)

        image = opencv.imread(image_path)

        #param, threshold_image = opencv.threshold(image,200,255,opencv.THRESH_BINARY)

        query_images_list.append(image)


        pass


    return query_images_list
    pass


def text_generator(text_dataFrame : pd.DataFrame, y_predict):


    text = np.array(text_dataFrame)[y_predict, 0]

    return text
    pass

def results_evaluation(ground_truth : str,predicted_text_list):

    file1 = open(ground_truth, 'r', encoding='utf-8-sig')
    Lines = file1.readlines()

    count = 0

    #array = Lines[0].split()

    array = []

    for idx in range(len(Lines)):

        for sub_word in Lines[idx].split():

            array.append(sub_word)

            pass


        pass

    # splitting text words to non joined words

    wordlist = []

    words_list = []

    for word in array:

        for subword in split(word):


            words_list.append(subword)


            pass

        pass



    #

    # removing/ pruning black spaces
    new_list = []

    for index, word in enumerate(words_list):

        if word != "":

            new_list.append(word)

            pass

        pass

    score = 0

    ground_truth_text = ""

    for i in range(len(new_list)):

        if new_list[i] == predicted_text_list[i]:

            #print("\n Match")

            score = score + 1

            pass

        else:

            score = score + 0

            #print("\n Not Matched" + predicted_text_list[i] + " " + str (i))

            pass


        ground_truth_text = ground_truth_text + " " + new_list[i]


        """for j in range(len(new_list)):



                    pass"""


        pass


    #print(len(new_list))

    accuracy = (score/len(new_list)) * 100

    accuracy = str (accuracy) + " % "



    return accuracy,ground_truth_text
    pass





def split(word):

    joined_words_list = []

    urdu_word = []

    complete_urdu_word = []

    for word_idx,char in enumerate(word):


        for id,character in enumerate(joiners):

            if char == joiners[id]:

                urdu_word.append(char)

            pass


        for idx,character in enumerate(non_joiners):

            if char == non_joiners[idx]:

                urdu_word.append(char)

                complete_urdu_word = urdu_word



                complete_word = ""

                for single_word in complete_urdu_word:
                    complete_word = single_word + complete_word

                    pass

                bidi_text = get_display(complete_word)
                temporary_text = reshaper.reshape(bidi_text)

                joined_words_list.append(temporary_text)

                urdu_word = []



            pass


        if word_idx == len(word)-1:

            complete_urdu_word = urdu_word

            complete_word = ""

            for single_word in complete_urdu_word:
                complete_word = single_word + complete_word

                pass

            bidi_text = get_display(complete_word)
            temporary_text = reshaper.reshape(bidi_text)

            joined_words_list.append(temporary_text)

            urdu_word = []

            pass



        pass

    """complete_word = ""

    for single_word in complete_urdu_word:

        complete_word = single_word + complete_word

        pass

    bidi_text = get_display(complete_word)
    temporary_text = reshaper.reshape(bidi_text)"""


    return joined_words_list







######################### main program######################




query_images_path = "temporary\\segment_images"

query_images_list = load_query_images(query_images_path)


features_list = []

for idx,image in enumerate(query_images_list):


    img = opencv.cvtColor(image, opencv.COLOR_RGB2GRAY, None)

    thresh, img = opencv.threshold(img, 200, 255, opencv.THRESH_BINARY, None)

    crop_image = cut_extra_height(img=img)


    query_image_features = get_features(img=crop_image)


    features_list.append(query_image_features)
    #break
    pass


pickle.dump(features_list,open("temporary\\query_images_2_features_list.pkl","wb"))

text_dataframe = pd.read_csv("dataset\\dataset.csv")

features_list = pickle.load(open("temporary\\query_images_2_features_list.pkl","rb"))


for feature in features_list:

    print(feature)

    pass

print()
print(len(feature))
print()
# load the model from disk


filename = 'custom_features_model.sav'

loaded_model = pickle.load(open(filename, 'rb'))

print(loaded_model)



y_predict = loaded_model.predict(features_list)

y_predict = y_predict.tolist()

print(y_predict)

text_list  = []
for prediction in y_predict:

    #print()
    #print(prediction)
    #print()

    text = text_generator(text_dataFrame=text_dataframe,y_predict=prediction)

    text_list.append(text)
    #print()

    pass


f = open("output.txt", "w",encoding="utf-8-sig")


paragraph_text = ""


for word in text_list:

    paragraph_text = paragraph_text + " " + word

    pass

print()
print("prediction : ")
print(paragraph_text)

f.write(paragraph_text)
f.close()

#print()


ground_truth_address = 'testing samples\\2\\ground_truth.txt'

#print()

accuracy,ground_truth_text = results_evaluation(ground_truth_address,text_list)

print()
print("Ground Truth :")
print(ground_truth_text)


print()
print("prediction / Recognition accuracy : " + accuracy)
