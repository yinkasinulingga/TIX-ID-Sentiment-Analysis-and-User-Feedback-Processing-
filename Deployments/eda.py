# Import Library
# Streamlit untuk UI
import streamlit as st

# Data Manipulasi
import pandas as pd

# Visualisasi Data
import matplotlib.pyplot as plt
import plotly.express as px
from wordcloud import WordCloud


def run():
    st.write('')
    st.write('')
    st.markdown("""
        <h1 style='text-align: center;  margin-bottom: 20px;'>Exploratory Data Analysis</h1>
    """, unsafe_allow_html=True)

    st.write('___')
    # Load Data
    st.write('## Dataset')

    # Read the CSV file
    df = pd.read_csv('data_sentimen_TIX_ID.csv')

    # Display the data inside a container and center it
    with st.container():
        st.markdown('<h3 style="text-align: center;">Data Preview </h3>', unsafe_allow_html=True)
        st.dataframe(df, use_container_width=True)  # This will center the dataframe in the container

    # Define kolom numerical untuk kebutuhan eda
    st.write('')
    st.write('## Visualization')
    st.write('')
    st.write('___')

    # DISTRIBUSI (BARCHART)
    st.markdown('<h3 style="text-align: center;">Distribution of Sentiment Classes</h3>', unsafe_allow_html=True)
    # Menghitung distribusi jumlah kategori
    sentimen_counts = df['sentiment'].value_counts().reset_index()
    sentimen_counts.columns = ['Kategori', 'Jumlah']

    fig = px.bar(sentimen_counts, 
                labels={'Kategori': 'Sentiment', 'Jumlah': 'Count'},
                color='Kategori')
    st.plotly_chart(fig)

    st.write('')
    st.write('')
    st.write('___')

    # DISTRIBUSI PIE CHART
    st.markdown('<h3 style="text-align: center;">Percentage Distribution of Sentiment Sentiment</h3>', unsafe_allow_html=True)
    # Count the sentiment categories
    kategori_counts = df['sentiment'].value_counts()

    fig = px.pie(
        names=kategori_counts.index,  
        values=kategori_counts.values,  
        hover_name=kategori_counts.index
    )
    st.plotly_chart(fig)

    st.write('')
    st.write('___')

    # WORDCLOUD
    st.markdown('<h3 style="text-align: center;">Word Cloud by Sentiment Category based</h3>', unsafe_allow_html=True)
    st.write('')
    # Periksa apakah kolom "sentiment" dan "text" ada dalam dataset
    if "sentiment" in df.columns and "text" in df.columns:
        # Pisahkan teks berdasarkan sentimen
        positif_text = " ".join(df[df["sentiment"] == "Positif"]["text"].dropna().astype(str))
        negatif_text = " ".join(df[df["sentiment"] == "Negatif"]["text"].dropna().astype(str))

        # Buat WordCloud 
        wordcloud_positif = WordCloud(width=800, height=400, background_color='white').generate(positif_text) if positif_text else None
        wordcloud_negatif = WordCloud(width=800, height=400, background_color='white').generate(negatif_text) if negatif_text else None

        st.write('')
        # Buat Selectbox 
        sentiment_option = st.selectbox("Select Sentiment : ", ["Positive", "Negative"])

        # Tampilkan WordCloud sesuai pilihan pengguna
        st.write(f"#### Word Cloud Sentiment {sentiment_option}")

        if sentiment_option == "Positive" and wordcloud_positif:
            fig, ax = plt.subplots()
            ax.imshow(wordcloud_positif, interpolation='bilinear')
            ax.axis("off")
            st.pyplot(fig)
        elif sentiment_option == "Negative" and wordcloud_negatif:
            fig, ax = plt.subplots()
            ax.imshow(wordcloud_negatif, interpolation='bilinear')
            ax.axis("off")
            st.pyplot(fig)
        else:
            st.write("Tidak ada data untuk sentimen ini.")


#Jika tidak ingin langsung run
if __name__ == "__main__":
    run()