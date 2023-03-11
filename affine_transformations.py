import cv2 as opencv
import numpy as np

from skimage.feature import hog


image = opencv.imread("temporary\\segment_images\\61.png")

image = np.pad(image,((0,0),(5,5),(0,0)))

height = len(image[:, 0])
width = len(image[0, :])

# calculating center of image as rotation point for rotation then rotation matrix

image = opencv.resize(image,(200,200))
(center_X, center_Y) = (width // 2, height // 2)


rotation_matrix = opencv.getRotationMatrix2D((center_X, center_Y), angle=8, scale=1.0)
rotated_image = opencv.warpAffine(image, rotation_matrix, (width, height))

threshold_value, image = opencv.threshold(image, 200, 255, opencv.THRESH_BINARY)


opencv.imshow("image",image)

opencv.imshow("rotation",rotated_image)


threshold_value, image = opencv.threshold(image, 200, 255, opencv.THRESH_BINARY)

hog_features, test_hog_image = hog(image, orientations=9, block_norm='L2', pixels_per_cell=(16, 16),
                                        cells_per_block=(2, 2), visualize=True, multichannel=True)

opencv.imshow("hog",test_hog_image)


opencv.waitKey(0)
opencv.destroyAllWindows()