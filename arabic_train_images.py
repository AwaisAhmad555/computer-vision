import os
import arabic_reshaper
import numpy as np
from bidi.algorithm import get_display
from PIL import Image, ImageFont, ImageDraw
import cv2 as openCV
import pandas as pd




joiners = ["ب","ت","ث","ج","ح","خ","س","ش","ص","ض",
           "ط","ظ","ع","غ","ف","ق","ك","ل","م","ن",
           "ه","ي","ئ","ى"]


non_joiners = ["ا","د","ذ","ر","ز","و","ؤ","ء","ة","أ","إ"]


reshaper = arabic_reshaper.ArabicReshaper(
        arabic_reshaper.config_for_true_type_font(
            'arial.ttf',
            arabic_reshaper.ENABLE_ALL_LIGATURES
        )
    )


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
    return threshold_image



#############################################################


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




    return joined_words_list



#######################################################################


####################### Reading CSV file ##########################



output_dataFrame = pd.read_csv("dataset\\arabic_dataset_labels.csv",encoding="utf-8-sig",index_col=None)


last_index = len(np.array(output_dataFrame))

print()

print(output_dataFrame)

#################### Reading text from text file ####################
############### and appending list with arabic words ################

file1 = open('arabic_text_new.txt', 'r',encoding='utf-8-sig')
Lines = file1.readlines()

count = 0

print(Lines)

words_list = []

for i in range(len(Lines)-0):

    array = Lines[i].split()

    # splitting text words to non joined words

    wordlist = []




    for word in array:

        for sub_word in split(word):


            words_list.append(sub_word)


            pass


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


print(new_list)

print()


final_list = list(dict.fromkeys(new_list))

output_list = []

for idx,words in enumerate(final_list):

    output_list.append([words,last_index + idx])

    pass



#######################################################################


print()

# joining the new words from text file with words already existed
# dataset csv file to re-create dataset csv file


total_array = np.concatenate((np.array(output_dataFrame),output_list))


print(pd.DataFrame(total_array))

# Accessing column 0 of total array data_frame to prune
# repeating words

new_array = list(dict.fromkeys(total_array[:,0].tolist()))


print(new_array)

# appending new list with unique word after pruning repeating words
# in new_array

new_final_list = []


for number,value in enumerate(new_array):

    new_final_list.append([value,number])

    pass

print(np.array(new_final_list))


final_dataFrame = pd.DataFrame(np.array(new_final_list))

print()

print(final_dataFrame)



final_dataFrame.to_csv("dataset\\arabic_dataset_labels.csv",index=False,encoding="utf-8-sig",index_label=None)

# variable $new_array holds all text words to be rendered in images
image_text_list = new_array


###########################################################

image_list = []

for text in image_text_list:


    #generating sample 1 with large font size


    #generating sample 2 with smaller font size


    ########## samples generation /- augmentation

    text_image = generate_custom_image(text=text, font_size=52)

    image_list.append(text_image)

    pass




if os.path.isdir("dataset\\arabic_dataset"):
    pass
else:
    os.makedirs("dataset\\arabic_dataset")



for i in range(len(image_list)-0):

    if os.path.isdir("dataset\\arabic_dataset\\"+str(i)):
        pass
    else:
        os.makedirs("dataset\\arabic_dataset\\"+str(i))

    word_image = image_list[i]

    parameter, word_image = openCV.threshold(word_image, 180, 255, openCV.THRESH_BINARY)

    openCV.imwrite("dataset\\arabic_dataset\\" + str(i) + "\\" + str(i + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1) + ".png", word_image)


    pass



