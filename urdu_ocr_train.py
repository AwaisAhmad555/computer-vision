import os
import numpy as np
import pandas as pd
import cv2 as openCV
from skimage.feature import hog
import random
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.model_selection import train_test_split
import pickle


#full_path = r"C:\Users\shahzad com\PycharmProjects\urdu_ocr\data_samples"

full_path = r"C:\Users\shahzad com\PycharmProjects\urdu_ocr\dataset\urdu_dataset"

directory = os.listdir(full_path)


dataset_list = []

X = []
Y = []

"""
def draw_contours(image):

    contour_image = image.copy()

    contour_image = contour_image * 0

    for i in range(len(image[:,0])):

        for j in range(len(image[0,:])-1):

            if image[i,j] - image[i,j+1] != 0 :

                contour_image[i,j+1] = 255

            pass

        pass

    for j in range(len(image[0, :])):

        for i in range(len(image[:, 0]) - 1):

            if image[i, j] - image[i+1, j] != 0:

                contour_image[i+1, j] = 255

            pass

        pass



    pass
    return contour_image
    """


for folders in directory:

    folder_name = str (folders)

    new_path = os.path.join(full_path,folders)

    for idx, imgs in enumerate(os.listdir(new_path)):
        image = openCV.imread(os.path.join(new_path, imgs))

        image = openCV.cvtColor(image, openCV.COLOR_RGB2GRAY, None, None)

        #contour_image = draw_contours(image)

        #openCV.imshow("images " + str(idx),image)

        fd, hog_image = hog(image, orientations=4, block_norm='L2', pixels_per_cell=(8, 8),
                            cells_per_block=(2, 2), visualize=True, multichannel=False)

        #openCV.imshow(""+folder_name+" - "+str(idx),np.hstack((image,hog_image)))

        label = int(os.path.splitext(imgs)[0])

        #print(label)

        X.append(fd.tolist())
        Y.append(label)

        dataset_list.append([label,fd.tolist()])

        pass

    pass


print(len(X))

print()

print(len(Y))


random.shuffle(dataset_list)




classifier = KNeighborsClassifier(n_neighbors=1,algorithm='brute')

#classifier = svm.SVC(kernel='linear') # Linear Kernel


array_new = np.array(dataset_list)

print("shape : ")
print(array_new[:,:])
print()

classifier.fit(X=array_new[:,1].tolist(),y=array_new[:,0].tolist())


filename = 'finalized_model.sav'
pickle.dump(classifier, open(filename, 'wb'))


print(classifier)

sample_array = array_new[:,1].tolist()
test_labels = array_new[:,0].tolist()

print()
print("testing samples labels = ")
print(test_labels[1:12])

#result = classifier.predict(sample_array[1:12])

#print(result)






openCV.waitKey(0)
openCV.destroyAllWindows()


