# 🏷️ Multi-Modal Annotation Suite (Streamlit + Whisper)
A unified, Streamlit-based annotation platform for image, text, and audio data — designed for machine learning and NLP projects.
Includes Whisper-based audio transcription and manual labeling support.

📌 Features
1️⃣ Image Annotation (Streamlit)
Upload and view images

Select labels from dropdown or text input

Save annotated data to CSV/JSON

Basic bounding box support (optional)

2️⃣ Text Annotation (Streamlit)
Upload plain text or CSV files

Label sentences or paragraphs

Multi-label or single-label support

Export labeled text data

3️⃣ Audio Annotation + Transcription (Streamlit + Whisper)
Upload .wav, .mp3, etc.

Transcribe audio using OpenAI Whisper

Manually label transcripts (e.g., speaker intent, emotion)

Save transcripts + labels to CSV/JSON

📁 Final Project Structure
python
Copy
Edit
annotation-suite/
│
├── text_annotation/
│   ├── app.py                  # Streamlit app for text annotation
│   ├── sample_text.txt         # Example input file
│   └── output/                 # Labeled text output (CSV/JSON)
│
├── image_annotation/
│   ├── app.py                  # Streamlit app for image annotation
│   ├── images.zip              # Zipped folder of image samples
│   └── output/                 # Labeled image data
│
├── audio_transcribing_annotation/
│   ├── app.py                  # Streamlit app for audio transcription + labeling
│   ├── audios/                 # Folder with input .wav/.mp3 files
│   └── output/       

🤖 Whisper Integration
The audio annotation module uses OpenAI Whisper to transcribe audio before presenting the text for manual labeling.

✅ Supports:

English and multilingual audio

MP3, WAV, M4A, etc.

📌 Use Cases
Dataset labeling for supervised learning

Audio NLP projects (e.g., intent detection)

Image classification or bounding-box tasks

Building corpora for custom models

📣 Coming Soon
Bounding box drawing for image labeling

Multi-user label versioning

Label validation and confidence scoring

Integration with HuggingFace datasets or S3

📬 Contributions & Feedback
Feel free to open issues or PRs for:

Bug fixes

New annotation features

UI improvements
