import streamlit as st
import joblib
import re
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

port_stem = PorterStemmer()
stop_words = set(stopwords.words('english'))

def preprocess_input(text):
    text = str(text).lower()
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'[^a-z\s]', '', text)
    words = text.split()
    words = [port_stem.stem(w) for w in words if w not in stop_words]
    return " ".join(words)

# List of red-flag words often found in fake jobs
fake_keywords = [
    'cash', 'bonus', 'earn', 'investment', 'bank', 'immediate', 
    'ninja', 'clients', 'free', 'urgent','comment yes','comment', 'Comment','24 hours'
]

def is_fake_boost(user_input):
    return any(word in user_input.lower() for word in fake_keywords)

# Load saved model & vectorizer
model = joblib.load(r"C:\Users\DELL\Desktop\fake-hr-post-detection\notebooks\model.pkl")
vectorizer = joblib.load(r"C:\Users\DELL\Desktop\fake-hr-post-detection\notebooks\vectorizer.pkl")


st.markdown("""
    <style>
   

    .stButton > button {
        background-color: #2E86C1; /* Blue */
        color: white;
        font-size: 18px;
        font-weight: bold;
        padding: 12px 30px;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        transition: 0.3s;
    }
    .stButton > button:hover {
        background-color: #1B4F72; /* Darker blue on hover */
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: #2E86C1;'>🕵️ Fake Job Posting Detector</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray; font-weight: bold'>Identify fraudulent HR job postings using AI</p>", unsafe_allow_html=True)
st.write("---")

st.markdown(" **Enter the job posting description below:**")
user_input = st.text_area("", height=300, placeholder="Paste the full job description here...")


if st.button("Predict"):
    if user_input.strip() != "":
        processed_input = preprocess_input(user_input)
        X_input = vectorizer.transform([processed_input])
        model_prediction = model.predict(X_input)[0]

        # Combine model prediction with keyword booster
        if model_prediction == 1 or is_fake_boost(user_input):
            st.toast("🚨 Fake Job Posting detected!", icon="⚠️")
        else:
            st.toast("✅ This looks like a Real Job Posting.", icon="🎉")


        if model_prediction == 1 or is_fake_boost(user_input):
            st.error("🚨 This looks like a **Fake Job Posting**")
        else:
            st.success("✅ This looks like a **Real Job Posting**")
    else:
        st.toast("⚠️ Please enter a job description!", icon="⚠️")
        st.warning("⚠️ Please enter a job description before clicking Predict.")