# Import Library
import streamlit as st
import pandas as pd
import numpy as np
import re
import nltk

# Machine Learning & Deep Learning
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
import tensorflow_hub as hub
from tensorflow_hub.keras_layer import KerasLayer

# NLP (Natural Language Processing)
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Unduh resource yang diperlukan
nltk.download('punkt_tab')
nltk.download('stopwords')

# Load stopwords untuk Bahasa Indonesia
stpwds_id = set(stopwords.words('indonesian'))

# Fungsi preprocessing teks
def text_preprocessing(text):
    # Case folding
    text = text.lower()
    
    # Menghapus mention (@username) dan hashtag
    text = re.sub(r"@[A-Za-z0-9_]+", " ", text)
    text = re.sub(r"#[A-Za-z0-9_]+", " ", text)
    
    # Menghapus newline (\n)
    text = re.sub(r"\\n", " ", text)
    
    # Menghapus whitespace di awal & akhir
    text = text.strip()
    
    # Menghapus URL
    text = re.sub(r"http\S+|www.\S+", " ", text)
    
    # Menghapus karakter non-huruf
    text = re.sub(r"[^A-Za-z\s']", " ", text)
    
    # Tokenisasi
    tokens = word_tokenize(text)
    
    # Menghapus stopwords
    tokens = [word for word in tokens if word not in stpwds_id]
    
    # Menggabungkan kembali token menjadi teks
    return ' '.join(tokens)

# Fungsi utama untuk aplikasi Streamlit
def run():
    st.markdown(
        """
        <h1 style='text-align: center; margin-bottom: 20px;'>Sentiment Analysis Tool</h1>
        <hr style="border: 1px solid #ccc;">
        """,
        unsafe_allow_html=True
    )

    # Input text
    user_input = st.text_area("Masukkan teks untuk analisis sentimen:", height=150)

    if st.button('Analyze Sentiment'):
        if user_input.strip():  
            # Load model
            model = load_model('sentiment_model.h5', custom_objects={'KerasLayer': KerasLayer})

            # Preprocessing input text
            processed_text = text_preprocessing(user_input)

            # Prediksi sentimen
            prediction = model.predict([[processed_text]])
            sentiment = "Positive" if prediction[0] > 0.5 else "Negative"
            sentiment_color = 'green' if prediction[0] > 0.5 else 'red'

            # Menampilkan hasil prediksi
            st.markdown(
                f"""
                <hr style="border: 1px solid #ccc;">
                <h3 style="text-align: center;">Sentiment Result: 
                <span style="color: {sentiment_color}; font-weight: bold;">{sentiment}</span></h3>
                <hr style="border: 1px solid #ccc;">
                """, 
                unsafe_allow_html=True)
        else:
            st.warning("Please enter some text before analyzing.")


# Menjalankan aplikasi
if __name__ == "__main__":
    run()
