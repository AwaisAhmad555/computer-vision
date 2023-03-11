import arabic_reshaper
import numpy as np
from bidi.algorithm import get_display
from PIL import Image, ImageFont, ImageDraw
import cv2 as openCV



reshaper = arabic_reshaper.ArabicReshaper(
        arabic_reshaper.config_for_true_type_font(
            'Jameel Noori Nastaleeq Regular.ttf',
            arabic_reshaper.ENABLE_ALL_LIGATURES
        )
    )



def generate_custom_image(text,font_size):



    font_size = int (font_size)
    title_font = ImageFont.truetype('Jameel Noori Nastaleeq Regular.ttf',font_size,encoding="utf-8-sig")


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






#######################################################################

sentence = "اس معاہدے"

image = generate_custom_image(sentence,40)

openCV.imshow("image",image)


openCV.waitKey(0)
openCV.destroyAllWindows()
