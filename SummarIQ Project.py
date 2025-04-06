import streamlit as st
import wikipedia==1.4.0
import pyttsx3
from googletrans import Translator
import base64

# Set up page config
st.set_page_config(page_title="SummarIQ", page_icon="🧠", layout="centered")

# Custom CSS for style
st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
        }
        .stButton>button {
            color: white;
            background-color: #4CAF50;
            border-radius: 10px;
            padding: 10px 20px;
            font-size: 16px;
            transition: background-color 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .title {
            font-size: 40px;
            font-weight: 700;
            color: #333;
        }
        .subtitle {
            font-size: 20px;
            color: #666;
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='title'>🧠 SummarIQ</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Summarize smarter. Learn faster.</div>", unsafe_allow_html=True)

# Input section
topic = st.text_input("🔍 Enter a topic:")
translator = Translator()
summary = ""

# Summarize Button
if st.button("📄 Summarize"):
    try:
        summary = wikipedia.summary(topic, sentences=3)
        st.success(summary)
    except wikipedia.exceptions.DisambiguationError as e:
        st.error(f"Be more specific. Suggestions: {e.options[:5]}")
    except wikipedia.exceptions.PageError:
        st.error("Topic not found.")

# TTS Button
if summary and st.button("🔊 Listen"):
    engine = pyttsx3.init()
    engine.say(summary)
    engine.runAndWait()

# Translate Button
if summary and st.button("🌐 Translate to Hindi"):
    translated = translator.translate(summary, dest='hi')
    st.info(translated.text)

# Download Button
if summary and st.button("💾 Download as TXT"):
    b64 = base64.b64encode(summary.encode()).decode()
    href = f'<a href="data:file/txt;base64,{b64}" download="summary.txt">Click to download</a>'
    st.markdown(href, unsafe_allow_html=True)

# Footer
st.markdown("""
---
Made with ❤️ by Siddharth Sharma
""")
