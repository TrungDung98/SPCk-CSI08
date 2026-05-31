import numpy as np
import os
from keras.models import load_model
from keras.utils import load_img, img_to_array

model = load_model("cards_model.keras")

class_names = sorted(os.listdir("dataset/train"))

def predict_card(img_path):
    img = load_img(
        img_path,
        target_size=(128, 128)
    )
    img_array = img_to_array(img)
    # img_array = img_array / 255.0
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

