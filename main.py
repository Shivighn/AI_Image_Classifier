import streamlit as st
from keras.models import load_model
from PIL import Image
import numpy as np

from util import classify, set_background


set_background('./bgs/bg.png')

# set title
st.title('AI Image Classifier')

# set header
st.header('Please upload an image')

# upload file
file = st.file_uploader('', type=['jpeg', 'jpg', 'png'])

# load classifier
model = load_model('./Models/Imageclassifier4.h5')

# display image
if file is not None:
    image = Image.open(file).convert('RGB')
    st.image(image, use_column_width=True)

    # classify image
    conf_score = classify(image, model)

    # write classification
    
    if(conf_score <0.5):
        st.write(f"##AI-Generated image")
    else:
        st.write(f"##Real Image")

