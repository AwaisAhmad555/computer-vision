import tensorflow as tf
import keras

from keras import Sequential
from keras.layers import Dense, Input




model = Sequential()


model.add(Input(shape=(10000)))
model.add(Dense(units=100,activation='relu',kernel_initializer='he_uniform'))
model.add(Dense(units=100,activation='relu',kernel_initializer='he_uniform'))
model.add(Dense(units=10,activation='softmax'))

print(model.summary())