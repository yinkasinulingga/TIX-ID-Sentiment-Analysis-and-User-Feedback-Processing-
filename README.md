
---

# **TIX ID: Analisis Sentimen dan Umpan Balik Pengguna**  

## **Tujuan Proyek**  
Proyek ini bertujuan untuk membangun **model analisis sentimen** menggunakan **Natural Language Processing (NLP)**. Model ini dilatih menggunakan ulasan aplikasi **TIX ID** untuk mengklasifikasikan sentimen pengguna, membantu bisnis memahami umpan balik pelanggan dan meningkatkan layanan.  

## **Tahapan Proyek**  
1. **Pengumpulan Data**: Menggunakan dataset ulasan pengguna dari TIX ID (Kaggle).  
2. **Pemrosesan Data**: Tokenisasi, penghapusan stopword, stemming, dan vektorisasi menggunakan TF-IDF.  
3. **Pelatihan Model**: Menerapkan **Artificial Neural Network (ANN)** menggunakan **TensorFlow & Keras**.  
4. **Evaluasi Model**: Mengukur performa dengan **akurasi, presisi, recall, dan F1-score**.  
5. **Deploy Model**: Model yang telah dilatih diunggah dan dijalankan melalui Hugging Face Spaces.  

## **Teknologi yang Digunakan**  
- **Pemrograman & Framework**: Python, TensorFlow, Keras, Scikit-learn, Pandas, NumPy  
- **Pemrosesan Data**: NLTK, Sastrawi, WordCloud, TF-IDF  
- **Visualisasi Data**: Matplotlib, Seaborn  
- **Deploy Model**: Hugging Face, Flask, Streamlit  

## **File Proyek**  
`Modeling.ipynb` → Pemrosesan data, pelatihan model, dan evaluasi  
`Model_Inference.ipynb` → Inferensi model pada data baru  
`Deployments/` : Folder deployment menggunakan Hugging Face  
`url.txt` → Berisi tautan ke dataset, model, dan hasil deploy  

## **Tautan Penting**  
- **Dataset**: [TIX ID Reviews - Kaggle](https://www.kaggle.com/code/devraai/tix-id-app-review-sentiment-and-eda#Sentiment-Analysis)  
- **Model**: [Google Drive - Sentiment Model](https://drive.google.com/file/d/1fZ0w0ED6SfgGNogdM9MD7exm_r1p5-iY/view?usp=sharing)  
- **Deploy Model**: [Hugging Face - Sentiment Analysis App](https://huggingface.co/spaces/yinkasinulingga/Sentiment-Analysis-App)  

## **Kesimpulan**  
- **Analisis sentimen membantu memahami kepuasan pengguna** → Dengan model NLP, TIX ID dapat mengidentifikasi pola ulasan positif dan negatif secara efisien.  
- **Peningkatan layanan berbasis data** → Hasil analisis dapat digunakan untuk memperbaiki fitur aplikasi yang sering dikritik oleh pengguna.  
- **Akurasi model cukup baik** → Model ANN yang digunakan menunjukkan performa optimal dalam mengklasifikasikan sentimen ulasan pengguna.  

## **Saran untuk Pengembangan Selanjutnya**  
- **Meningkatkan akurasi model** → Mencoba arsitektur deep learning lain seperti LSTM atau BERT untuk meningkatkan klasifikasi sentimen.  
- **Menambahkan aspek analisis aspek-sentimen** → Mengidentifikasi bagian spesifik dari aplikasi yang sering dikritik atau dipuji.  
- **Integrasi dengan sistem rekomendasi** → Menggunakan hasil analisis untuk memberikan rekomendasi konten atau promosi yang lebih personal bagi pengguna.  

## **Dampak Bisnis**  
- **Meningkatkan pengalaman pelanggan** → Analisis sentimen membantu TIX ID memahami kepuasan pengguna dan memperbaiki layanan berdasarkan feedback negatif.  
- **Optimasi strategi pemasaran** → Mengidentifikasi tren ulasan positif dan negatif memungkinkan perusahaan menargetkan promosi dengan lebih tepat.  
- **Pengelolaan reputasi lebih baik** → Dengan memahami pola keluhan pelanggan, perusahaan dapat segera mengambil tindakan untuk meningkatkan layanan.  
- **Peningkatan loyalitas pelanggan** → Dengan merespons umpan balik secara cepat dan akurat, kepuasan pengguna meningkat sehingga mereka lebih cenderung menggunakan layanan TIX ID kembali.  

## **Kontak**  
Jika ada pertanyaan atau saran terkait proyek ini, silakan hubungi:  
**Email**: yinkasinulingga@gmail.com  

---

