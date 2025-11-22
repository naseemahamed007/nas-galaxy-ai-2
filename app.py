import streamlit as st
import requests

st.set_page_config(page_title="Nas Galaxy AI", page_icon="🚀", layout="wide")

# UI Title
st.markdown("""
    <h1 style='text-align:center; font-size:48px; margin-bottom:0;'>
        🚀 NAS GALAXY AI
    </h1>
    <p style='text-align:center; font-size:20px; margin-top:0;'>
        Ultra-fast AI • Emotional Intelligence • Coding • Creativity
    </p>
""", unsafe_allow_html=True)

# Text input
prompt = st.text_area("💬 Ask anything to Nas Galaxy AI:", height=150)

# Button
if st.button("Generate 🚀"):
    if prompt.strip():
        with st.spinner("Galaxy thinking..."):
            API_URL = "https://api.siliconflow.cn/v1/chat/completions"
            API_KEY = st.secrets["API_KEY"]

            headers = {"Authorization": f"Bearer {API_KEY}"}
            data = {
                "model": "deepseek-ai/DeepSeek-V3",
                "messages": [{"role": "user", "content": prompt}]
            }

            response = requests.post(API_URL, json=data, headers=headers).json()

            st.subheader("🌌 Response:")
            st.write(response["choices"][0]["message"]["content"])
