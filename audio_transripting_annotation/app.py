import streamlit as st
import whisper
import pandas as pd
import tempfile
import os
import subprocess


def get_ffmpeg_version():
    try:
        result = subprocess.run(["ffmpeg", "-version"],
                                capture_output=True, text=True, check=True)
        version_line = result.stdout.splitlines()[0]
        return version_line
    except FileNotFoundError:
        return "FFmpeg is not installed or not in PATH."
    except Exception as e:
        return f"Error checking FFmpeg version: {e}"


st.sidebar.markdown("### Environment Info")
st.sidebar.text(f"FFmpeg: {get_ffmpeg_version()}")

st.title("Audio Transcription + Annotation")

model = whisper.load_model("base")

uploaded_files = st.file_uploader(
    "Upload audio files", type=["mp3", "wav", "m4a"], accept_multiple_files=True
)

if uploaded_files:
    labels = st.multiselect(
        "Select or define labels",
        ["Arabic", "English", "Korean", "Positive",
            "Negative", "Neutral", "Male", "Female"]
    )

    annotations = []

    for audio_file in uploaded_files:
        st.audio(audio_file)

        suffix = os.path.splitext(audio_file.name)[1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp_audio:
            tmp_audio.write(audio_file.read())
            tmp_path = tmp_audio.name

        try:
            result = model.transcribe(tmp_path)
            transcript = result["text"]
        except Exception as e:
            transcript = f"[Error during transcription: {e}]"

        st.markdown(f"*Transcript:* {transcript}")
        label = st.selectbox(
            f"Label for {audio_file.name}", labels, key=audio_file.name)

        annotations.append({
            "filename": audio_file.name,
            "transcript": transcript,
            "label": label
        })

    if st.button("Download Annotated Transcripts"):
        df = pd.DataFrame(annotations)
        st.download_button(
            label="Download CSV",
            data=df.to_csv(index=False).encode("utf-8"),
            file_name="transcribed_annotations.csv",
            mime="text/csv"
        )
