from features_extraction import *
import cv2 as opencv
import numpy as np
import os


def sum_histogram_function(image):

    image = image/255

    histogram_sum = np.sum(image,axis=0)

    histogram_sum = list (histogram_sum)

    """for i in range(len(histogram_sum)):

        histogram_sum[i] = int (histogram_sum[i])
        
        pass"""


    return histogram_sum
    pass

################################## main program ########################


img = opencv.imread("temporary\\segment_images\\16.png")

#img = opencv.imread("dataset\\urdu_dataset\\13\\21.png")



#img = 255 - img

thresh , img = opencv.threshold(img,200,255,opencv.THRESH_BINARY,None)

#img = opencv.Canny(img,200,255)

opencv.imshow("image",img)

img = opencv.cvtColor(img,opencv.COLOR_RGB2GRAY,None)

"""image_contour, parameter = opencv.findContours(image=img,mode=opencv.RETR_LIST,method=opencv.CHAIN_APPROX_SIMPLE)

output_image = img.copy() * 0

output_image = opencv.cvtColor(output_image,opencv.COLOR_GRAY2RGB,None)

output_image = opencv.drawContours(output_image,image_contour,-1,(0,255,0),1)

opencv.imshow("contours",output_image)"""




#new_crop_image = cut_extra_width(img=img)

new_crop_image = cut_extra_height(img=img)


new_crop_image = np.pad(new_crop_image,((5,5),(0,0)),constant_values=255)

new_crop_image = opencv.resize(new_crop_image,(100,100),None)


thresh , new_crop_image = opencv.threshold(new_crop_image,200,255,opencv.THRESH_BINARY,None)

y, x = new_crop_image.shape

topLeft = new_crop_image[0:y // 2, 0:x // 2]
topRight = new_crop_image[0:y // 2, x // 2:x]
bottomeLeft = new_crop_image[y // 2:y, 0:x // 2]
bottomRight = new_crop_image[y // 2:y, x // 2:x]

opencv.imshow("topLeft",topLeft)
opencv.imshow("topRight",topRight)
opencv.imshow("bottomeLeft",bottomeLeft)
opencv.imshow("bottomRight",bottomRight)


opencv.imshow("crop_image",new_crop_image)

#img = crop_image

sum_histogram = sum_histogram_function(new_crop_image)

print(new_crop_image.shape)
print()
print(sum_histogram)

print()
print(len(sum_histogram))


print()


holes_features = f_get_holes(img)

dotes_features = f_get_dots(img)

#margin_removed_image = removeMargins(img=img)



print("holes features : ")
print()
print(holes_features)
print()

print("dots features : ")
print(dotes_features)


print("\n")
black_to_white_ratio = whiteBlackRatio(img=new_crop_image)


print("black to white ratio feature : ")
print(black_to_white_ratio)

print()


horizontalTransitions = horizontalTransitions(img=new_crop_image)
verticalTransitions = verticalTransitions(img=new_crop_image)

print("\n")
print("average horizontal transitions : " + str (horizontalTransitions))

print("\n")
print("average Vertical transitions : " + str (verticalTransitions))


"""print("\n")
print("horizontal transitions : " + str (f_horizontal_transitions(img)))

print("\n")
print("Vertical transitions : " + str (f_vertical_transitions(img)))"""


print("\n")
print("width over height : " + str (width_over_height(new_crop_image)))

xCenter, yCenter, xHistogram = histogramAndCenterOfMass(new_crop_image)

print("\n")
print("xHistogram : \n")
print(xHistogram)


print("\n")
print("xCenter : " + str (xCenter))

print("\n")

print("yCenter : " + str (yCenter))

print("\n")

print("xHistogram Average : " + str (np.sum(xHistogram,axis=0)/len(xHistogram)))


#features_list = get_features(img=new_crop_image)

print()

#print(features_list)


opencv.waitKey(0)
opencv.destroyAllWindows()
