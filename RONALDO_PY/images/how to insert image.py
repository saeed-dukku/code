import streamlit as st
from PIL import Image

# Load image (local path or URL)
image = Image.open("your_image.jpg")  # Replace with your file path

# Display image
st.image(image, caption="This is an example image", use_column_width=True)
