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
from features_extraction import *
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

################################################################

def load_images_dataset(path):

    upti_images = os.listdir(path=path)

    upti_images = sorted(upti_images,key=lambda a:int(a.split(".")[0]))

    dataset_list = []

    for idx,image in enumerate(upti_images):

        folder_name = str(image)

        image_path = os.path.join(path, image)

        label = int(folder_name.split(".")[0])

        img = openCV.imread(image_path)

        img = openCV.cvtColor(img, openCV.COLOR_RGB2GRAY, None)

        thresh, img = openCV.threshold(img, 200, 255, openCV.THRESH_BINARY, None)

        new_crop_image = cut_extra_height(img=img)

        custom_features = get_features(new_crop_image)

        dataset_list.append([label, custom_features])


        pass




    return dataset_list
    pass



full_path = 'upti\\training dataset'


dataset_list = load_images_dataset(path=full_path)

random.shuffle(dataset_list)


custom_features_dataset = pickle.dump(dataset_list,open("upti\\upti_custom_features_dataset.pkl", "wb"))

dataset_list = pickle.load(open("upti\\upti_custom_features_dataset.pkl", "rb"))

print(len(dataset_list))


#classifier = svm.SVC(kernel='rbf', gamma=10.005, C=100)

classifier = svm.SVC(kernel='rbf', gamma=10.005, C=100)



array_new = np.array(dataset_list)

print("shape : ")
print(len(array_new[:,:]))
print()

#Data
X = array_new[:,1].tolist()

#Label
Y = array_new[:,0].tolist()


classifier.fit(X=X,y=Y)


filename = 'upti\\upti_custom_features_model.sav'
pickle.dump(classifier, open(filename, 'wb'))


print(classifier)

sample_array = array_new[:,1].tolist()
test_labels = array_new[:,0].tolist()

samples = sample_array[0:]

lables = test_labels[0:]

print()

#print(samples)
print()

print("testing samples labels = ")
print(lables)

result = classifier.predict(samples)

print(result.tolist())

#print()


#print(confusion_matrix(lables, result))
#print(classification_report(lables, result))

#print()
print()
print(classifier.score(samples,lables))

"""for i in range(len(lables)):

    if lables[i] != result[i]:

        print("Not matching ! ")

        print()

        print("label : " + str(lables[i]))

        print()

        print("prediction : " + str(result[i]))


        pass


    pass"""




"""openCV.waitKey(0)
openCV.destroyAllWindows()"""