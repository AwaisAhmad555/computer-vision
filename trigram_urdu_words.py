from PIL import Image, ImageFont, ImageDraw
import arabic_reshaper
from bidi.algorithm import get_display
import cv2 as openCV
import numpy as np
import os


def trigram_words_generation(index1,index2,index3):

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

    #print(len(characters))

    #os.makedirs("urdu_bi-words_samples")

    temporary_name = reshaper.reshape(first_characters[index1])
    temporary_name = get_display(temporary_name)
    directory_name = temporary_name

    title_text = first_characters[index1] + first_characters[index2] + characters[index3]

    #lable to be returned

    label = title_text

    reshaped_text = reshaper.reshape(title_text)
    bidi_text = get_display(reshaped_text)

    title_font = ImageFont.truetype('arial.ttf', 40)

    w, h = title_font.getsize(bidi_text)

    #print(w, h)

    image_editable = ImageDraw.Draw(my_image)

    image_editable.multiline_text(((120 - w) / 2, (50 - h) / 2), bidi_text, font=title_font, fill='white', spacing=151,
                                  align='left')

    # my_image.save("urdu_word_result.jpg")

    #my_image.show()

    #openCV.imshow("", np.asarray(my_image))

    #openCV.waitKey(0)
    #openCV.destroyAllWindows()

    return directory_name,label,np.asarray(my_image)


img_list = []
label_list = []
directory_list = []

for i in range(0,27):

    for j in range(0,27):

        for k in range(0,40):
            directory_name, label, image = trigram_words_generation(i, j, k)

            img_list.append(image)
            directory_list.append(directory_name)
            label_list.append(label)


            pass


        pass


    pass


for idx,image in enumerate(img_list):

    print(str(idx)+" <----> "+label_list[idx])

    my_image = Image.fromarray(image)

    my_image.save("urdu_chars_dataset\\" + str(directory_list[idx]) + "\\" + str(label_list[idx]) + ".jpg")

    pass


