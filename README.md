📱 SMS Spam Classifier

This project is a Machine Learning-based SMS Spam Classifier that predicts whether a given text message is Spam or Not Spam. It comes with an interactive Streamlit web app that allows users to easily test messages in real time.

🌐 Live Demo: Click here to try it out!

🚀 Project Overview

Have you ever wondered if a message is spam or genuine?
This project uses a Random Forest Classifier trained on labeled SMS data to automatically classify messages.
Just type any message into the input box — the model will instantly tell you if it’s spam or ham (not spam).

🧠 Tech Stack

Python 🐍

Streamlit – for building the web UI

Scikit-learn – for model training and evaluation

Random Forest Classifier – as the ML algorithm

Pandas & NumPy – for data preprocessing and handling

⚙️ How It Works

The user enters an SMS or text message in the Streamlit app.

The message is preprocessed (cleaning, tokenizing, etc.).

The trained Random Forest model analyzes the input.

The result is displayed: ✅ Not Spam or 🚫 Spam.

🖥️ Installation & Setup

To run this project locally:

# Clone the repository
git clone https://github.com/Moin36532/SMS_Spam_Classifier.git

# Navigate into the project folder
cd SMS_Spam_Classifier

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py


Then open your browser and go to:
👉 http://localhost:8501/

📸 Live Demo

Try it online without installation!
👉 https://sms-spam-classifier325.streamlit.app/
