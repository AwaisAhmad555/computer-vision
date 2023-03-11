import tensorflow
import os
import arabic_reshaper
import numpy as np
from bidi.algorithm import get_display
from PIL import Image, ImageFont, ImageDraw
import cv2 as openCV
import pandas as pd

joiners = ["ب", "پ", "ت", "ٹ", "ث", "ج", "چ", "ح", "خ",
           "س", "ش", "ص", "ض", "ط", "ظ", "ع", "غ", "ف", "ق", "ک", "گ", "ل", "م",
           "ن", "ہ", "ھ", "ی"]

non_joiners = ["ا", "آ", "د", "ڈ", "ذ", "ر", "ڑ", "ز", "ژ",
               "و","ؤ", "ۓ", "ں", "ے"]


reshaper = arabic_reshaper.ArabicReshaper(
        arabic_reshaper.config_for_true_type_font(
            'arial.ttf',
            arabic_reshaper.ENABLE_ALL_LIGATURES
        )
    )


###########################################################################

joined_words_list = []


def split(word):

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

    complete_word = ""

    for single_word in complete_urdu_word:

        complete_word = single_word + complete_word

        pass

    bidi_text = get_display(complete_word)
    temporary_text = reshaper.reshape(bidi_text)


    return temporary_text



#######################################################################



def generate_custom_image(text,font_size):




    font_size = int (font_size)
    title_font = ImageFont.truetype('arial.ttf',font_size)


    reshaped_text = reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)

    w, h = title_font.getsize(bidi_text)

    my_image = Image.new('RGB', (w+5, h+5), 'black')

    image_editable = ImageDraw.Draw(my_image)

    image_editable.multiline_text(((4) / 2, (0) / 2), bidi_text, font=title_font, fill='white', spacing=151,
                                  align='left')

    parameter, threshold_image = openCV.threshold(openCV.cvtColor(np.asarray(my_image),openCV.COLOR_RGB2GRAY,None), 100, 255, openCV.THRESH_BINARY, None)

    pass
    return np.asarray(my_image)
    #return threshold_image


#######################################################################


file1 = open('urdu_2.txt', 'r',encoding='utf-8-sig')
Lines = file1.readlines()

count = 0


array = Lines[0].split()


for word in array:

    split(word)

    pass

split_words_array = []


for index,word in enumerate(joined_words_list):


    if word != "" :

        split_words_array.append(word)

        pass


    pass

print(Lines)

print()

print(split_words_array)

split_words_array = list(dict.fromkeys(split_words_array))

print()
print(split_words_array)


complete_dataset = []

for number,value in enumerate(split_words_array):

    complete_dataset.append([value,number])

    pass

print(complete_dataset)

dataset_dataFrame = pd.DataFrame(np.array(complete_dataset))

print(dataset_dataFrame)

if os.path.isdir("sample_images"):
    pass
else:
    os.makedirs("sample_images")

dataset_dataFrame.to_csv("sample_images\\dataset.csv",index=False,encoding="utf-8-sig",index_label=None)

images_text_list = np.array(dataset_dataFrame)[:,0].tolist()

print("\n")

print(images_text_list)


images_list_1 = []
images_list_2 = []
images_list_3 = []
images_list_4 = []
images_list_5 = []



for text in images_text_list:

    text_image_1 = generate_custom_image(text=text, font_size=45)

    text_image_2 = generate_custom_image(text=text, font_size=50)

    text_image_3 = generate_custom_image(text=text, font_size=55)

    text_image_4 = generate_custom_image(text=text, font_size=60)

    text_image_5 = generate_custom_image(text=text, font_size=65)

    ########## appending lists

    images_list_1.append(text_image_1)

    images_list_2.append(text_image_2)

    images_list_3.append(text_image_3)

    images_list_4.append(text_image_4)

    images_list_5.append(text_image_5)



    pass

for i in range(len(images_list_1)):


    if os.path.isdir("sample_images\\urdu_dataset\\"+str(i)):
        pass
    else:
        os.makedirs("sample_images\\urdu_dataset\\"+str(i))

    image_1 = images_list_1[i]
    image_2 = images_list_2[i]
    image_3 = images_list_3[i]
    image_4 = images_list_4[i]
    image_5 = images_list_5[i]

    image_1 = openCV.resize(image_1, (200, 200), None)
    image_2 = openCV.resize(image_2, (200, 200), None)
    image_3 = openCV.resize(image_3, (200, 200), None)
    image_4 = openCV.resize(image_4, (200, 200), None)
    image_5 = openCV.resize(image_5, (200, 200), None)

    parameter, image_1 = openCV.threshold(image_1, 180, 255, openCV.THRESH_BINARY)
    parameter, image_2 = openCV.threshold(image_2, 180, 255, openCV.THRESH_BINARY)
    parameter, image_3 = openCV.threshold(image_3, 180, 255, openCV.THRESH_BINARY)
    parameter, image_4 = openCV.threshold(image_4, 180, 255, openCV.THRESH_BINARY)
    parameter, image_5 = openCV.threshold(image_5, 180, 255, openCV.THRESH_BINARY)


    openCV.imwrite("sample_images\\urdu_dataset\\" + str(i) + "\\" + str(i + 1 + 1 + 1) + ".png", image_1)
    openCV.imwrite("sample_images\\urdu_dataset\\" + str(i) + "\\" + str(i + 1 + 1 + 1 + 1) + ".png", image_1)
    openCV.imwrite("sample_images\\urdu_dataset\\" + str(i) + "\\" + str(i + 1 + 1 + 1 + 1 + 1) + ".png", image_2)
    openCV.imwrite("sample_images\\urdu_dataset\\" + str(i) + "\\" + str(i + 1 + 1 + 1 + 1 + 1 + 1) + ".png", image_3)
    openCV.imwrite("sample_images\\urdu_dataset\\" + str(i) + "\\" + str(i + 1 + 1 + 1 + 1 + 1 + 1 + 1) + ".png", image_4)
    openCV.imwrite("sample_images\\urdu_dataset\\" + str(i) + "\\" + str(i + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1) + ".png", image_5)

    pass

