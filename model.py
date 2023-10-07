import cv2
from PIL import Image, ImageOps
import numpy as np
from tensorflow.keras import datasets, layers, models


def load_model():
    model_path = "C:/Users/Rampraveen/Project_1/knee_564.00.h5"
    model = models.load_model(model_path)
    return model


model = load_model()


def upload_predict(upload_image):
    image = ImageOps.fit(upload_image, (224, 224), Image.ANTIALIAS)
    num_channels = np.asarray(image).shape[-1]
    image = np.asarray(image)
    if num_channels == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    size = (224, 224)
    print(image)
    img_resize = cv2.resize(image, dsize=size, interpolation=cv2.INTER_CUBIC)
    img_reshape = np.expand_dims(np.expand_dims(img_resize, 0), 3)
    print(img_reshape.shape)
    prediction = model.predict(img_reshape)
    print(prediction)
    class_labels = ["Normal", "Doubtful", "Mild", "Moderate", "Severe"]
    predicted_class = class_labels[np.argmax(prediction)]
    similarity_score = prediction[0][np.argmax(prediction)]
    return predicted_class, similarity_score
