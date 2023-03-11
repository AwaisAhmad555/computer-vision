import cv2 as opencv

#path_1 = ''


##########################################################

path_1 = r'F:\image 2.png'
path_2 = r'F:\image1.png'


image_1 = opencv.imread(path_1)

image_1 = opencv.resize(image_1,(300,300))

image_2 = opencv.imread(path_2)

image_2 = opencv.resize(image_2,(300,300))

resized_image = image_1.copy()


opencv.imshow("1",image_1)

opencv.imshow("2",image_2)


print(image_2.shape)
print(image_1.shape)

image_1 = opencv.Canny(image_1,50,100)


image_2 = opencv.Canny(image_2,50,100)

kernel = opencv.getStructuringElement(opencv.MORPH_RECT, (3,3))

image_1 = opencv.morphologyEx(image_1, opencv.MORPH_CLOSE, kernel)

image_2 = opencv.morphologyEx(image_2, opencv.MORPH_CLOSE, kernel)


contours, hierarchy = opencv.findContours(image=image_1,mode=opencv.RETR_EXTERNAL,method=opencv.CHAIN_APPROX_SIMPLE)

#contours = sorted(contours, key= lambda contour: opencv.boundingRect(contour)[0], reverse=False)

contours = sorted(contours, key=opencv.contourArea, reverse=True)[:1]

x, y, w, h = opencv.boundingRect(contours[0])

contour_img = opencv.drawContours(opencv.cvtColor(image_1.copy(), opencv.COLOR_GRAY2RGB, None), contours, -1,
                                      (0, 0, 255), 2)

#(0, 255, 75)
new_image = opencv.rectangle(resized_image, (x, y), (x + w, y + h), (0, 0, 255), 2)


opencv.imshow("contour_img",contour_img)

opencv.imshow('cropped_image',resized_image)




opencv.imshow("canny 1",image_1)

opencv.imshow("canny 2",image_2)


#path = r'C:\Users\shahzad com\Desktop\predictions\pred_BRATS_Segnet.png'

"""
image =  opencv.imread(path)

#opencv.imshow("image",image[83:336,818:1068,:])

#opencv.imshow("image",image[83:336,162:413,:])

#opencv.imshow("image",image[83:336,490:740,:])

opencv.imshow("image",image[21:220,507:703,:])"""




opencv.waitKey(0)
opencv.destroyAllWindows()
