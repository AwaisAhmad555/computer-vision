import numpy as np
import cv2 as openCV
import matplotlib.pyplot as plot


img = openCV.imread("test1.png")

copy = img.copy()

line_start_index_list = []
line_last_index_list = []

def projection(img,type:str):


    if type == 'horizontal':

        projections = np.sum(img, 1).astype('int32')
    elif type == 'vertical':

        projections = np.sum(img, 0).astype('int32')
        pass

    return projections
    pass


def preprocessing(img):

    gray_img = openCV.cvtColor(img,openCV.COLOR_RGB2GRAY)

    parameter, threshold_img = openCV.threshold(gray_img,220,255,openCV.THRESH_BINARY_INV)

    threshold_img = openCV.GaussianBlur(threshold_img,(1,1),sigmaX=1,sigmaY=1)

    return threshold_img


def line_segmentation(projections_list):

    start = -1
    end_flag = 0

    start_index = 0
    end_index = 0

    text_lines = []

    for idx, horizontal_projection in enumerate(projections_list):

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

            line_img = np.pad(img[start_index:end_index,:],((0,0),(0,0),(0,0)), mode='constant', constant_values=255)
            text_lines.append(line_img)

            end_flag = 0

            line_start_index_list.append(start_index)
            line_last_index_list.append(end_index)


            pass

    return text_lines

def word_segmentation(projections_list,line_image,line_start_index,line_end_index):

    flag = 0
    start = -1
    end = 0
    gap_flag = 0

    words_list = []


    for idx, single_projection in enumerate(projections_list):

        #print(single_projection)
        #print()

        if single_projection != 0:

            #copy[:, idx, 0] = 0

            pass

        if single_projection !=0 and start == -1:


            start_index = idx
            #openCV.imshow(""+str(idx),img[:,idx:])

            start = start + 1
            pass

        if single_projection == 0 and start != -1:

            gap_flag = gap_flag + 1

            pass

        if gap_flag == 1:

            end_index = idx
            start = start + 1
            gap_flag = 0

            pass

        if start == 1:

            #openCV.imshow(""+str(idx),img[:,start_index:end_index])
            copy[line_start_index:line_end_index, start_index:end_index, 2] = 0
            words_list.append(line_image[:,start_index:end_index])

            start = -1
            pass

        pass

    return words_list

#/////////////////////////////////////

copy_image = openCV.cvtColor(img[:,:,0].copy(),openCV.COLOR_GRAY2RGB)

def character_segmentation(character_img,baseline_image):

    copy_image = openCV.cvtColor(character_img.copy(),openCV.COLOR_GRAY2RGB)

    copy_image_dimension = copy_image.shape

    #new_copy_image = np.zeros(copy_image_dimension)

    new_copy_image = np.zeros((copy_image.shape[0]+100,copy_image.shape[1]+100))

    #copy_image = openCV.copyMakeBorder(copy_image,6,6,6,6,borderType=openCV.BORDER_ISOLATED)

    #copy_image = np.pad(copy_image,((0,0),(6,6),(0,0)), mode='constant', constant_values=0)

    #character_img = np.pad(character_img, ((0, 0), (6, 6), (0, 0)), mode='constant', constant_values=0)

    openCV.imshow("character",character_img)
    #openCV.imshow("new copy",new_copy_image)

    max = 0

    total_max = 0

    maximum_index = 0

    for row in range(len(character_img[:,0])):

        for column in range(len(character_img[row,:])-1):

            if character_img[row, column] - character_img[row, column + 1] != 0:

                max = max + 1

                pass

            pass


        if max > total_max:

            total_max = max

            maximum_index = row

            pass

        max = 0

        if row == len(character_img[:,0])-1:

            character_start_idx = 0
            character_end_idx = 0

            start_flag = -1

            for i in range(len(character_img[maximum_index,:])-1):

                if character_img[maximum_index,i] - character_img[maximum_index,i+1] == 255:

                    #if i == (len(character_img[maximum_index,:])-2):
                    character_img[:,i] = 255
                    copy_image[:,i,2] = 255
                        #pass

                    print(i)
                    print()

                    if start_flag == -1 and character_start_idx == 0:
                        character_start_idx = i
                        start_flag = start_flag + 1
                        print("start index",character_start_idx)
                        pass

                    elif start_flag != -1:
                        character_end_idx = i+1
                        start_flag = -1
                        pass

                    if character_end_idx != 0:

                        openCV.imshow("character No ."+str(i),np.pad(copy_image[:,character_start_idx:character_end_idx],((0,0),(20,20),(0,0)), mode='constant', constant_values=0))

                        print("start :",character_start_idx)
                        print()
                        print("end :",character_end_idx)
                        pass

                    character_start_idx = character_end_idx
                    start_flag = start_flag + 1

                    pass

                if i == len(character_img[maximum_index, :]) - 2:
                    #openCV.imshow("character No ." + str(i), np.pad(copy_image[:, :-character_start_idx+10], ((0, 0), (20, 20), (0, 0)), mode='constant', constant_values=0))
                    print("this is end index : ",character_end_idx)
                    character_end_idx = i
                    pass

                pass

            character_img[maximum_index,:] = 255

            pass

        pass

    openCV.imshow("character-with-lmt", character_img)
    openCV.imshow("copy",copy_image)


    return

