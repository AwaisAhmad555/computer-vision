import arabic_reshaper
from bidi.algorithm import get_display
import os
import numpy as np
import pandas as pd
from PIL import Image, ImageFont, ImageDraw
import cv2 as openCV
from skimage.feature import hog
from sklearn.neighbors import KNeighborsClassifier



joiners = ["ب", "پ", "ت", "ٹ", "ث", "ج", "چ", "ح", "خ",
           "س", "ش", "ص", "ض", "ط", "ظ", "ع", "غ", "ف", "ق", "ک", "گ", "ل", "م",
           "ن", "ہ", "ھ", "ی"]


non_joiners = ["ا", "آ", "د", "ڈ", "ذ", "ر", "ڑ", "ز", "ژ",
               "و", "ۓ", "ں", "ے"]


reshaper = arabic_reshaper.ArabicReshaper(
        arabic_reshaper.config_for_true_type_font(
            'arial.ttf',
            arabic_reshaper.ENABLE_ALL_LIGATURES
        )
    )




def generate_image(text):


    my_image = Image.new('RGB', (120, 50), 'black')

    title_font = ImageFont.truetype('arial.ttf', 40)


    reshaped_text = reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)

    w, h = title_font.getsize(bidi_text)

    image_editable = ImageDraw.Draw(my_image)

    image_editable.multiline_text(((120 - w) / 2, (50 - h) / 2), bidi_text, font=title_font, fill='white', spacing=151,
                                  align='left')


    pass
    return np.asarray(my_image)



###########################################################################

def generate_sample_2(text):


    my_image = Image.new('RGB', (120, 50), 'black')

    title_font = ImageFont.truetype('arial.ttf', 20)


    reshaped_text = reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)

    w, h = title_font.getsize(bidi_text)

    # print(w, h)

    image_editable = ImageDraw.Draw(my_image)

    image_editable.multiline_text(((120 - w) / 2, (50 - h) / 2), bidi_text, font=title_font, fill='white', spacing=151,
                                  align='left')


    pass
    return np.asarray(my_image)



#############################################################################



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





file1 = open('urdu_2.txt', 'r',encoding='utf-8-sig')
Lines = file1.readlines()

count = 0




array = Lines[0].split()



wordlist = []

for word in array:

    split(word)

    pass


new_list = []

for index,word in enumerate(joined_words_list):


    if word != "" :

        new_list.append(word)

        pass


    pass



final_list = list(dict.fromkeys(new_list))


label_list = []


#csv file output dataframe
output_dataFrame = pd.read_csv("new_urdu_words_1.csv",encoding="utf-8-sig",index_col=None)

csv_array = np.array(output_dataFrame)[:,1]


last_index = len(np.array(output_dataFrame))

for idx,words in enumerate(final_list):

    label_list.append([len(np.array(output_dataFrame))+idx,words])

    pass



dataframe = pd.DataFrame(label_list)


image_text_list = np.array(output_dataFrame)[:,0].tolist()

#csv file output dataframe
output_array = np.fliplr(np.array(output_dataFrame))
label_array = np.array(label_list)

print("csv file output : ")
print(output_array)

print("Notepad text : ")
print(label_array)

total_array = np.concatenate((output_array,label_array))

print(total_array)


new_array = list(dict.fromkeys(total_array[:,1].tolist()))

print()

print(new_array)

new_final_list = []

for number,value in enumerate(new_array):

    new_final_list.append([value,number])

    pass

print(np.array(new_final_list))


final_dataFrame = pd.DataFrame(np.array(new_final_list))


#saving label in csv file

final_dataFrame.to_csv("new_urdu_words_1.csv",index=False,encoding="utf-8-sig",index_label=None)





output_list = np.array(output_dataFrame)[:,1].tolist()



###########################################################################




image_list = []
list_sample_3 = []

sift = openCV.xfeatures2d.SIFT_create()


for text in image_text_list:


    #generating sample 1 with large font size
    image = generate_image(text)

    #generating sample 2 with smaller font size

    small_font_image = generate_sample_2(text)


    image_list.append(image)

    list_sample_3.append(small_font_image)

    pass



if os.path.isdir("sample_2"):
    pass
else:
    os.makedirs("sample_2")


if os.path.isdir("data_samples\\urdu_dataset"):
    pass
else:
    os.makedirs("data_samples\\urdu_dataset")


if os.path.isdir("data_samples\\sample_2"):
    pass
else:
    os.makedirs("data_samples\\sample_2")


if os.path.isdir("data_samples\\sample_3"):
    pass
else:
    os.makedirs("data_samples\\sample_3")


for idx,img in enumerate(image_list):




    #img_blur = openCV.GaussianBlur(img,(1,1),openCV.BORDER_ISOLATED)

    parameter , thresh_image = openCV.threshold(img,150,250,openCV.THRESH_BINARY,None)


    #openCV.imshow("" + str(last_index+idx), np.hstack((img,thresh_image)))


    openCV.imwrite("data_samples\\urdu_dataset\\" + str(idx) + ".png", img)
    openCV.imwrite("data_samples\\sample_2\\"+str(idx)+".png",thresh_image)

    pass



#############################################################################


for idx,img_1 in enumerate(list_sample_3):



    #img_blur = openCV.GaussianBlur(img,(1,1),openCV.BORDER_ISOLATED)

    parameter , thresh_image = openCV.threshold(img_1,150,250,openCV.THRESH_BINARY,None)


    #openCV.imshow("" + str(idx), np.hstack((img_1,thresh_image)))


    openCV.imwrite("data_samples\\sample_3\\" + str(idx) + ".png", img_1)

    pass




openCV.waitKey(0)
openCV.destroyAllWindows()