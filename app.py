import streamlit as st

st.set_page_config(page_title="Nas Galaxy AI 🌌", page_icon="🌌", layout="wide")

st.markdown("<h1 style='text-align:center;color:#6C63FF;'>🌌 Nas Galaxy AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;font-size:18px;'>Emotional support and programming help — fast, simple, reliable.</p>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["💙 Emotional Support", "💻 Programming Help"])

with tab1:
    st.subheader("Share your thoughts 💭")
    text = st.text_area("What's on your mind?", height=160)
    if st.button("Get Support"):
        if text.strip():
            # Lightweight placeholder logic (no heavy ML)
            st.success("✨ Here's some perspective:")
            st.write("I hear you. Try breaking your morning into small steps: identify one tiny task, "
                     "do it for 5 minutes, then reassess. If you feel stuck, write down three options, "
                     "pick the easiest, and act. You’ve got this.")
        else:
            st.warning("Please enter something to talk about.")

with tab2:
    st.subheader("Ask your programming question 👨‍💻")
    question = st.text_area("Describe your problem:", height=120)
    code = st.text_area("Optional: paste code or error message", height=160)
    if st.button("Get Code Help"):
        if question.strip():
            st.success("💡 Suggested approach:")
            st.write("- Clarify expected vs actual output\n"
                     "- Add a minimal reproducible example\n"
                     "- Log inputs and check types\n"
                     "- Write a small test to lock the fix")
            if code.strip():
                st.code(code, language="python")
        else:
            st.warning("Please enter a programming question.")
