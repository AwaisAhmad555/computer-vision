from PIL import Image, ImageFont, ImageDraw

from matplotlib import pyplot as plt
import numpy as np
import cv2

text_string = u'تصوير'

img = Image.new('RGB', (200, 150))
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('Jameel Noori Nastaleeq.ttf', 50)

draw.text((25,40), text_string, fill='white', font=font)

img.show()