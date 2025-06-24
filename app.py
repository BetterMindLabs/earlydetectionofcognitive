import streamlit as st
import google.generativeai as genai

# === Gemini Setup ===
api_key = st.secrets["api_keys"]["google_api_key"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# === UI Setup ===
st.set_page_config(page_title="🧠 Cognitive Health Screener")
st.title("🧠 Early Detection of Cognitive Disorders")
st.write("Adjust the parameters below to assess the likelihood of early cognitive disorders. This tool is not diagnostic.")

# === Input Sliders ===
memory_loss = st.slider("🧠 Memory Issues (1 = none, 10 = severe)", 1, 10, 3)
confusion_freq = st.slider("🔁 Confusion/Disorientation Frequency", 1, 10, 4)
attention_span = st.slider("📍 Attention Span (1 = poor, 10 = excellent)", 1, 10, 6)
language_difficulty = st.slider("🗣️ Language Difficulty (1 = none, 10 = severe)", 1, 10, 2)
daily_task_difficulty = st.slider("🧹 Difficulty with Daily Tasks", 1, 10, 3)
mood_swings = st.slider("🎭 Mood Swings", 1, 10, 5)
family_history = st.selectbox("🧬 Family History of Cognitive Disorders?", ["No", "Yes"])

# === Predict Button ===
if st.button("Assess Cognitive Health"):
    with st.spinner("Analyzing cognitive pattern..."):
        prompt = f"""
You are a cognitive health screener trained to flag early signs of disorders like Alzheimer's or MCI (Mild Cognitive Impairment).

Based on these user inputs:
- Memory Issues: {memory_loss}/10
- Confusion Frequency: {confusion_freq}/10
- Attention Span: {attention_span}/10
- Language Difficulty: {language_difficulty}/10
- Difficulty with Daily Tasks: {daily_task_difficulty}/10
- Mood Swings: {mood_swings}/10
- Family History: {family_history}

Respond in this format:
Risk Level: <Low | Moderate | High>  
Comment: <1-line observation>  
Recommendation: <1-line next step, e.g., consult doctor, track symptoms, etc.>
"""

        response = model.generate_content(prompt)
        result = response.text.strip()

        st.subheader("🧠 Cognitive Screening Result")
        st.text(result)
