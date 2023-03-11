import cv2 as opencv
import numpy as np


#img = opencv.imread("upti\\upti samples\\118\\118.png")

img = opencv.imread(r"C:\Users\shahzad com\Desktop\upti.png")

img = 255 - img

"""img = 255 - img

second_array = np.ones_like(img) * 100

img = np.bitwise_and(img,second_array)"""

img = opencv.cvtColor(img,opencv.COLOR_RGB2GRAY)

threshold_img = opencv.threshold(img,0,255,opencv.THRESH_BINARY+opencv.THRESH_OTSU)[1]

threshold_img = np.pad(threshold_img,((10,10),(10,10)),constant_values=0)



num_labels , labels = opencv.connectedComponents(threshold_img)

label_hue = np.uint8(179*labels/np.max(labels))

labels_new_image = np.uint8(3000*labels/np.max(labels))

blank_ch = 255*np.ones_like(label_hue)

######################

new_labels = label_hue

######################


labeled_img = opencv.merge([label_hue, blank_ch, blank_ch])

# Converting cvt to BGR
labeled_img = opencv.cvtColor(labeled_img, opencv.COLOR_HSV2BGR)



# set bg label to black
labeled_img[label_hue==0] = 255

labeled_img[label_hue==0] = 0

opencv.imshow("label image",labeled_img)

labeled_img[label_hue==0] = 0

print(np.unique(label_hue))


#blank_image = np.ones_like(threshold_img) * 0

bounding_boxes_list = []

for i in range(num_labels):

    #print()
    #print(np.unique(label_hue)[i])

    single_label =np.unique(label_hue)[i]

    segment_image = opencv.merge([label_hue,blank_ch,blank_ch])

    # Converting cvt to BGR
    segment_image = opencv.cvtColor(segment_image, opencv.COLOR_HSV2BGR)

    segment_image[label_hue != single_label] = 0

    segment_image[label_hue == single_label] = 255


    ###########################      finding contours


    grayscale_segment_image = opencv.cvtColor(segment_image, opencv.COLOR_RGB2GRAY)

    thresh_segment_image = opencv.threshold(grayscale_segment_image, 0, 255, opencv.THRESH_BINARY + opencv.THRESH_OTSU)[1]

    contours, hierarchy = opencv.findContours(thresh_segment_image, opencv.RETR_EXTERNAL, opencv.CHAIN_APPROX_SIMPLE)

    for contour in contours:

        x, y, w, h = opencv.boundingRect(contour)

        rect = opencv.rectangle(segment_image, (x, y), (x + w, y + h), (0, 255, 0), 1)

        #opencv.putText(segment_image, str(x + w), (x + w + 5, y + h), opencv.FONT_HERSHEY_SIMPLEX, 0.4, (36, 255, 12), 1)
        #opencv.putText(segment_image, str(x), (x - w - w - w - 5 , y - 0), opencv.FONT_HERSHEY_SIMPLEX, 0.4, (36, 255, 12), 1)
        pass

    first_index = x
    last_index = x+w
    first_y_index = y
    last_y_index = y+h


    if i>0:

        bounding_boxes_list.append([first_index, last_index,first_y_index,last_y_index, single_label])

        #opencv.imshow("label image No. " + str(i), segment_image)

        pass


    pass


#print(bounding_boxes_list)

print()

new_list = sorted(bounding_boxes_list,key=lambda a:a[0],reverse=True)


print(new_list)

#print(len(new_list))

last_y_index_list = []

width_list = []

for k in range(len(new_list)):

    last_y_index_list.append(new_list[k][3]-new_list[k][2])

    pass


for k in range(len(new_list)):

    width_list.append(new_list[k][1]-new_list[k][0])

    pass



print(last_y_index_list)

print(max(last_y_index_list))

max_height = max(last_y_index_list)

max_width = max(width_list)


diacritics_list = []

for j in range(len(new_list)):

    segment_label = new_list[j][len(new_list[j])-1]

    ligature_height = new_list[j][3]-new_list[j][2]

    ligature_width = new_list[j][1] - new_list[j][0]

    """print()
    print("label : ")
    print(segment_label)"""


    if ligature_height/max_height < 0.30:


        first_index = new_list[j][0]
        last_index = new_list[j][1]
        first_y_index = new_list[j][2]
        last_y_index = new_list[j][3]
        diacritic_label = new_list[j][4]

        #new_labels[new_labels == diacritic_label] == 133

        #segment_image[label_hue != segment_label] = 0

        #segment_image[label_hue == segment_label] = 255

        #rect = opencv.rectangle(segment_image, (first_index, first_y_index), (last_index, last_y_index), (0, 255, 0), 1)


        #opencv.putText(segment_image, str(last_index), (first_index + 10, last_y_index + 20), opencv.FONT_HERSHEY_SIMPLEX, 0.4, (36, 255, 12), 1)


        #opencv.imshow("label image No. " + str(j), segment_image)


        diacritics_list.append([first_index,last_index,first_y_index,last_y_index,diacritic_label])


        pass



    pass


print()
print("Diacritics list : ")
print(diacritics_list)


