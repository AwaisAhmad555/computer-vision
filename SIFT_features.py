import cv2 as opencv
import os
import numpy as np
import pandas as pd
from skimage.feature import hog
import random
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm


def load_dataset(root_path):


    images_array = []
    dataset_array = []

    folder_list = os.listdir(root_path)

    for item in folder_list:

        current_path = os.path.join(root_path, item)

        if os.path.isfile(current_path):

            # print(folder + " is a file")

            """print()
            print()
            print(item + " is a file")
            print()
            print("path is : ", current_path)"""

            pass

        else:

            """print()
            print()
            print(item + " is a folder")
            print()
            print("path is : ", current_path)"""

            classes = os.listdir(current_path)

            print()
            #print(classes)

            for single_class in classes:

                images_path = os.path.join(current_path,single_class)

                images_list = os.listdir(images_path)

                for image_name in images_list:

                    image_address = os.path.join(images_path,image_name)

                    """print()
                    print()
                    print()
                    print(image_address)"""

                    image = opencv.imread(image_address)

                    images_array.append(image)

                    #print(single_class)

                    dataset_array.append([int(single_class),image])


                    pass

                pass




            pass




        pass


    print()
    print()
    print(folder_list)


    return dataset_array, images_array
    """return list([0])"""

    pass


root_path = "dataset"

full_dataset, dataset_list = load_dataset(root_path)

print()

print(np.array(full_dataset).shape)

print()

print(np.array(full_dataset)[0,:])

#opencv.imshow("label : "+str(full_dataset[10][0]), full_dataset[10][1])

for idx,img in enumerate(dataset_list):


    #opencv.imshow(""+str(idx), img)

    sift = opencv.xfeatures2d.SIFT_create()

    keypoints_1, descriptors_1 = sift.detectAndCompute(img, None)

    # sift_image = opencv.drawKeypoints(dataset_list[211],keypoints_1,dataset_list[211])

    sift_image = opencv.drawKeypoints(img, keypoints_1, None, color=(0, 255, 0), flags=0)

    print(descriptors_1.shape)

    opencv.imshow("sift "+str(idx), np.concatenate((img,sift_image),axis=1))

    if idx == 10:
        break
        pass


    pass


print(len(dataset_list))

random.shuffle(full_dataset)


for label, image in full_dataset:

    image = opencv.cvtColor(image, opencv.COLOR_RGB2GRAY, None, None)

    # contour_image = draw_contours(image)

    # openCV.imshow("images " + str(idx),image)

    fd, hog_image = hog(image, orientations=4, block_norm='L2', pixels_per_cell=(8, 8),
                        cells_per_block=(2, 2), visualize=True, multichannel=False)

    opencv.imshow("images label. " + str(label), np.concatenate((image,hog_image),axis=1))


    break

    pass

opencv.waitKey(0)
opencv.destroyAllWindows()