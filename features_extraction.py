import cv2 as opencv
from scipy.ndimage import label
import numpy as np
from math import copysign, log10

from skimage.feature import hog


##################################### custom features #########################

def f_get_holes(word):

    contours, _ = opencv.findContours(word, opencv.RETR_LIST, opencv.CHAIN_APPROX_SIMPLE)

    _, n = label(word)

    return max(0, len(contours) - n)

def f_get_dots(word):

    contours, _ = opencv.findContours(word, opencv.RETR_EXTERNAL, opencv.CHAIN_APPROX_NONE)

    count = 0

    for contour in contours:
        contour = np.unique(contour, axis=0)

        if (contour.shape[0] < 4):
            count += 1

        elif (contour.shape[0] < 6):
            count += 2

        elif (contour.shape[0] < 7):
            count += 3

    return count


def whiteBlackRatio(img):
    h = img.shape[0]
    w = img.shape[1]
    # initialized at 1 to avoid division by zero
    blackCount = 1
    whiteCount = 0
    for y in range(0, h):
        for x in range(0, w):
            if (img[y, x] == 0):
                blackCount += 1
            else:
                whiteCount += 1
    return whiteCount / blackCount



def horizontalTransitions(img):
    h = img.shape[0]
    w = img.shape[1]
    maximum = 0
    for y in range(0, h):
        prev = img[y, 0]
        transitions = 0
        for x in range(1, w):
            if (img[y, x] != prev):
                transitions += 1
                prev = img[y, x]
        maximum = max(maximum, transitions)

    return maximum


def verticalTransitions(img):
    h = img.shape[0]
    w = img.shape[1]
    maximum = 0
    for x in range(0, w):
        prev = img[0, x]
        transitions = 0
        for y in range(1, h):
            if (img[y, x] != prev):
                transitions += 1
                prev = img[y, x]
        maximum = max(maximum, transitions)

    return maximum

"""def f_horizontal_transitions(img):
    count = 0
    for i in range(img.shape[0]):
        prev = img[i, 0]
        for j in range(img.shape[1]):
            if img[i, j] != prev:
                prev = img[i, j]
                count += 1
    return count


def f_vertical_transitions(img):
    count = 0
    for i in range(img.shape[1]):
        prev = img[0, i]
        for j in range(img.shape[0]):
            if img[j, i] != prev:
                prev = img[j, i]
                count += 1
    return count"""



def cut_extra_height(img):
    histo = np.sum(img, axis=1)
    count = 0
    count1 = 0
    for i in range(len(histo)):
        if histo[i] == 0:
            count += 1
        else:
            break

    for i in range(len(histo) - 1, 0, -1):
        if histo[i] == 0:
            count1 += 1
        else:
            break

    return img[count: img.shape[0] - count1, :]


def cut_extra_width(img):
    histo = np.sum(img, axis=0)

    count = 0
    count1 = 0

    for i in range(len(histo)):
        if histo[i] == 0:
            count += 1
        else:
            break

    for i in range(len(histo) - 1, 0, -1):
        if histo[i] == 0:
            count1 += 1
        else:
            break

    return img[: , count: img.shape[1] - count1]



def width_over_height(img):
    new = cut_extra_height(img)
    return new.shape[1] / new.shape[0]

def height_over_width(img):
    new = cut_extra_height(img)
    return new.shape[0] / new.shape[1]

def histogramAndCenterOfMass(img):
    h = img.shape[0]
    w = img.shape[1]
    histogram = []
    sumX = 0
    sumY = 0
    num = 0
    for x in range(0, w):
        localHist = 0
        for y in range(0, h):
            if (img[y, x] == 0):
                sumX += x
                sumY += y
                num += 1
                localHist += 1
        histogram.append(localHist)

    return sumX / num, sumY / num, histogram


def blackPixelsCount(img):
    blackCount = 1  # initialized at 1 to avoid division by zero when we calculate the ratios
    h = img.shape[0]
    w = img.shape[1]
    for y in range(0, h):
        for x in range(0, w):
            if (img[y, x] == 0):
                blackCount += 1

    return blackCount



######## Yamina paper########
#############################


