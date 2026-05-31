import tensorflow as tf
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.utils import image_dataset_from_directory
from keras.layers import Rescaling

train_path = "dataset/train"
valid_path = "dataset/valid"

train_data = image_dataset_from_directory(
    train_path,
    image_size=(128, 128),
    batch_size=32,
    label_mode="categorical"
)

valid_data = image_dataset_from_directory(
    valid_path,
    image_size=(128, 128),
    batch_size=32,
    label_mode="categorical"
)

model = Sequential([
    Rescaling(1./255, input_shape=(128, 128, 3)), 
    Conv2D(32, (3, 3), activation="relu"),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation="relu"),
    MaxPooling2D(2, 2),
    Conv2D(128, (3, 3), activation="relu"),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(128, activation="relu"),
    Dropout(0.5),
    Dense(53, activation="softmax")
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