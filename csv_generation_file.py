from PIL import Image, ImageFont, ImageDraw
import arabic_reshaper
from bidi.algorithm import get_display
import cv2 as openCV
import numpy as np
import os
import pandas as pd


characters = ["ا", "آ", "ب", "پ", "ت", "ٹ", "ث", "ج", "چ", "ح", "خ", "د", "ڈ", "ذ", "ر", "ڑ", "ز", "ژ",
                  "س", "ش", "ص", "ض", "ط", "ظ", "ع", "غ", "ف", "ق", "ک", "گ", "ل", "م",
                  "ن", "ں", "و", "ہ", "ھ", "ء", "ی", "ۓ"]


def trigram_words_generation(index1):

    reshaper = arabic_reshaper.ArabicReshaper(
        arabic_reshaper.config_for_true_type_font(
            'arial.ttf',
            arabic_reshaper.ENABLE_ALL_LIGATURES
        )
    )



    characters = ["ا", "آ", "ب", "پ", "ت", "ٹ", "ث", "ج", "چ", "ح", "خ", "د", "ڈ", "ذ", "ر", "ڑ", "ز", "ژ",
                  "س", "ش", "ص", "ض", "ط", "ظ", "ع", "غ", "ف", "ق", "ک", "گ", "ل", "م",
                  "ن", "ں", "و", "ہ", "ھ", "ء", "ی", "ۓ"]

    first_characters = ["ب", "پ", "ت", "ٹ", "ث", "ج", "چ", "ح", "خ",
                  "س", "ش", "ص", "ض", "ط", "ظ", "ع", "غ", "ف", "ق", "ک", "گ", "ل", "م",
                  "ن", "ہ", "ھ",  "ی"]

    temporary_name = reshaper.reshape(characters[index1])
    temporary_name = get_display(temporary_name)
    directory_name = temporary_name

    title_text = characters[index1]


    label = title_text

    reshaped_text = reshaper.reshape(title_text)
    bidi_text = get_display(reshaped_text)

    title_font = ImageFont.truetype('arial.ttf', 40)

    w, h = title_font.getsize(bidi_text)

    #print(w, h)

    my_image = Image.new('RGB', (w+40, h+15), 'black')

    image_editable = ImageDraw.Draw(my_image)

    image_editable.multiline_text(((40) / 2, (10) / 2), bidi_text, font=title_font, fill='white', spacing=151,
                                  align='left')


    #print(bidi_text)
    return directory_name,label,np.asarray(my_image)

print(len(characters))
#directory_name, label, word_image = trigram_words_generation(0)


sift = openCV.xfeatures2d.SIFT_create()

total_data_frame = pd.DataFrame([])

for idx in range(len(characters)):

    #print(idx," : ",characters[idx])
    directory_name, label, word_image = trigram_words_generation(idx)

    #print(idx, " : ", label)

    openCV.imshow(label, word_image)

    keypoints, descriptors = sift.detectAndCompute(word_image, None)

    new_word_image = openCV.drawKeypoints(word_image, keypoints, None, color=(0, 255, 0), flags=0)

    openCV.imshow(label + " 1 ", new_word_image)

    #print(idx, " : ", label, descriptors)

    if descriptors is not None:

        print()
        print(False)
        print()


        flatten_array = descriptors.reshape(-1)

        data_frame = pd.DataFrame([label] + flatten_array.tolist()).T

        total_data_frame = pd.concat([data_frame , total_data_frame])

        print(data_frame)

        pass

    pass


print(total_data_frame)

total_data_frame.to_csv("urdu_descriptors.csv",encoding='utf-8-sig')


#openCV.imshow(label,word_image)

openCV.waitKey(0)

openCV.destroyAllWindows()