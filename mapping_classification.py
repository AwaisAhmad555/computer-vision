import tensorflow as tf
import os
import cv2 as openCV
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plot
import pickle

training_dataset = []


def model(x_train,y_train,number_of_classes):

    model = tf.keras.models.Sequential()
    #model.add(tf.keras.layers.Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', input_shape=(200, 200, 3)))
    #model.add(tf.keras.layers.MaxPooling2D((2, 2)))
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(512, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(512, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(512, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(number_of_classes,activation=tf.nn.softmax))

    model.compile(optimizer="adam",
              loss="sparse_categorical_crossentropy" ,
              metrics=["accuracy"]
              )

    model.fit(x_train, y_train , epochs=10)

    val_loss , val_accuracy = model.evaluate(x_train,y_train)

    print("loss : ",val_loss,"Accuracy : ", val_accuracy)

    model.save("my_work.model")

    return 0

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



root_folder = "dataset"

words_classes = os.listdir(root_folder)

for folder in words_classes:

    current_path = os.path.join(root_folder,folder)

    if os.path.isfile(current_path):

        #print(folder + " is a file")

        pass

    else:

        #print(folder + " is a folder")

        words_classes = len(os.listdir(current_path))

        for single_class in os.listdir(current_path):

            """
            print()
            print(int(single_class))
            print()
            """

            image_label = int(single_class)

            images_path = os.path.join(current_path,single_class)

            image_names = os.listdir(images_path)

            #print(image_names)

            for idx,single_image_name in enumerate(image_names):

                image_full_path = os.path.join(images_path, single_image_name)

                """
                print()
                print(image_full_path)
                print()
                """


                word_image = openCV.imread(image_full_path)

                training_dataset.append([image_label,word_image])

                #openCV.imshow("1"+str(idx),word_image)

                pass



        pass


    pass

random.shuffle(training_dataset)

"""
print(np.array(training_dataset)[:,0])

image = np.array(training_dataset)[0,1]

print(image)

openCV.imshow(""+ str(np.array(training_dataset)[0,0]),image)
"""


#x_train = np.array(training_dataset)[:,1]
#y_train = np.array(training_dataset)[:,0]

x_train = []
y_train = []

for img_label,img in training_dataset:

    y_train.append(img_label)
    x_train.append(img)


    pass


#x_train = x_train/255

#print(y_train)

print()

print(len(x_train))
print()
print(len(y_train))
print()

x_train = np.array(x_train)
y_train = np.array(y_train)

#print(x_train[0:5])

print()

#print(y_train)

pickle.dump(x_train,open("X.pkl","wb"))

pickle.dump(y_train,open("Y.pkl","wb"))

print()


X = pickle.load(open("X.pkl","rb"))

Y = pickle.load(open("Y.pkl","rb"))

print(X.shape)


#model(x_train=X,y_train=Y,number_of_classes=words_classes)



###############model prediction on segmented images##############


segment_images_path = r"sample_2\segment_images"

segment_images = os.listdir(segment_images_path)

img_list = []

for images_name in segment_images:

    single_segment_image_path = os.path.join(segment_images_path,images_name)

    segment_img = openCV.imread(single_segment_image_path)

    img_list.append(segment_img)

    #openCV.imshow(images_name,segment_img)

    pass

prediction_function(x_train=X,y_train=Y,train_index=12)


openCV.waitKey(0)
openCV.destroyAllWindows()
