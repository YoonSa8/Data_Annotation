import streamlit as st
import pandas as pd


st.title("Text Classification Labeler")

uploaded_file = st.file_uploader(
    "Upload CSV file with a text column", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    if "text" not in df.columns:
        st.error("CSV must have a 'text' column ")
    else:
        if "lable" not in df.columns:
            df["label"] = ""
        labels = ["Positive", "Negative", "Neutral"]

        for i in range(len(df)):
            st.markdown(f'Text {i+1}: {df.loc[i, "text"]}')
            df.at[i, "label"] = st.selectbox(
                f'Label for text {i+1}', labels, key=i)
        st.subheader("preview Labeled Data")
        st.dataframe(df)
        if st.button("Download Labeled CSV"):
            st.download_button(label="dowload", data=df.to_csv(index=False).encode("utf-8"),
                               file_name="labeled_data.csv", mime="text/csv")
