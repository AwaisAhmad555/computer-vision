from PIL import Image, ImageFont, ImageDraw
import arabic_reshaper
from bidi.algorithm import get_display
import cv2 as openCV
import numpy as np
import os


def words_generation(index1,index2):

    reshaper = arabic_reshaper.ArabicReshaper(
        arabic_reshaper.config_for_true_type_font(
            'arial.ttf',
            arabic_reshaper.ENABLE_ALL_LIGATURES
        )
    )

    my_image = Image.new('RGB', (74, 50), 'black')

    first_characters = ["ب", "پ", "ت", "ٹ", "ث", "ج", "چ", "ح", "خ",
                        "س", "ش", "ص", "ض", "ط", "ظ", "ع", "غ", "ف", "ق", "ک", "گ", "ل", "م",
                        "ن", "ہ", "ھ", "ی"]

    characters = ["ا", "آ", "ب", "پ", "ت", "ٹ", "ث", "ج", "چ", "ح", "خ", "د", "ڈ", "ذ", "ر", "ڑ", "ز", "ژ",
                  "س", "ش", "ص", "ض", "ط", "ظ", "ع", "غ", "ف", "ق", "ک", "گ", "ل", "م",
                  "ن", "ں", "و", "ہ", "ھ", "ء", "ی", "ۓ"]

    #print(len(characters))

    #os.makedirs("urdu_bi-words_samples")

    temporary_name = reshaper.reshape(first_characters[index1])
    temporary_name = get_display(temporary_name)
    directory_name = temporary_name

    title_text = first_characters[index1] + characters[index2]

    #lable to be returned

    label = title_text

    reshaped_text = reshaper.reshape(title_text)
    bidi_text = get_display(reshaped_text)

    title_font = ImageFont.truetype('arial.ttf', 40)

    w, h = title_font.getsize(bidi_text)

    #print(w, h)

    image_editable = ImageDraw.Draw(my_image)

    image_editable.multiline_text(((74 - w) / 2, (50 - h) / 2), bidi_text, font=title_font, fill='white', spacing=151,
                                  align='left')

    # my_image.save("urdu_word_result.jpg")

    #my_image.show()

    #openCV.imshow("", np.asarray(my_image))

    #openCV.waitKey(0)
    #openCV.destroyAllWindows()

    return directory_name,label,np.asarray(my_image)

