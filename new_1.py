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


my_image = Image.new('RGB', (90, 50), 'black')

title_text = characters[28] + characters[20] + characters[39]

label = title_text

reshaped_text = reshaper.reshape(title_text)
bidi_text = get_display(reshaped_text)

title_font = ImageFont.truetype('arial.ttf', 40)

w, h = title_font.getsize(bidi_text)

image_editable = ImageDraw.Draw(my_image)

image_editable.multiline_text(((90 - w) / 2, (50 - h) / 2), bidi_text, font=title_font, fill='white', spacing=151,
                              align='left')

openCV.imshow("new" , np.asarray(my_image))


openCV.waitKey(0)
openCV.destroyAllWindows()