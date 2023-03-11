import cv2 as openCV

import numpy as np

from skimage import exposure

from skimage.feature import hog


orignal_image = openCV.imread("test.png")


openCV.imshow("1",orignal_image)


features, hog_image = hog(orignal_image, orientations=1, pixels_per_cell=(8, 8),
                    cells_per_block=(2, 2), visualize=True, multichannel=True)

openCV.imshow("a",hog_image)

hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10))

openCV.imshow("rescaled_intensity_image",hog_image_rescaled)
print(len(features))

print(np.expand_dims(features,axis=1).tolist())

openCV.waitKey(0)
openCV.destroyAllWindows()
