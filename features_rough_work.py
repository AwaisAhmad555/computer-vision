import numpy as np
import pandas as pd
import cv2 as openCV
import math
from scipy.spatial.distance import cdist, cosine
from scipy.optimize import linear_sum_assignment
import matplotlib.pyplot as plt
import arabic_reshaper
from bidi.algorithm import get_display
from PIL import Image, ImageFont, ImageDraw
import os


reshaper = arabic_reshaper.ArabicReshaper(
        arabic_reshaper.config_for_true_type_font(
            'arial.ttf',
            arabic_reshaper.ENABLE_ALL_LIGATURES
        )
    )



def generate_custom_image(text,font_size):



    font_size = int (font_size)
    title_font = ImageFont.truetype('arial.ttf',font_size)


    reshaped_text = reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)

    w, h = title_font.getsize(bidi_text)

    #my_image = Image.new('RGB', (w+5, h+5), 'white')

    width = 1060
    height = 70

    my_image = Image.new('RGB', (width, height), 'white')

    image_editable = ImageDraw.Draw(my_image)

    image_editable.multiline_text(((height) / 2, (0) / 2), bidi_text, font=title_font, fill='black', spacing=151,
                                  align='center')

    parameter, threshold_image = openCV.threshold(openCV.cvtColor(np.asarray(my_image),openCV.COLOR_RGB2GRAY,None), 200, 255, openCV.THRESH_BINARY, None)

    pass
    return openCV.cvtColor(np.asarray(my_image),openCV.COLOR_RGB2GRAY,None)


file1 = open('paragraph.txt', 'r',encoding='utf-8-sig')
Lines = file1.readlines()


image_list = []



###########################################################################

path = "training_text_images"


folder_index = len(os.listdir(path))


full_path = os.path.join(path,str(folder_index))


if os.path.isdir(full_path):

    pass

else:

    os.makedirs(full_path)


    pass

print(full_path)

f = open(full_path+"\\text_output.txt", "w",encoding="utf-8-sig")



for idx,line in enumerate(Lines):

    image = generate_custom_image(line, font_size=50)

    #openCV.imshow("img" + str(idx), image)

    #print(line)

    image_list.append(image)

    f.write(line)

    pass


f.close()


print()

#print(Lines)




complete_image = np.vstack(image_list)

openCV.imshow("complete image",complete_image)

openCV.imwrite(full_path+"\\"+ str (folder_index)+ ".png",complete_image)



"""complete_image = np.array([])

for i in range(len(image_list)-1):

    complete_image = np.vstack((image_list[i],image_list[i+1]))

    pass"""


openCV.waitKey(0)
openCV.destroyAllWindows()