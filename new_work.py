from PIL import Image, ImageFont, ImageDraw
import arabic_reshaper
from bidi.algorithm import get_display
import cv2 as openCV
import numpy as np
import os
import pandas as pd


def trigram_words_generation(index1):

    reshaper = arabic_reshaper.ArabicReshaper(
        arabic_reshaper.config_for_true_type_font(
            'arial.ttf',
            arabic_reshaper.ENABLE_ALL_LIGATURES
        )
    )

    my_image = Image.new('RGB', (120, 50), 'black')

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

    image_editable = ImageDraw.Draw(my_image)

    image_editable.multiline_text(((120 - w) / 2, (50 - h) / 2), bidi_text, font=title_font, fill='white', spacing=151,
                                  align='left')


    print(bidi_text)
    return directory_name,label,np.asarray(my_image)



directory_name, label, word_image = trigram_words_generation(23)

openCV.imshow(label,word_image)

#openCV.imwrite("single_sample.jpg",word_image)

#parameter, threshold_image = openCV.threshold(word_image,200,255,openCV.THRESH_BINARY)

#openCV.imshow("8",threshold_image)

sift = openCV.xfeatures2d.SIFT_create()

keypoints, descriptors = sift.detectAndCompute(word_image, None)


new_word_image = openCV.drawKeypoints(word_image, keypoints, None, color=(0, 255, 0), flags=0)

openCV.imshow(label+" 1 ",new_word_image)

print(descriptors)

print()

print(descriptors.shape)

print()

flatten_array = descriptors.reshape(-1)

data_frame = pd.DataFrame([label] + flatten_array.tolist()).T

print(data_frame)
data_frame.to_csv("descriptor.csv",encoding='utf-8-sig')

print()

print(flatten_array)

print()

print(flatten_array.shape)

new_shape = flatten_array.reshape(11,128)

print()

print(new_shape.shape)

print()

print(new_shape)

openCV.waitKey(0)
openCV.destroyAllWindows()
