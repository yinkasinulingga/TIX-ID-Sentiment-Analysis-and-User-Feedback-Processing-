# Streamlit untuk UI
import streamlit as st

# Import modul internal
import home
import eda
import predict


st.sidebar.title("TIX ID Sentiment App")
st.sidebar.markdown("""
    <style>
        .stButton > button {
            width: 100%;
            padding: 8px;
            margin-bottom: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar buttons
home_button = st.sidebar.button("Home")
eda_button = st.sidebar.button("EDA")
predict_button = st.sidebar.button("Predict")

# Page navigation logic based on button clicks
if home_button:
    st.session_state.page = "home"
elif eda_button:
    st.session_state.page = "eda"
elif predict_button:
    st.session_state.page = "predict"

# Default page is "home" if no button is clicked
if 'page' not in st.session_state:
    st.session_state.page = "home"

# Run the respective page based on the stored session state
if st.session_state.page == "home":
    home.run()
elif st.session_state.page == "eda":
    eda.run()
elif st.session_state.page == "predict":
    predict.run()
