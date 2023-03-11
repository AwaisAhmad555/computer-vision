import pickle
import numpy as np

sift_features_list = pickle.load(open("dataset\\training_samples_SIFT_Features.pkl","rb"))

print(len(sift_features_list))

print(len(sift_features_list[2]))
sorted_sift_features_list = sorted(sift_features_list, key= lambda x : len(x))

print("\n")

for x in sorted_sift_features_list:

    print()
    print(len(x))

    pass
"""
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
#from preprocessing import binary_otsus, deskew
#from utilities import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import glob
import os
import os.path
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
import warnings


# %matplotlib inline
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


def blackPixelsCount(img):
    blackCount = 1  # initialized at 1 to avoid division by zero when we calculate the ratios
    h = img.shape[0]
    w = img.shape[1]
    for y in range(0, h):
        for x in range(0, w):
            if (img[y, x] == 0):
                blackCount += 1

    return blackCount


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


def getFeatures(img):
    x, y = img.shape
    featuresList = []
    # first feature: height/width ratio
    featuresList.append(y / x)
    # second feature is ratio between black and white count pixels
    featuresList.append(whiteBlackRatio(img))
    # third and fourth features are the number of vertical and horizontal transitions
    featuresList.append(horizontalTransitions(img))
    featuresList.append(verticalTransitions(img))

    # print (featuresList)
    # splitting the image into 4 images
    topLeft = img[0:y // 2, 0:x // 2]
    topRight = img[0:y // 2, x // 2:x]
    bottomeLeft = img[y // 2:y, 0:x // 2]
    bottomRight = img[y // 2:y, x // 2:x]

    # get white to black ratio in each quarter
    featuresList.append(whiteBlackRatio(topLeft))
    featuresList.append(whiteBlackRatio(topRight))
    featuresList.append(whiteBlackRatio(bottomeLeft))
    featuresList.append(whiteBlackRatio(bottomRight))

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

    featuresList.append(topLeftCount / topRightCount)
    featuresList.append(bottomLeftCount / bottomRightCount)
    featuresList.append(topLeftCount / bottomLeftCount)
    featuresList.append(topRightCount / bottomRightCount)
    featuresList.append(topLeftCount / bottomRightCount)
    featuresList.append(topRightCount / bottomLeftCount)
    # get center of mass and horizontal histogram
    xCenter, yCenter, xHistogram = histogramAndCenterOfMass(img)
    featuresList.append(xCenter)
    featuresList.append(yCenter)
    # featuresList.extend(xHistogram)
    # print(len(featuresList))
    return featuresList


def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]


def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles


def trainAndClassify(data, classes):
    X_train, X_test, y_train, y_test = train_test_split(data, classes, test_size=0.20)
    svclassifier = SVC(kernel='rbf', gamma=0.005, C=1000)
    svclassifier.fit(X_train, y_train)
    y_pred = svclassifier.predict(X_test)
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))


def removeMargins(img):
    th, threshed = cv.threshold(img, 245, 255, cv.THRESH_BINARY_INV)
    ## (2) Morph-op to remove noise
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (11, 11))
    morphed = cv.morphologyEx(threshed, cv.MORPH_CLOSE, kernel)
    ## (3) Find the max-area contour
    cnts = cv.findContours(morphed, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[-2]
    cnt = sorted(cnts, key=cv.contourArea)[-1]
    ## (4) Crop and save it
    x, y, w, h = cv.boundingRect(cnt)
    dst = img[y:y + h, x:x + w]
    return dst


def optimizedGetFeatures(img):
    x, y = img.shape
    featuresList = []


def main():
    data = np.array([])
    classes = np.array([])
    directory = '../LettersDataset'
    chars = get_immediate_subdirectories(directory)
    count = 0
    numOfFeatures = 16
    charPositions = ['Beginning', 'End', 'Isolated', 'Middle']
    for char in chars:
        for position in charPositions:
            if (os.path.isdir(directory + '/' + char + '/' + position) == True):
                listOfFiles = getListOfFiles(directory + '/' + char + '/' + position)
                for filename in listOfFiles:
                    img = cv.imread(filename)
                    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
                    cropped = removeMargins(gray_img)
                    #binary_img = binary_otsus(cropped, 0)
                    #features = getFeatures(binary_img)
                    #data = np.append(data, features)
                    classes = np.append(classes, char + position)
                    count += 1

    data = np.reshape(data, (count, numOfFeatures))
    trainAndClassify(data, classes)


main()

#################################################################################


import cv2
import numpy as np
from scipy.ndimage import label
from scipy.signal import convolve2d
import matplotlib.pyplot as plt
#from utility import vertical_histogram, horizontal_histogram


# =================== #
# Structural features #
# =================== #


def f_get_holes(word):
    contours, _ = cv2.findContours(
        word, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    _, n = label(word)
    return max(0, len(contours) - n)


def f_get_dots(word):
    contours, _ = cv2.findContours(
        word, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
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


def f_strokes_count(word):
    pass


def f_width():
    pass


def f_height():
    pass


def f_max_y():
    pass


def f_min_y():
    pass


# ====================== #
# Global transformations #
# ====================== #

# works with grayscale images only
# a boolean parameter indicates whether the image is in grayscale or binarized
# word images should be of fixed size (28x20) in the paper

def get_circular_lbp(word, nbins, is_binarized=False):
    if is_binarized:
        # This filter transforms a binarized image into a gray scal one
        filter = np.array([[0.1, 0.1, 0.1], [0.1, 0.2, 0.1], [0.1, 0.1, 0.1]])
        word = np.array(convolve2d(word * 255, filter)).astype(int)

    word = np.array(word)
    lbps = []
    powers_of_2 = np.array([1, 2, 4, 8, 16, 32, 64, 128])
    for i in range(1, word.shape[0] - 1):
        for j in range(1, word.shape[1] - 1):
            roi = word.copy()[i - 1: i + 2, j - 1: j + 2]
            roi[roi <= roi[1, 1]] = 0
            roi[roi > roi[1, 1]] = 1
            value = roi[1, 0] * powers_of_2[7] + roi[2, 0] * powers_of_2[6] + \
                    roi[2, 1] * powers_of_2[5] + \
                    roi[2, 2] * powers_of_2[4] + roi[1, 2] * powers_of_2[3] + roi[0, 2] * \
                    powers_of_2[2] + roi[0, 1] * powers_of_2[1] + \
                    roi[0, 0] * powers_of_2[0]
            lbps.append(value)

    # Get a histogram of 59 bins
    lbps = np.array(lbps)
    hist, _ = np.histogram(lbps, bins=nbins)
    return hist


def f_multi_lbp(word, is_binarized=False, nbins=10):
    # get full word image lbp
    fullWordHist = get_circular_lbp(word, nbins, is_binarized)
    # compute lbp for 4 quarters of the image
    w, h = word.shape
    upperLeft = word[0: w // 2, 0: h // 2]
    upperRight = word[w // 2: w, 0: h // 2]
    lowerLeft = word[0: w // 2, h // 2: h]
    lowerRight = word[w // 2: w, h // 2: h]

    upperLeftHist = get_circular_lbp(upperLeft, nbins, is_binarized)
    upperRighttHist = get_circular_lbp(upperRight, nbins, is_binarized)
    lowerLeftHist = get_circular_lbp(lowerLeft, nbins, is_binarized)
    lowerRightHist = get_circular_lbp(lowerRight, nbins, is_binarized)
    # Return a feature vector of 295 dimensions
    return np.concatenate((fullWordHist, upperLeftHist, upperRighttHist, lowerLeftHist, lowerRightHist))


# assumes the input img is binarized
def f_ft(img):
    filter = np.array([[0.1, 0.1, 0.1], [0.1, 0.2, 0.1], [0.1, 0.1, 0.1]])
    word = np.array(convolve2d(img * 255, filter)).astype(int)
    ft = np.fft.fft2(word)
    ft = np.fft.fftshift(ft)
    h, w = ft.shape
    w = w // 2
    h = h // 2
    ft = ft[h - 2: h + 2, w - 2: w + 2]
    h, w = ft.shape
    ft = np.reshape(ft, (h * w,))
    # To reconstruct the signal:
    # ift = np.fft.ifft2(ft).real
    return ft


def f_center_of_mass(char):
    #vh = vertical_histogram(char)
    columns = range(1, char.shape[1] + 1)
    #cm = vh * columns

    #hh = horizontal_histogram(char)
    rows = range(1, char.shape[0] + 1)
    #rm = hh * rows

    return
    #return int(np.sum(cm) // np.sum(vh)), int(np.sum(rm) // np.sum(hh))


# def f_white_ink_hist(char):
#     vh = vertical_histogram(char)
#     hh = horizontal_histogram(char)

# ==================== #
# Statistical features #
# ==================== #

import skimage.io as io

dim = (15, 25)


def f_norm_vertical_hist(char):
    char = cv2.resize(char, dim, interpolation=cv2.INTER_AREA)
    return np.sum(char, axis=0)


def f_norm_horizontal_hist(char):
    char = cv2.resize(char, dim, interpolation=cv2.INTER_AREA)
    return np.sum(char, axis=1)


def f_zoning():
    pass


def f_vertical_crossings():
    pass


def f_horizontal_crossings():
    pass


#############################
##     YAMINA PAPER        ##
#############################

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
    return img[:, count: img.shape[0] - count1]


def f_w_over_h(img):
    new = cut_extra_height(img)
    return new.shape[1] / new.shape[0]


def f_bpixels_over_wpixels(img):
    num_zeros = np.count_nonzero(img == 0)
    num_ones = np.count_nonzero(img == 1)
    return num_zeros / num_ones


def f_horizontal_transitions(img):
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
    return count


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


# ==================== #
#   Get all features   #
# ==================== #

def get_features(char, use_ft_lbp=False):
    holes = np.array([f_get_holes(char)])
    dots = np.array([f_get_dots(char)])

    vertical_trans = np.array([f_vertical_transitions(char)])
    hor_trans = np.array([f_horizontal_transitions(char)])

    w_over_h = np.array([f_w_over_h(char)])
    bp_over_wp = np.array([f_bpixels_over_wpixels(char)])

    norm_hh = np.asarray(f_norm_horizontal_hist(char))
    norm_vh = np.asarray(f_norm_vertical_hist(char))
    # bwr = np.asarray(f_bw_pr(char)).astype(np.uint8)
    cof = np.asarray(f_center_of_mass(char)).astype(np.uint8)
    features = np.concatenate((holes, dots, cof, vertical_trans, hor_trans, w_over_h, bp_over_wp, norm_hh, norm_vh))
    if use_ft_lbp:
        lbp = np.array(f_multi_lbp(char, is_binarized=True, nbins=2))
        # ft = np.array(f_ft(char))
        features = np.concatenate((features, lbp))
    return features

##################################################################################

import cv2 as opencv
import numpy as np
import pandas as pd


def removeMargins(img):
    th, threshed = opencv.threshold(img, 245, 255, opencv.THRESH_BINARY_INV)

    ## (2) Morph-op to remove noise
    kernel = opencv.getStructuringElement(opencv.MORPH_ELLIPSE, (11,11))

    morphed = opencv.morphologyEx(threshed, opencv.MORPH_CLOSE, kernel)

    ## (3) Find the max-area contour
    cnts = opencv.findContours(morphed, opencv.RETR_EXTERNAL, opencv.CHAIN_APPROX_SIMPLE)[-2]
    cnt = sorted(cnts, key=opencv.contourArea)[-1]

    ## (4) Crop and save it
    x,y,w,h = opencv.boundingRect(cnt)
    dst = img[y:y+h, x:x+w]

    new_img = opencv.drawContours(dst,cnt,1,color=(255,255,255),thickness=1)
    opencv.imshow("dst",new_img)

    return dst





image = opencv.imread("test 2.jpg")

cropped_image = removeMargins(opencv.cvtColor(image,opencv.COLOR_RGB2GRAY,None))

combine = np.concatenate((opencv.cvtColor(image,opencv.COLOR_RGB2GRAY,None),cropped_image),axis=1)

opencv.imshow("1",combine)

opencv.waitKey(0)
opencv.destroyAllWindows()


"""
"""def crop_image_height(img):

    projections = np.sum(img, axis=1).astype('int32')

    start = -1
    end_flag = 0

    start_index = 0
    end_index = 0

    crop_image = []

    for idx, horizontal_projection in enumerate(projections):

        if horizontal_projection != 0 and start == -1:
            start_index = idx

            start = start + 1

            pass

        if horizontal_projection == 0 and start != -1:
            end_index = idx

            start = -1

            end_flag = 1

            pass

        if end_flag == 1:
            line_img = np.pad(img[start_index:end_index, :], ((10, 10), (0, 0)), mode='constant',
                              constant_values=0)

            #crop_image.append(line_img)

            end_flag = 0


            pass

            return line_img"""




