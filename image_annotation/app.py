import streamlit as st
import pandas as pd
import zipfile
import os
from PIL import Image
import tempfile

st.title("Image Annotation Tool")

uploaded_zip = st.file_uploader("Upload a .zip file of images", type="zip")

if uploaded_zip:
    temp_dir = tempfile.TemporaryDirectory()
    with zipfile.ZipFile(uploaded_zip, 'r') as zip_ref:
        zip_ref.extractall(temp_dir.name)

    image_files = [f for f in os.listdir(temp_dir.name) if f.endswith(('.png', '.jpg', '.jpeg'))]

    if not image_files:
        st.warning("No image files found in the zip.")
    else:
        st.success(f"Found {len(image_files)} image(s). Start annotating!")

        labels = st.multiselect("Enter possible classes (or select)", ["Cat", "Dog", "Car", "Other"])

        annotations = []

        for i, file_name in enumerate(image_files):
            img_path = os.path.join(temp_dir.name, file_name)
            img = Image.open(img_path)
            st.image(img, caption=f"Image {i+1}: {file_name}", use_column_width=True)
            label = st.selectbox(f"Label for {file_name}", labels, key=i)
            annotations.append({"image": file_name, "label": label})

        if st.button("Download Annotations"):
            df = pd.DataFrame(annotations)
            st.download_button(
                label="Download CSV",
                data=df.to_csv(index=False).encode("utf-8"),
                file_name="image_labels.csv",
                mime="text/csv"
            )