import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Flatten, Dense, Dropout

train_path = "dataset/train"
valid_path = "dataset/valid"

train_data = ImageDataGenerator(
    rescale=1./255
).flow_from_directory(
    train_path,
    target_size=(128,128),
    batch_size=32,
    class_mode="categorical"
)

valid_data = ImageDataGenerator(
    rescale=1./255
).flow_from_directory(
    valid_path,
    target_size=(128,128),
    batch_size=32,
    class_mode="categorical"
)

model = Sequential([
    Conv2D(32,(3,3),activation="relu",input_shape=(128,128,3)),
    MaxPooling2D(2,2),

    Conv2D(64,(3,3),activation="relu"),
    MaxPooling2D(2,2),

    Conv2D(128,(3,3),activation="relu"),
    MaxPooling2D(2,2),

    Flatten(),

    Dense(128,activation="relu"),
    Dropout(0.5),

    Dense(53,activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

history = model.fit(
    train_data,
    validation_data=valid_data,
    epochs=10
)

model.save("cards_model.h5")

print("Training Complete")