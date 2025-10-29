import streamlit as st
import pickle

# Load model and vectorizer
spam_model = pickle.load(open("finalized_model.sav", "rb"))
tfidf = pickle.load(open("tfidf.sav", "rb"))  # make sure you saved it too!

# Streamlit UI
st.set_page_config(page_title="SMS Spam Detector", page_icon="📩", layout="centered")
st.title("📩 SMS Spam Detector")
st.markdown("### Enter your message below to check if it’s spam:")

# Input text box
user_input = st.text_area("Your message:", height=150)

# Button
if st.button("Check Spam"):
    if user_input.strip() == "":
        st.warning("Please enter a message first!")
    else:
        result = spam_model.predict(tfidf.transform([user_input]))[0]
        if result == 1:
            st.error("🚫 The message is **SPAM**")
        else:
            st.success("✅ The message is **NOT SPAM**")

st.markdown("____")
# st.caption("Built with Streamlit and scikit-learn 💻")