"""


prediction_features = pickle.load(open("dataset\\custom_features_dataset.pkl","rb"))


print(len(prediction_features))


array_new = np.array(prediction_features)

sample_features = array_new[:,1].tolist()
labels = array_new[:,0].tolist()

print()

for idx, sample_features_list in enumerate(sample_features):

    print(sample_features_list)
    print()
    print(len(sample_features_list))

    if idx == 20:
        break
        pass

    pass


















def boundary_extraction(image):
    rows = len(image[:, 0])

    columns = len(image[0, :])

    # new Plain black image to map contours for visulization

    new_image = image.copy() * 0

    # finding contours by traversing through image height and width and comparing
    # Adjacent Pixels, if the difference of Adjacent pixels is not equals to 0 that
    # indicates the boundary and that pixel index will be added in contours list and
    # its value will be transform 255/white color

    for row_pixel in range(rows - 1):

        for column_pixel in range(columns - 1):

            if image[row_pixel, column_pixel + 1] - image[row_pixel, column_pixel] != 0:
                new_image[row_pixel, column_pixel] = 255

                pass

            if image[row_pixel + 1, column_pixel] - image[row_pixel, column_pixel] != 0:
                new_image[row_pixel, column_pixel] = 255

                pass

            pass

        pass
    
    
    
    return new_image
    pass
    
    
    
    
    
    
    


"""

#######################################################################

