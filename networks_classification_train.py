from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.utils import np_utils
from keras import backend as K
from keras.models import load_model
from tensorflow.keras.utils import to_categorical

import tensorflow as tf
import matplotlib.pyplot as plot

import os as os
import numpy as np


mnist = tf.keras.datasets.fashion_mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = tf.keras.utils.normalize(x_train)
x_test = tf.keras.utils.normalize(x_test)

names = ["T-shirt/top", "Trouser/pants", "Pullover shirt", "Dress", "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]


#print(to_categorical(y_train).shape)


#plot.imshow(x_train[7])

#plot.show()

def model(x_train,y_train):

    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(10,activation=tf.nn.softmax))

    model.compile(optimizer="adam",
              loss="sparse_categorical_crossentropy" ,
              metrics=["accuracy"]
              )

    model.fit(x_train, y_train , epochs=10)

    val_loss , val_accuracy = model.evaluate(x_test,y_test)

    print("loss : ",val_loss,"Accuracy : ", val_accuracy)

    model.save("fashion_mnist_cnn_model.model")

    return 0

def prediction_function(x_test,y_test,test_index):

    new_model = tf.keras.models.load_model("fashion_mnist_cnn_model.model")

    new_model.summary()
    predictions = new_model.predict([x_test])

    print(predictions[test_index])
    print()
    predicted_number = np.argmax(predictions[test_index])

    print("Predicted test data set Sample at index - '",test_index,"' is :", predicted_number)

    print()
    print("Actual label : ", y_test[test_index]," ("+names[predicted_number]+")")

    plot.imshow(x_test[test_index],cmap='binary')

    plot.xlabel(names[predicted_number],fontsize=36)

    plot.show()

    return 0


#model(x_train=x_train,y_train=y_train)

print(x_train[0:7])
#prediction_function(x_test=x_test,y_test = y_test,test_index=171)
