import streamlit as st
import pyttsx3
import base64
from pydub import AudioSegment

# Set page title and icon
st.set_page_config(page_title="Text-to-Speech Converter", page_icon="🔊")

# Set page header
st.title("Text-to-Speech Converter")

# Object creation
engine = pyttsx3.init()

# Input choices for pyttsx3
with st.sidebar:
    st.subheader("Speech Settings")
    rate = st.slider("Select speaking rate", 50, 200, 125)
    volume = st.slider("Select volume level", 0.0, 1.0, 1.0)
    voice_gender = st.selectbox("Select voice", ("Male", "Female"))

# Setting up voice rate, volume, and gender
engine.setProperty('rate', rate)
engine.setProperty('volume', volume)
voices = engine.getProperty('voices')
if voice_gender == "Male":
    engine.setProperty('voice', voices[0].id)
else:
    engine.setProperty('voice', voices[1].id)

# Text input for conversion
text_input = st.text_input("Enter the text to convert to speech", "Hello, World!")

# Convert text to speech
if st.button("Convert"):
    engine.say(text_input)
    engine.runAndWait()

    # Convert the speech to an AudioSegment
    engine.save_to_file(text_input, 'output.wav')  # Save as WAV file
    engine.runAndWait()

    audio = AudioSegment.from_wav('output.wav')
    audio.export('output.mp3', format="mp3")

    # Display the saved audio file
    with open("output.mp3", "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        st.audio(data, format='audio/mp3', start_time=0)
