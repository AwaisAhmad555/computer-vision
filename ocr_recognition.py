import tensorflow as tf
import cv2 as openCV
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plot
#from mapping_classification import prediction_function


def prediction_function(x_train,y_train,train_index):

    new_model = tf.keras.models.load_model("my_work.model")

    new_model.summary()
    predictions = new_model.predict([x_train])

    print(predictions[train_index])
    print()
    predicted_number = np.argmax(predictions[train_index])

    print("label is : ", y_train[train_index])
    print()
    print("Predicted test data set Sample at index - '",train_index,"' is :", predicted_number)

    print()
    #print("Actual label : ", y_train[train_index]," ("+predicted_number+")")

    plot.imshow(x_train[train_index],cmap='binary')

    plot.xlabel(predicted_number,fontsize=36)

    plot.show()

    return 0

images_list = []
images_names = []
images_numbers = []

root_path = "sample_2\\segment_images"

all_images_names = os.listdir(root_path)

print(all_images_names)


for images_name in all_images_names:

    image_number = int (os.path.splitext(images_name)[0])
    print()
    print(image_number)
    print()

    images_numbers.append(image_number)


    image_path = os.path.join(root_path,images_name)

    images_names.append(image_path)

    pass


for names in images_names:


    img = openCV.imread(names)

    #img = openCV.resize(img,(100,100))

    img = np.array(img)

    print()
    print(img.shape)
    print()

    images_list.append(img)

    #images_list = np.array(images_list)

    print()
    print(names)
    print()


    pass

print()
print(images_numbers)

print()

#print(images_list[0:11])

print()

images_list = np.array(images_list)
images_numbers = np.array(images_numbers)

prediction_function(x_train=images_list,y_train=images_numbers,train_index=83)