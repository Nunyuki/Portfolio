import streamlit as st
import base64

def load_css():
    st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(to bottom, #000000 60%, #4B0000 100%);
        color: #f5f5f5;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    h1, h2 { text-align: center; }

    h3, h4, h5, h6, p, a, button { color: #f5f5f5; text-align: left; }

    .cv-button {
        font-weight: bold;
        color: #f5f5f5 !important;
        background-color: #550000 !important;
        padding: 10px 20px;
        border-radius: 8px;
        text-decoration: none !important;
    }

    .cv-button:hover {
        background-color: #770000 !important;
        text-decoration: none !important;
        color: #f5f5f5 !important;
    }

    .info-box, .contact-box {
        background-color: rgba(255, 255, 255, 0.05);
        padding: 20px 25px;
        border-radius: 10px;
        font-size: 18px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)


def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()