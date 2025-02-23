# Streamlit untuk UI
import streamlit as st

def run():     
    st.markdown("""
        <h1 style='text-align: center;  margin-bottom: 20px;'>Application of Sentiment Analysis</h1>
    """, unsafe_allow_html=True)


    st.markdown("<p style='text-align: center;'> <img src='https://asset.tix.id/wp-content/uploads/2021/11/Screen-Shot-2021-11-30-at-00.40.07-1200x760.png'> </p>", 
            unsafe_allow_html=True)

    # About
    st.write('___')
    st.markdown('''
    ### About 
    Welcome to the User Sentiment Analysis of Tix ID app project. This project utilizes Natural Language Processing (NLP) 
    techniques to analyze user reviews and identify their sentiments towards the features, service quality, 
    and experience of using the Tix ID app. Our goal is to provide valuable insights that can help the development 
    team identify areas for improvement and devise strategies to improve the overall user experience.''')

    # Background of the Problem
    st.write('___')
    st.markdown('''
    ### Background of the Problem
    With the rapid advancement in technology, various innovations in the digital field are now making everyday life easier. 
    One of them is online movie ticket booking. According to https://www.liputan6.com/feeds/read/5789953/cara-pesan-tiket-bioskop-online-panduan-lengkap-dan-praktis , 
    online movie ticket booking methods are increasingly in demand because they provide convenience and flexibility for consumers without having to wait in the counter 
    queue. One example is Tix ID, an online movie theater ticket booking application that is increasingly popular in Indonesia. The app allows users to purchase tickets 
    without having to visit a movie theater counter, providing convenience and easy access to the latest movies. Ticket booking is done through a digital platform such as 
    a smartphone app or website, allowing users to select the desired movie, showtime, and seats anytime and anywhere.

    Although these applications offer convenience, criticism 
    or negative feedback still needs to be considered to maintain service quality. Sentiment analysis on user reviews using Natural Language Processing (NLP) is one way to 
    understand user experience with the Tix ID app. With NLP techniques, Tix ID can analyze user feedback to identify feelings and opinions related to the services provided, 
    as well as find areas that need improvement. Therefore, sentiment analysis with NLP is essential in understanding the public perception of Tix ID and continuously improving 
    the overall user experience''')


#Jika tidak ingin langsung run
if __name__ == "__main__":
    run()