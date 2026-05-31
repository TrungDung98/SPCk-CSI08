from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

model = load_model("cards_model.h5")

class_names = sorted(
    os.listdir("dataset/train")
)

def predict_card(img_path):

    img = image.load_img(
        img_path,
        target_size=(128,128)
    )

    img_array = image.img_to_array(img)

    img_array = img_array / 255.0

    img_array = np.expand_dims(
        img_array,
        axis=0
    )

    prediction = model.predict(img_array)

    class_index = np.argmax(prediction)

    confidence = np.max(prediction)

    return (
        class_names[class_index],
        confidence
    )