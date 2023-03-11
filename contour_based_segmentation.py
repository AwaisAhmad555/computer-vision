import cv2 as opencv
import numpy as np



def contour_based_subwords_segmentation(image):


    ###########################################

    img = image

    img = opencv.cvtColor(img, opencv.COLOR_RGB2GRAY, None)

    param, thresh_img = opencv.threshold(img, 200, 255, type=opencv.THRESH_BINARY)


    #Structure element for performing erosion operation for getting smooth and
    #Accurate contours [[1,1],[1,1]] = (2x2)[1]

    #for different font size have changing here
    #               ||
    #               ||
    #               ||
    #              \  /
    #               \/
    kernel = np.ones((1,2), np.uint8)

    img_erosion = opencv.erode(thresh_img, kernel, iterations=1)

    #No need to perform dialation
    #img_dilation = opencv.dilate(thresh_img, kernel, iterations=1)


    #assigning erode image to the thresh_img variable
    thresh_img = img_erosion

    #opencv.imshow("erode image", img_erosion)


    binary_image = img



    rows = len(binary_image[:, 0])

    columns = len(binary_image[0, :])


    #new Plain black image to map contours for visulization

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

    #sorting contours along horizontal axis from right to left

    contours = sorted(contours, key=lambda ctr: opencv.boundingRect(ctr)[0], reverse=True)


    contour_img = opencv.drawContours(opencv.cvtColor(new_image.copy(), opencv.COLOR_GRAY2RGB, None), contours, -1,
                                      (0, 255, 75), 1)

    copy_image = opencv.cvtColor(new_image.copy(), opencv.COLOR_GRAY2RGB, None)

    #opencv.imshow("contour_image",contour_img)


    kernel = np.ones((1, 1), np.uint8)


    i = 0

    plain_image = img.copy()

    img = opencv.cvtColor(img, opencv.COLOR_GRAY2RGB, None)

    segment_images_list = []


    for cnt in contours:

        x, y, w, h = opencv.boundingRect(cnt)

        rect = opencv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)

        opencv.putText(img, str(h), (x, y - 10), opencv.FONT_HERSHEY_SIMPLEX, 0.4, (36, 255, 12), 1)

        if h > 13 :

            #image full height , # bounding box width
            cropped_image = plain_image[0+1:img.shape[0]-1, x + 1:x + w + 0]

            padded_image = np.pad(cropped_image, ((0, 0), (2, 2)), mode='constant', constant_values=0)

            #resized_image = opencv.resize(padded_image, (200, 200))

            resized_image = opencv.resize(padded_image, (padded_image.shape[1], padded_image.shape[0]))


            img_erosion = opencv.erode(resized_image, kernel, iterations=1)

            parameter, segment_image = opencv.threshold(img_erosion, 200, 255, opencv.THRESH_BINARY, None)


            segment_images_list.append(segment_image)

            pass

        i = i + 1

        pass

    #opencv.imshow("img",img)


    return segment_images_list
    pass


########################

#img = opencv.imread("temporary\\3.png")

#img = 255 - img

"""opencv.imshow("new",img)


segment_images_list = contour_based_subwords_segmentation(img)

for idx,images in enumerate(segment_images_list):

    opencv.imshow(""+ str(idx),images)

    pass"""



"""

    #opencv.imshow("single box - " + str(i), segment_image)
            # opencv.imshow("single box - " + str(i) + str(i), plain_image[y:y + h, x:x + w])

            # opencv.imshow("single box - " + str(i), plain_image[y - 2:y + h + 2, x - 1:x + w + 1])


    opencv.imshow("bounded box", img)
    opencv.imshow("contour image", contour_img)
    
    opencv.imshow("binary_image", binary_image)
    
    
    opencv.imshow("copy_image_1", new_image)
    
    print(len(binary_image[0, :]))

    print()

    print(len(binary_image[:, 0]))

    print(img.shape)
    
    print()

    print("rows = : ", rows)

    print()

    print("columns = : ", columns)
    
    print(kernel)
    
    
    opencv.imshow("", img)

    opencv.imshow("2", thresh_img)

    #opencv.imshow("img_dilation", img_dilation)
    opencv.imshow("img_erosion", img_erosion)

    

    opencv.imshow("copy_image", new_image)
    
    """

"""opencv.waitKey(0)

opencv.destroyAllWindows()"""