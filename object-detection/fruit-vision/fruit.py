import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Conv2D , Dense,BatchNormalization,Dropout,Flatten,MaxPooling2D,GlobalAveragePooling2D
from tensorflow.keras.models import Sequential

import math
import numpy as np
import matplotlib.pyplot as plt
import logging
logger = tf.get_logger()
logger.setLevel(logging.ERROR)

train_data = keras.utils.image_dataset_from_directory(
    directory = "/kaggle/input/fruit-classification-dataset/Fruit_dataset/train1",
    labels = "inferred",
    label_mode = 'int',
    batch_size=32,
    image_size = (256,256),
)

val_data = keras.utils.image_dataset_from_directory(
    directory = "/kaggle/input/fruit-classification-dataset/Fruit_dataset/val1",
    labels = "inferred",
    label_mode = 'int',
    batch_size=32,
    image_size = (256,256),
)

test_data = keras.utils.image_dataset_from_directory(
    directory = "/kaggle/input/fruit-classification-dataset/Fruit_dataset/test1",
    labels = "inferred",
    label_mode = 'int',
    batch_size=32,
    image_size = (256,256),
)

def preprocess(image,label):
    image = tf.cast(image/255.0,tf.float32),
    return image,label
train_data_norm = train_data.map(preprocess)
val_data_norm =  val_data.map(preprocess)
test_data_norm = test_data.map(preprocess)

model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(filters=32,kernel_size=(3,3),input_shape=(256,256,3),activation=tf.nn.relu ,padding="same"),
    tf.keras.layers.MaxPooling2D((2,2), strides = 2),
    tf.keras.layers.Conv2D(filters=32,kernel_size=(3,3),activation=tf.nn.relu ,padding="same"),
    tf.keras.layers.MaxPooling2D((2,2), strides = 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128,activation="relu"),
    tf.keras.layers.Dense(100,activation="softmax")
])

model.compile(optimizer = 'adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

BATCH_SIZE = 32
train_data_norm = train_data_norm.cache().repeat()
val_data_norm = val_data_norm.cache()

model.fit(train_data_norm, epochs=10, steps_per_epoch=math.ceil(50000/BATCH_SIZE))