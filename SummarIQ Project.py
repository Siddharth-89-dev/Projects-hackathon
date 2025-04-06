import streamlit as st
import wikipedia
from deep_translator import GoogleTranslator
import base64
import streamlit.components.v1 as components

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
summary = ""
topic = st.text_input("🔍 Enter a topic:")

# Summarize Button
if st.button("📄 Summarize"):
    if topic:
        try:
            summary = wikipedia.summary(topic, sentences=3)
            st.success(summary)
        except wikipedia.exceptions.DisambiguationError as e:
            st.error(f"Be more specific. Suggestions: {e.options[:5]}")
        except wikipedia.exceptions.PageError:
            st.error("❌ Topic not found. Please check spelling.")
        except Exception as e:
            st.error(f"⚠️ Unexpected error: {str(e)}")
    else:
        st.warning("Please enter a topic to summarize.")

# TTS Button using browser (safe version)
if summary:
    if st.button("🔊 Listen"):
        safe_summary = summary.replace('"', '\\"')
        tts_code = f'''
        <script>
            var msg = new SpeechSynthesisUtterance("{safe_summary}");
            window.speechSynthesis.speak(msg);
        </script>
        '''
        components.html(tts_code)

# Language selection and translation
languages = {
    "Hindi": "hi",
    "Spanish": "es",
    "French": "fr",
    "Tamil": "ta",
    "Bengali": "bn"
}
language = st.selectbox("🌐 Choose translation language", list(languages.keys()))

if summary:
    if st.button("🌍 Translate"):
        try:
            translated_text = GoogleTranslator(source='auto', target=languages[language]).translate(summary)
            st.info(translated_text)
        except Exception as e:
            st.error(f"Translation failed: {str(e)}")

# Download Button
if summary:
    if st.button("💾 Download as TXT"):
        try:
            b64 = base64.b64encode(summary.encode()).decode()
            href = f'<a href="data:file/txt;base64,{b64}" download="summary.txt">Click to download</a>'
            st.markdown(href, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Download failed: {str(e)}")

# Footer
st.markdown("""
---
Made with ❤️ by Siddharth Vishwakarma
""")