for a in range(len(new_list)):


    ligature_height = new_list[a][3] - new_list[a][2]

    ligature_width = new_list[j][1] - new_list[j][0]


    ################ label association will be done here |  |
    #                                                    |  |
    #                                                    |  |
    #                                                   \|  |/
    #                                                    \  /
    #                                                     \/

    if ligature_height / max_height > 0.30:

        first_index = new_list[a][0]
        last_index = new_list[a][1]
        first_y_index = new_list[a][2]
        last_y_index = new_list[a][3]
        ligature_label = new_list[a][4]

        #new_labels[new_labels == ligature_label] = 8300


        for index in range(len(diacritics_list)):

            diacritic_start_index = diacritics_list[index][0]
            diacritic_label = diacritics_list[index][4]

            if first_index < diacritic_start_index and last_index > diacritic_start_index :

                print("---values---")

                print("diacritic_start_index : ",diacritic_start_index)
                print()
                print("start_index : ",first_index)
                print()
                print("last_index : ",last_index)
                print()

                print("---values---")

                segment_label = new_list[a][len(new_list[a]) - 1]



                label_hue[label_hue == diacritic_label] = segment_label


                """rect = opencv.rectangle(segment_image, (first_index, first_y_index), (last_index, last_y_index),
                                        (0, 255, 0), 1)

                opencv.putText(segment_image, str(last_index), (first_index + 10, last_y_index + 20), opencv.FONT_HERSHEY_SIMPLEX, 0.4, (36, 255, 12), 1)

                opencv.imshow("label image No. " + str(index), segment_image)"""




                pass


            pass



        # segment_image[label_hue == segment_label] = 255

        # rect = opencv.rectangle(segment_image, (first_index, first_y_index), (last_index, last_y_index), (0, 255, 0), 1)

        # opencv.putText(segment_image, str(last_index), (first_index + 10, last_y_index + 20), opencv.FONT_HERSHEY_SIMPLEX, 0.4, (36, 255, 12), 1)

        # opencv.imshow("label image No. " + str(j), segment_image)


        pass

    threshold_1 = 0.30
    threshold_2 = 0.50

    if ligature_height / max_height < threshold_1:

        ligature_label = new_list[a][4]

        new_labels[new_labels == ligature_label] = 1200


        pass

    if ligature_height / max_height > threshold_1:

        ligature_label = new_list[a][4]

        new_labels[new_labels == ligature_label] = 200


        pass


    pass

#################################################################################



new_label_list = np.unique(label_hue)

print(new_label_list)

for i in range(len(new_label_list)-1):

    segment_image[label_hue != new_label_list[i]] = 0

    segment_image[label_hue == new_label_list[i]] = 255

    if new_label_list[i]>0:

        opencv.imshow("label image No. " + str(i), segment_image)

        pass




    pass


labeled_img[label_hue != 0] = 255

#opencv.imshow("label image 0",labeled_img)


labeled_img = opencv.cvtColor(labeled_img,opencv.COLOR_RGB2GRAY)

labeled_img =  np.pad(labeled_img,((20,20),(20,20)),constant_values=0)

labeled_img = opencv.threshold(labeled_img,0,255,opencv.THRESH_BINARY+opencv.THRESH_OTSU)[1]

contours,hierarchy = opencv.findContours(labeled_img,opencv.RETR_EXTERNAL,opencv.CHAIN_APPROX_SIMPLE)

contours = sorted(contours, key=lambda ctr: opencv.boundingRect(ctr)[0], reverse=True)

labeled_img = opencv.cvtColor(labeled_img,opencv.COLOR_GRAY2RGB)

#Counters = opencv.drawContours(labeled_img,contours, -1, (0,255,0),1)

size_list = []

for single_contour in contours:

    size_list.append(opencv.boundingRect(single_contour)[3])

    pass


max_count = max(size_list)

i = 0
for contour in contours:

    i = i + 1

    x, y, w, h = opencv.boundingRect(contour)

    #if ((x/(x+w))/2 + (y/(y+h))/2) > 0.38:
    if (h/max_count) < 0.28:

        rect = opencv.rectangle(labeled_img, (x, y), (x + w, y + h), (0, 255, 0), 1)

        first_x_index = x
        last_x_index = x+w

        opencv.putText(labeled_img, str(h), (last_x_index - 20, y+h+15), opencv.FONT_HERSHEY_SIMPLEX, 0.4, (36, 255, 12), 1)
        opencv.putText(labeled_img, str(w), (first_x_index, y - 5), opencv.FONT_HERSHEY_SIMPLEX, 0.4, (36, 255, 12), 1)
        pass

    #print("y coordinate : ")
    #print(y)
    #print()
    #print(y+h)



    pass




opencv.imshow("labeled_img",labeled_img)

#label_hue = np.uint8(179*(np.unique(label_hue))/np.max((np.unique(label_hue))))

new_image = opencv.merge([label_hue, blank_ch, blank_ch])

new_image = opencv.cvtColor(new_image, opencv.COLOR_HSV2BGR)


# set bg label to black
new_image[label_hue==0] = 255


opencv.imshow("new_image",new_image)


new_segment_image = opencv.merge([new_labels, blank_ch, blank_ch])

new_segment_image = opencv.cvtColor(new_segment_image, opencv.COLOR_HSV2BGR)


# set bg label to black
new_segment_image[new_labels==0] = 255


opencv.imshow("new_segment_image",new_segment_image)



"""opencv.imshow("img",img)

opencv.imshow("threshold_img",threshold_img)

opencv.imshow("label_hue",label_hue)

opencv.imshow("label new image",labels_new_image)

opencv.imshow("labeled_img",labeled_img)"""

print(img.shape)



opencv.waitKey(0)

opencv.destroyAllWindows()