def f_bw_pr(char):
    w, h = char.shape
    # region 1
    upperLeft = char[0: w // 2, 0: h // 2]
    # region 2
    upperRight = char[w // 2: w, 0: h // 2]
    # region 3
    lowerLeft = char[0: w // 2, h // 2: h]
    # region 4
    lowerRight = char[w // 2: w, h // 2: h]

    b1w1 = len(np.nonzero(upperLeft)[0]) / (upperLeft.size - len(np.nonzero(upperLeft)))
    b2w2 = len(np.nonzero(upperRight)[0]) / (upperRight.size - len(np.nonzero(upperRight)))
    b3w3 = len(np.nonzero(lowerLeft)[0]) / (lowerLeft.size - len(np.nonzero(lowerLeft)))
    b4w4 = len(np.nonzero(lowerRight)[0]) / (lowerRight.size - len(np.nonzero(lowerRight)))
    b1w2 = len(np.nonzero(upperLeft)[0]) / (len(np.nonzero(upperRight)))
    b3w4 = len(np.nonzero(lowerLeft)[0]) / (len(np.nonzero(lowerRight)))
    b1w3 = len(np.nonzero(upperLeft)[0]) / (len(np.nonzero(lowerLeft)))
    b2w4 = len(np.nonzero(upperRight)[0]) / (len(np.nonzero(lowerRight)))
    b1w4 = len(np.nonzero(upperLeft)[0]) / (len(np.nonzero(lowerRight)))
    b2w3 = len(np.nonzero(upperRight)[0]) / (len(np.nonzero(lowerLeft)))
    return [b1w1, b2w2, b3w3, b4w4, b1w2, b3w4, b1w3, b2w4, b1w4, b2w3]


def sum_histogram_function(image):

    image = opencv.resize(image,(500,500),None)

    thresh, image = opencv.threshold(image,200,255,opencv.THRESH_BINARY,None)

    image = image / 255

    histogram_sum = np.sum(image, axis=1)

    histogram_sum = list(histogram_sum)

    """for i in range(len(histogram_sum)):

        histogram_sum[i] = int (histogram_sum[i])

        pass"""

    return histogram_sum
    pass

def hog_features(image):

    image = np.pad(image,((2,2),(0,0)),constant_values=0)

    image = opencv.resize(image,(100,100),None)

    #image = opencv.cvtColor(image, opencv.COLOR_RGB2GRAY, None, None)

    threshold_value, image = opencv.threshold(image, 200, 255, opencv.THRESH_BINARY)

    hog_features, test_hog_image = hog(image, orientations=9, block_norm='L2', pixels_per_cell=(16, 16),
                                        cells_per_block=(2, 2), visualize=True, multichannel=False)


    return hog_features
    pass


def get_features(img):

    y, x = img.shape

    features_list = []

    crop_image = img

    """holes_features = f_get_holes(img)

    features_list.append(holes_features)

    black_to_white_ratio = whiteBlackRatio(img=crop_image)

    features_list.append(black_to_white_ratio)

    horizontalTransition = horizontalTransitions(img=img)
    verticalTransition = verticalTransitions(img=img)



    features_list.append(horizontalTransition)
    features_list.append(verticalTransition)

    #width_to_height_ratio = width_over_height(crop_image)

    #features_list.append(width_to_height_ratio)

    xCenter, yCenter, xHistogram = histogramAndCenterOfMass(crop_image)

    #average_histogram_sum = np.sum(xHistogram, axis=0) / len(xHistogram)

    features_list.append(xCenter)
    features_list.append(yCenter)
    #features_list.append(average_histogram_sum)"""

    #crop_image = np.pad(img, ((2, 2), (0, 0)), constant_values=0)

    #crop_image = opencv.resize(crop_image,(100,100),None)



    ################# calculating Hu moments features

    moments = opencv.moments(img)

    hu_moments = opencv.HuMoments(moments)

    ################# Applying log transformation to moments features


    for i in range(len(hu_moments)):

        hu_moments[i] = -1 * copysign(1.0, hu_moments[i]) * log10(abs(hu_moments[i]))

        pass

    #converting array to list

    hu_moments = hu_moments.reshape(-1).tolist()


    for single_hu_moment in hu_moments:

        #features_list.append(abs(single_hu_moment))
        #features_list.append(single_hu_moment)

        pass

    HOG_features = hog_features(image=img)


    for feature in HOG_features:

        features_list.append(feature)

        pass


    horizontalTransition = horizontalTransitions(img=img)
    verticalTransition = verticalTransitions(img=img)

    features_list.append(horizontalTransition)
    features_list.append(verticalTransition)

    black_to_white_ratio = whiteBlackRatio(img=crop_image)

    features_list.append(black_to_white_ratio)

    # splitting the image into 4 images
    topLeft = crop_image[0:y // 2, 0:x // 2]
    topRight = crop_image[0:y // 2, x // 2:x]
    bottomeLeft = crop_image[y // 2:y, 0:x // 2]
    bottomRight = crop_image[y // 2:y, x // 2:x]

    # get white to black ratio in each quarter
    features_list.append(whiteBlackRatio(topLeft))
    features_list.append(whiteBlackRatio(topRight))
    features_list.append(whiteBlackRatio(bottomeLeft))
    features_list.append(whiteBlackRatio(bottomRight))

    # the next 6 features are:
    # • Black Pixels in Region 1/ Black Pixels in Region 2.
    # • Black Pixels in Region 3/ Black Pixels in Region 4.
    # • Black Pixels in Region 1/ Black Pixels in Region 3.
    # • Black Pixels in Region 2/ Black Pixels in Region 4.
    # • Black Pixels in Region 1/ Black Pixels in Region 4
    # • Black Pixels in Region 2/ Black Pixels in Region 3.
    topLeftCount = blackPixelsCount(topLeft)
    topRightCount = blackPixelsCount(topRight)
    bottomLeftCount = blackPixelsCount(bottomeLeft)
    bottomRightCount = blackPixelsCount(bottomRight)

    features_list.append(topLeftCount / topRightCount)
    features_list.append(bottomLeftCount / bottomRightCount)
    features_list.append(topLeftCount / bottomLeftCount)
    features_list.append(topRightCount / bottomRightCount)
    features_list.append(topLeftCount / bottomRightCount)
    features_list.append(topRightCount / bottomLeftCount)

    holes_features = f_get_holes(img)

    features_list.append(holes_features)


    pass

    return features_list