openCV.imshow("copy",copy_image)


img = openCV.imread("test1.png")


grayscale_img = preprocessing(img)

openCV.imshow("gray",grayscale_img)

projections_list = projection(grayscale_img/255, type='horizontal')

values_list = projections_list.tolist()

#print(values_list)

indexlist = []
for ids, numbers in enumerate(values_list):

    indexlist.append(ids)
    pass

#plot.plot(values_list,indexlist)

#plot.show()

print("projection list ",projections_list)

lines = line_segmentation(projections_list)

line_projections_list = []

#openCV.imshow("line", lines[5])

for idx,line_image in enumerate(lines):

    line_image = preprocessing(line_image)

    openCV.imshow("line No. "+str(idx), line_image)

    pass

print(len(lines))

for line_images in lines:

    line_images = preprocessing(line_images)
    vertical_projection = projection(line_images / 255, type='vertical')

    line_projections_list.append(vertical_projection)

    pass

print(line_projections_list[0])

all_words_list = []
for idx, line_img in enumerate(lines):

    words_list = word_segmentation(line_projections_list[idx],lines[idx],line_start_index_list[idx],line_last_index_list[idx])

    all_words_list.append(words_list)

    pass

baseline_images_list = []

descriptor_list = []

label = 0

for idx,word_image in enumerate(all_words_list):

    word_image.reverse()

    for img_idx,single_word_image in enumerate(word_image):

        label = label + 1

        word_image = preprocessing(single_word_image)

        #extra padding functions just skip

        padding_value = 200 - len(word_image[0,:])
        height_padding_value = 200 - len(word_image[:,0])

        padding_value_1 = float(padding_value/2)
        height_padding_value_1 = float(height_padding_value / 2)

        padding_value_1 = int(padding_value_1)
        height_padding_value_1 = int(height_padding_value_1)

        #word_image = np.pad(word_image,((height_padding_value_1,height_padding_value_1),(padding_value_1,padding_value_1)), mode='constant', constant_values=0)

        word_image = np.pad(word_image,((10, 10), (10, 10)),mode='constant', constant_values=0)

        word_image = openCV.resize(word_image,(200,200),interpolation=openCV.INTER_AREA)
        
        #detector = openCV.FastFeatureDetector_create()
        # find the keypoints with ORB
        #kp = detector.detect(word_image, None)

        sift = openCV.xfeatures2d.SIFT_create()
        keypoints_1, descriptors_1 = sift.detectAndCompute(word_image, None)

        descriptor_list.append(descriptors_1)

        new_word_image = openCV.drawKeypoints(word_image, keypoints_1, None, color=(0, 255, 0), flags=0)

        parameters, word_image = openCV.threshold(word_image, 100, 255, openCV.THRESH_BINARY, None)

        openCV.imshow("Line No . "+ str(idx) +"Word No . " + str(img_idx),word_image)

        openCV.imshow("Line No . " + str(idx+100) + "Word No . " + str(img_idx+100), new_word_image)


        #word_image = img_pad = openCV.copyMakeBorder(word_image, 50, 50, 50, 50, openCV.BORDER_CONSTANT, (0,0,0))


        #openCV.imwrite("sample_2\\segment_images\\"+str(idx)+" - " + str(img_idx)+".png",word_image)


        openCV.imwrite("sample_2\\segment_images\\" + str (label) + ".png", word_image)

        #print(word_image)
        pass

    pass

for descriptor_index,descriptor in enumerate(descriptor_list):

    try:
        print()
        print(descriptor.shape)
        print()
        print("index : ",descriptor_index)
    except:
        pass

    #if not (descriptor_index is None):

        #pass


    pass

"""
    if descriptor_index == 3:
        print()
        print(descriptor.shape)
        print()

    if descriptor_index == 4:
        print()
        print(descriptor.shape)
        print()

    if descriptor_index == 5:
        print()
        print(descriptor.shape)
        print()

    if descriptor_index == 6:
        print()
        print(descriptor.shape)
        print()
        
    """

for idx,images in enumerate(baseline_images_list):

    openCV.imshow(""+ str(idx),images)

    pass

#words_list[0] = np.pad(words_list[0],((0,0),(20,20),(0,0)), mode='constant', constant_values=255)

#character_segmentation(preprocessing(words_list[0]),grayscale_img)

#character_segmentation(grayscale_img,grayscale_img)

openCV.imshow("segmented image",copy)

openCV.imshow("",img)

print(padding_value_1)
print()
print(height_padding_value_1)
openCV.waitKey(0)
openCV.destroyAllWindows()
