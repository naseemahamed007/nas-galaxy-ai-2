import streamlit as st
from transformers import pipeline

# Page setup
st.set_page_config(
    page_title="Nas Galaxy AI 🌌",
    page_icon="🌌",
    layout="wide"
)

# Title
st.markdown(
    "<h1 style='text-align: center; color: #6C63FF;'>🌌 Nas Galaxy AI</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center; font-size:18px;'>Your all-in-one AI companion for emotional support and programming help</p>",
    unsafe_allow_html=True
)

# Load AI models (you can swap these later for bigger ones)
summarizer = pipeline("summarization")
qa_model = pipeline("question-answering")

# Tabs for different modes
tab1, tab2 = st.tabs(["💙 Emotional Support", "💻 Programming Help"])

# Emotional Support Tab
with tab1:
    st.subheader("Share your thoughts 💭")
    support_input = st.text_area("What's on your mind?", height=150)

    if st.button("Get Support"):
        if support_input.strip():
            # Simple summarizer as placeholder for emotional support
            response = summarizer(support_input, max_length=60, min_length=20, do_sample=False)
            st.success("✨ Here's some perspective:")
            st.write(response[0]['summary_text'])
        else:
            st.warning("Please enter something to talk about.")

# Programming Help Tab
with tab2:
    st.subheader("Ask your programming question 👨‍💻")
    question = st.text_area("Describe your problem:", height=150)
    context = st.text_area("Optional: paste related code or error message", height=150)

    if st.button("Get Code Help"):
        if question.strip():
            # Placeholder QA model
            if context.strip():
                response = qa_model(question=question, context=context)
                st.success("💡 Suggested Answer:")
                st.write(response['answer'])
            else:
                st.info("Try pasting code or error message for better help.")
                st.write("Example solution:\n```python\nprint('Hello World')\n```")
        else:
            st.warning("Please enter a programming question.")
