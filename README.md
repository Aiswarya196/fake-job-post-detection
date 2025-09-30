🕵️ Fake HR Job Posting Detection

A Machine Learning + NLP project that detects whether a job posting is real or fake.
Built to showcase practical Data Science, NLP, and Streamlit app deployment skills.

🚀 Overview

Fake job postings are a growing problem on online job portals, leading to scams and data theft.
This project demonstrates how Natural Language Processing (NLP) and Machine Learning can be applied to detect fraudulent job ads.

Dataset: Fake Job Postings Dataset (Kaggle)

Size: ~18,000 job postings (real + fake)

The project includes:

Data Preprocessing & Cleaning (stopwords, stemming, text normalization).

Feature Engineering using TF-IDF Vectorization.

Classification Model using Logistic Regression.

Model evaluation

Visualizations and insights

Interactive Web App built with Streamlit for live predictions.

✨ Features

Input any job posting text and get instant prediction (Real ✅ or Fake 🚨).

Clean UI with professional design and styled buttons.

Inline + Toast-style prediction messages.

Reusable code structure with saved model (.pkl files).

🛠️ Tech Stack

Language: Python 🐍

Libraries: pandas, numpy, scikit-learn, nltk, matplotlib, seaborn, wordcloud

Vectorization: TfidfVectorizer

Model: Logistic Regression

Deployment/UI: Streamlit

📂 Project Structure
fake-hr-post-detection/
│── app/
│   └── app.py          # Streamlit app
│── data/
│   └── fake_job_postings.csv
│── notebooks/
│   ├── EDA.ipynb  # Model training and EDA
│   ├── model.pkl       # Saved trained model
│   └── vectorizer.pkl  # Saved TF-IDF vectorizer
│── requirements.txt
│── README.md

⚡ Quick Start

1️⃣ Clone this repo:

git clone https://github.com/your-username/fake-hr-post-detection.git
cd fake-hr-post-detection


2️⃣ Install dependencies:

pip install -r requirements.txt


3️⃣ Run the app:

streamlit run app/app.py

📈 Model Evaluation & Insights

To ensure the model is reliable, I performed both quantitative evaluation and visual exploratory analysis.

✅ Evaluation Metric

Accuracy Score → Baseline performance measure for classification.


📊 Visual Insights

Class Distribution (Bar Chart) → Highlights dataset imbalance, critical for interpreting metrics.

WordClouds (Real vs. Fake) → Quick visual of most frequent words in each class.

Top-N Words (Bar Plot with CountVectorizer) → Shows dominant keywords driving classification.

Text Length Distribution by Label → Fake job posts often shorter/longer than real ones.

Most Informative Features (Logistic Regression Coefficients with TF-IDF) → Identifies which words strongly indicate “fake” or “real”.

ROC & Precision-Recall Curves → Deeper model performance evaluation beyond accuracy, especially for imbalanced datasets.

These insights helped in:

Understanding how scammers phrase fake jobs.

Identifying potential improvements like balancing classes or enriching features.

Presenting results in a clear, stakeholder-friendly way.

🎯 Example Predictions

🔹 Real Job Post:

"We are hiring a Data Analyst in Bangalore with 1+ years of experience. Strong SQL/Python skills required."
✅ Model Output: Real

🔹 Fake Job Post:

"Work from home, no experience needed, earn $500 daily. Just send your personal details to our HR email."
🚨 Model Output: Fake

📊 Skills Demonstrated

End-to-End Machine Learning Pipeline

Text Preprocessing & NLP

Model Deployment using Streamlit

Data Visualization with Seaborn & WordCloud

Version Control & GitHub Documentation

End-to-End ML Project Ownership (data cleaning → model training → evaluation → deployment → documentation)g

📸 Screenshots


💼 About Me

I’m Aiswarya P V, a passionate Data Analytics enthusiast with a background in Computer Science.
I enjoy working on real-world projects that combine data, problem-solving, and visualization to deliver insights.
🔗 LinkedIn Profile