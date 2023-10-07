import base64

import cv2
import numpy as np
import streamlit as st
from PIL import Image, ImageOps
from tensorflow.keras import models

from chat import chatbot


@st.cache_resource
def load_model():
    model_path = "C:/Users/Rampraveen/Project_1/knee_564.00.h5"
    model = models.load_model(model_path)
    return model


def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_png_as_page_bg(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-color: rgb(214,123,255);
    background-size: cover;
    background-attachment: scroll; # doesn't work
    }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return


# set_png_as_page_bg('background.mp4')

with st.spinner('Model is being loaded..'):
    model = load_model()

file = st.file_uploader(label=":orange[Upload the image to be classified]", type=["jpg", "png"])
st.set_option('deprecation.showfileUploaderEncoding', False)


def upload_predict(upload_image, model):
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


prompt = st.chat_input("Say something")
if prompt:
    st.write(chatbot.respond(prompt))
if file is None:
    if prompt:
        st.write(chatbot.respond(prompt))
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    predictions = upload_predict(image, model)
    image_class = predictions[0]
    score = predictions[1]
    st.write("The image is classified as", image_class)
    st.write("The similarity score is approximately", score)
    print("The image is classified as ", image_class, "with a similarity score of", score)
    if prompt:
        st.write(chatbot.respond(prompt))
