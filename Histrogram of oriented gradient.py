import cv2 as opencv
from skimage.feature import hog
import numpy as np


image_path = 'upti\\extra\\96.png'


image = opencv.imread(image_path)




image = opencv.cvtColor(image, opencv.COLOR_RGB2GRAY, None, None)

# contour_image = draw_contours(image)

# openCV.imshow("images " + str(idx),image)

fd, hog_image = hog(image, orientations=9, block_norm='L2', pixels_per_cell=(12, 12),
                        cells_per_block=(2, 2), visualize=True, multichannel=False)

opencv.imshow("images label. " + str(len(fd)), np.concatenate((image,hog_image),axis=1))

image = np.pad(image,((20,0),(0,0)), constant_values=0)

opencv.imshow("image ", image)

hog_image = np.pad(hog_image,((20,0),(0,0)), constant_values=0)

opencv.imshow("hog_image ", hog_image)

opencv.waitKey(0)
opencv.destroyAllWindows()