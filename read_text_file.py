import arabic_reshaper
from bidi.algorithm import get_display
import numpy as np
import pandas as pd
from PIL import Image, ImageFont, ImageDraw
import cv2 as openCV
import os
from skimage.feature import hog

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



joined_words_list = []

def split(word):

    words_list = []

    urdu_word = []

    complete_urdu_word = []

    for word_idx,char in enumerate(word):

        #print()
        #print(word_idx," : ",char)
        #print()

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
                words_list.append(temporary_text)

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
            words_list.append(temporary_text)

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



def find_contours(image):

    new_image = image.copy()

    new_image[:, :, :] = 0

    image = openCV.cvtColor(image, openCV.COLOR_RGB2GRAY)

    parameter, threshold_image = openCV.threshold(image, 200, 250, openCV.THRESH_BINARY, None)

    for i in range(len(threshold_image[:, 0])):

        for j in range(len(threshold_image[i, :]) - 1):

            if threshold_image[i, j] - threshold_image[i, j + 1] != 0:
                new_image[i, j, :] = 255

                pass

            pass

        pass

    for j in range(len(threshold_image[0, :])):

        for i in range(len(threshold_image[:, j]) - 1):

            if threshold_image[i, j] - threshold_image[i + 1, j] != 0:
                new_image[i, j, :] = 255

                pass

            pass

        pass


    return new_image
    pass





file1 = open('urdu.txt', 'r',encoding='utf-8-sig')
Lines = file1.readlines()

count = 0

for line in Lines:
    count += 1
    print("Line{}: {}".format(count, line.strip()))


array = Lines[0].split()

for word in array :

    #print()
    #print(split(word))
    #print()

    split(word)
    pass

new_list = []

for index,word in enumerate(joined_words_list):

    #print()

    if word != "" :

        new_list.append(word)
        #print(index," : ",word)
        pass


    #print()

    pass

for line in Lines:
    count += 1
    print("Line{}: {}".format(count, line.strip()))

    pass


print(Lines[0].split())


print()

print(joined_words_list)
print()


final_list = list(dict.fromkeys(new_list))

print(final_list)
print()

print(np.array(final_list))

dataFrame = pd.DataFrame(np.array(final_list))

print()
print(dataFrame)

dataFrame.to_csv("urdu_words_list.csv",encoding='utf-8-sig',index = False)


image_list = []

sift = openCV.xfeatures2d.SIFT_create()


for text in final_list:

    image = generate_image(text)


    #image = find_contours(image)


    image_list.append(image)

    image = openCV.cvtColor(image,openCV.COLOR_RGB2GRAY)

    fd, hog_image = hog(image, orientations=4,block_norm='L2', pixels_per_cell=(8, 8),
                        cells_per_block=(2, 2), visualize=True, multichannel=False)

    print()
    print(hog_image.shape)
    print()
    #keypoints, descriptors = sift.detectAndCompute(image, None)

    #new_word_image = openCV.drawKeypoints(image, keypoints, None, color=(0, 255, 0), flags=0)

    image_list.append(hog_image)

    pass

if os.path.isdir("urdu_dataset"):
    pass
else:
    os.makedirs("urdu_dataset")

print(fd.size)
print()
print(fd)
print()


for idx,img in enumerate(image_list):

    openCV.imshow(""+str(idx),img)

    #openCV.imwrite("urdu_dataset\\"+str(idx)+".png",img)

    pass



data_file = open("urdu_words_list.csv", 'r',encoding='utf-8-sig')
data_list = data_file.readlines()
data_file.close()

print()
print(len(data_list))
print()

for i in range(len(data_list)):

    print()
    print(data_list[i].strip())
    print()

    pass

print()

string = ""

for ids in range(len(data_list)):

    print()
    print(ids," : ",data_list[ids])
    print()

    string = string + data_list[ids].strip()

    print()
    print(string)

    pass

openCV.waitKey(0)
openCV.destroyAllWindows()

