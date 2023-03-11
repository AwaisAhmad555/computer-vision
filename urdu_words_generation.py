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

#################images generation function####################

def generate_image(text):


    my_image = Image.new('RGB', (120, 50), 'black')

    title_font = ImageFont.truetype('arial.ttf', 40)


    reshaped_text = reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)

    w, h = title_font.getsize(bidi_text)

    # print(w, h)

    image_editable = ImageDraw.Draw(my_image)

    image_editable.multiline_text(((120 - w) / 2, (50 - h) / 2), bidi_text, font=title_font, fill='white', spacing=151,
                                  align='left')


    pass
    return np.asarray(my_image)



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




file1 = open('urdu.txt', 'r',encoding='utf-8-sig')
Lines = file1.readlines()

count = 0

for line in Lines:
    count += 1
    print("Line{}: {}".format(count, line.strip()))


array = Lines[0].split()

print()
print(array)


wordlist = []

for word in array:

    split(word)

    pass

print("words list : ")

print(joined_words_list)

new_list = []
for index,word in enumerate(joined_words_list):


    if word != "" :

        new_list.append(word)

        pass


    #print()

    pass

print()
print(new_list)


final_list = list(dict.fromkeys(new_list))

print()

print(final_list)

label_list = []

for idx,words in enumerate(final_list):

    label_list.append([idx,words])

    pass


print()

print(label_list)

dataframe = pd.DataFrame(label_list)

print()

print(dataframe)

dataframe.to_csv("new_urdu_words.csv",index=None,encoding="utf-8-sig",index_label=None)


output_dataFrame = pd.read_csv("new_urdu_words.csv",encoding="utf-8-sig",index_col=None)

print()

print("CSV data_frames : ")

print()

print(output_dataFrame)

print()

output_list = np.array(output_dataFrame)[:,1].tolist()

print(np.array(output_list))


###########################################################################



image_list = []

sift = openCV.xfeatures2d.SIFT_create()


for text in final_list:

    image = generate_image(text)


    image_list.append(image)

    image = openCV.cvtColor(image,openCV.COLOR_RGB2GRAY)

    fd, hog_image = hog(image, orientations=4,block_norm='L2', pixels_per_cell=(8, 8),
                        cells_per_block=(2, 2), visualize=True, multichannel=False)


    #image_list.append(hog_image)

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


    openCV.imshow("" + str(idx), np.hstack((img,thresh_image)))


    #openCV.imwrite("data_samples\\urdu_dataset\\" + str(idx) + ".png", img)
    #openCV.imwrite("data_samples\\sample_2\\"+str(idx)+".png",thresh_image)

    pass


openCV.waitKey(0)
openCV.destroyAllWindows()