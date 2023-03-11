import tensorflow as tf
from keras.models import load_model
import cv2 as opencv
import numpy as np


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

def add_extra_margin(img):

    padded_image = np.pad(img,((50,50),(50,50)),constant_values=0)


    return padded_image

def pre_processing(image):

    #image = np.invert(image)

    image = opencv.cvtColor(image, opencv.COLOR_RGB2GRAY)

    parameter, image = opencv.threshold(image, 0, 255, opencv.THRESH_BINARY + opencv.THRESH_OTSU)

    image = cut_extra_width(img=image)

    image = cut_extra_height(image)

    image = add_extra_margin(image)

    kernel = np.ones((4, 4), np.uint8) * 255

    #print(kernel)

    image = opencv.dilate(image, kernel=kernel, iterations=1)


    return image
    pass

def segmentation(image):


    image = np.invert(image)

    original_image = image.copy()

    bounding_box_image = image.copy()

    image = opencv.cvtColor(image,opencv.COLOR_RGB2GRAY)

    image = opencv.threshold(image, 0, 255, opencv.THRESH_BINARY + opencv.THRESH_OTSU)[1]

    kernel = opencv.getStructuringElement(opencv.MORPH_RECT, (3,3))

    image = opencv.morphologyEx(image, opencv.MORPH_CLOSE, kernel)

    #opencv.imshow("threshold_image",image)

    image = opencv.Canny(image=image,threshold1=150,threshold2=200)

    #opencv.imshow("canny",image)

    canny_image = image.copy()

    image = opencv.threshold(image,0,255,opencv.THRESH_BINARY + opencv.THRESH_OTSU)[1]

    """kernel = opencv.getStructuringElement(opencv.MORPH_ELLIPSE,(1,2))

    image = opencv.morphologyEx(image,opencv.MORPH_OPEN,kernel=kernel)

    opencv.imshow("morphological operation image", image)"""

    contours, hierarchy = opencv.findContours(image=image,mode=opencv.RETR_EXTERNAL,method=opencv.CHAIN_APPROX_SIMPLE)

    contours = sorted(contours, key= lambda contour: opencv.boundingRect(contour)[0], reverse=False)

    contour_img = opencv.drawContours(opencv.cvtColor(image.copy(), opencv.COLOR_GRAY2RGB, None), contours, -1,
                                      (0, 255, 75), 1)


    images_list = []

    height_list = []

    for contour in contours:

        height = opencv.boundingRect(contour)[3]

        height_list.append(height)

        pass

    maximum_height = max(height_list)

    for contour in contours:

        x, y, w, h = opencv.boundingRect(contour)

        if h/maximum_height > 0.40:

            rect = opencv.rectangle(bounding_box_image, (x, y), (x + w, y + h), (0, 255, 0), 1)

            images_list.append(original_image[y:y + h, x:x + w])


            pass

        pass

    #opencv.imshow("bounding_box_image",bounding_box_image)

    return images_list, canny_image, bounding_box_image


def prediction_function(image):


    image = opencv.resize(image, (28, 28))


    #opencv.imshow("28x28 image",image)

    image = image.reshape(1, 28, 28, 1)
    image = image.astype('float32')
    image /= 255

    model = load_model('cnn.h5')

    out = model.predict(image)

    """print()
    print("Predicted number is :")
    print(np.argmax(out))"""


    return np.argmax(out)
    pass

############################################################





def main_program(file_name : str, color_check):

    image = opencv.imread(filename=file_name)

    if color_check != 1:

        image = np.invert(image)

        pass

    images_list, canny_image, bounding_box_image = segmentation(image=image)

    # opencv.imshow("canny_image",canny_image)

    # opencv.imshow("bounding_box_image",bounding_box_image)

    numbers_list = []

    for idx, single_image in enumerate(images_list):
        # opencv.imshow("Image No. " + str(idx), single_image)

        new_image = pre_processing(single_image)

        # opencv.imshow("Preprocessing Image No. " + str(idx), new_image)

        number = prediction_function(new_image)

        numbers_list.append(number)

        # opencv.waitKey(0)
        # opencv.destroyAllWindows()

        pass

    complete_number = ''

    for number in numbers_list:

        complete_number = complete_number + str(number)

        pass



    return complete_number,canny_image,bounding_box_image
    pass



"""image = opencv.imread("number_plate.png")

image = opencv.cvtColor(image,opencv.COLOR_RGB2GRAY)

image = opencv.GaussianBlur(image,(5,5),0)

image = opencv.Canny(image,50,200,255)

opencv.imshow("-",image)

opencv.waitKey(0)
opencv.destroyAllWindows()"""



#print(model)

