from PIL import Image, ImageFont, ImageDraw
import arabic_reshaper
from bidi.algorithm import get_display
import cv2 as openCV
import numpy as np
import os

reshaper = arabic_reshaper.ArabicReshaper(
    arabic_reshaper.config_for_true_type_font(
        'arial.ttf',
        arabic_reshaper.ENABLE_ALL_LIGATURES
    )
)

characters = ["ا", "آ", "ب", "پ", "ت", "ٹ", "ث", "ج", "چ", "ح", "خ", "د", "ڈ", "ذ", "ر", "ڑ", "ز", "ژ",
              "س", "ش", "ص", "ض", "ط", "ظ", "ع", "غ", "ف", "ق", "ک", "گ", "ل", "م",
              "ن", "ں", "و", "ہ", "ھ", "ء", "ی", "ۓ"]

# os.makedirs("urdu_bi-words_samples")

for idx,char in enumerate(characters):

    my_image = Image.new('RGB', (64, 50), 'black')

    title_text = characters[idx]

    label = title_text

    reshaped_text = reshaper.reshape(title_text)
    bidi_text = get_display(reshaped_text)

    title_font = ImageFont.truetype('arial.ttf', 40)

    w, h = title_font.getsize(bidi_text)

    image_editable = ImageDraw.Draw(my_image)

    image_editable.multiline_text(((64 - w) / 2, (50 - h) / 2), bidi_text, font=title_font, fill='white', spacing=151,
                                  align='left')

    openCV.imshow(""+str(idx),np.asarray(my_image))

    directory = "urdu_chars_dataset\\"+str(bidi_text)

    if os.path.isdir(directory):
        pass
    else:
        os.makedirs("urdu_chars_dataset\\"+str(bidi_text))

    openCV.imwrite("urdu_chars_dataset\\"+str(bidi_text)+"\\"+str(bidi_text)+".jpg",np.asarray(my_image))

    my_image.save("urdu_chars_dataset\\"+str(bidi_text)+"\\"+str(bidi_text)+".jpg")
    pass


openCV.waitKey(0)
openCV.destroyAllWindows()