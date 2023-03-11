import cv2 as opencv
import numpy as np

##############################################################





##############################################################


def contour_based_subwords_segmentation(image):
    ###########################################

    img = image

    img = opencv.cvtColor(img, opencv.COLOR_RGB2GRAY, None)

    param, thresh_img = opencv.threshold(img, 200, 255, type=opencv.THRESH_BINARY)

    # Structure element for performing erosion operation for getting smooth and
    # Accurate contours [[1,1],[1,1]] = (2x2)[1]

    # for different font size have changing here
    #               ||
    #               ||
    #               ||
    #              \  /
    #               \/
    kernel = np.ones((1, 2), np.uint8)

    img_erosion = opencv.erode(thresh_img, kernel, iterations=1)

    # No need to perform dialation
    # img_dilation = opencv.dilate(thresh_img, kernel, iterations=1)

    # assigning erode image to the thresh_img variable
    thresh_img = img_erosion

    # opencv.imshow("erode image", img_erosion)

    binary_image = img

    rows = len(binary_image[:, 0])

    columns = len(binary_image[0, :])

    # new Plain black image to map contours for visulization

    new_image = binary_image.copy() * 0

    # finding contours by traversing through image height and width and comparing
    # Adjacent Pixels, if the difference of Adjacent pixels is not equals to 0 that
    # indicates the boundary and that pixel index will be added in contours list and
    # its value will be transform 255/white color

    for row_pixel in range(rows - 1):

        for column_pixel in range(columns - 1):

            if thresh_img[row_pixel, column_pixel + 1] - thresh_img[row_pixel, column_pixel] != 0:
                new_image[row_pixel, column_pixel] = 255

                pass

            if thresh_img[row_pixel + 1, column_pixel] - thresh_img[row_pixel, column_pixel] != 0:
                new_image[row_pixel, column_pixel] = 255

                pass

            pass

        pass

    contours, hierarchy = opencv.findContours(image=new_image, mode=opencv.RETR_EXTERNAL,
                                              method=opencv.CHAIN_APPROX_SIMPLE)

    # contours = sorted(contours, key=opencv.contourArea,reverse=True)

    # sorting contours along horizontal axis from right to left

    contours = sorted(contours, key=lambda ctr: opencv.boundingRect(ctr)[0], reverse=True)

    contour_img = opencv.drawContours(opencv.cvtColor(new_image.copy(), opencv.COLOR_GRAY2RGB, None), contours, -1,
                                      (0, 255, 75), 1)

    copy_image = opencv.cvtColor(new_image.copy(), opencv.COLOR_GRAY2RGB, None)

    # opencv.imshow("contour_image",contour_img)

    kernel = np.ones((1, 1), np.uint8)

    i = 0

    plain_image = img.copy()

    img = opencv.cvtColor(img, opencv.COLOR_GRAY2RGB, None)

    segment_images_list = []

    bounding_box_size_array = []

    for cnt in contours:

        x, y, w, h = opencv.boundingRect(cnt)

        bounding_box_size_array.append(h)

        pass

    maximum_size = max(bounding_box_size_array)

    print(maximum_size)

    i = 0
    for idx,cnt in enumerate(contours):

        i = i + 1

        x, y, w, h = opencv.boundingRect(cnt)

        """rect = opencv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)

        opencv.putText(img, str(h), (x, y - 10), opencv.FONT_HERSHEY_SIMPLEX, 0.4, (36, 255, 12), 1)"""

        if h/maximum_size > 0.00:
            # image full height , # bounding box width

            if x == 0:
                x = 1
                pass

            cropped_image = plain_image[0 + 1:img.shape[0] - 1, x - 1:x + w + 1]

            padded_image = np.pad(cropped_image, ((0, 0), (2, 2)), mode='constant', constant_values=0)

            # resized_image = opencv.resize(padded_image, (200, 200))

            rect = opencv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)

            opencv.putText(img, str(idx), (x, y - 10), opencv.FONT_HERSHEY_SIMPLEX, 0.4, (36, 255, 12), 1)

            resized_image = opencv.resize(padded_image, (padded_image.shape[1], padded_image.shape[0]))

            img_erosion = opencv.erode(resized_image, kernel, iterations=1)

            parameter, segment_image = opencv.threshold(img_erosion, 200, 255, opencv.THRESH_BINARY, None)

            segment_images_list.append(segment_image)

            pass

        i = i + 1

        pass

    opencv.imshow("img",img)

    return segment_images_list
    pass


########################

img = opencv.imread("upti.png")

#img = 255 - img

param, img = opencv.threshold(img, 200, 255, type=opencv.THRESH_BINARY_INV)

img = np.pad(img,((50,50),(40,40),(0,0)))


print('Original Dimensions : ', img.shape)

scale_percent = 100  # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

img = opencv.resize(img,dim,None)

#thresh, img =  opencv.threshold(img,70,255,opencv.THRESH_BINARY,None)


images_list = contour_based_subwords_segmentation(img)

for idx,single_image in enumerate(images_list):

    opencv.imshow(str (idx) +" ",single_image)

    pass

opencv.waitKey(0)

opencv.destroyAllWindows()