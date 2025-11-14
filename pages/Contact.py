import streamlit as st
from utils.style import load_css, img_to_base64

st.set_page_config(page_title="Mes Contacts", layout="wide")
load_css()

linkedin_b64 = img_to_base64("assets/logo/linkedin.png")
github_b64   = img_to_base64("assets/logo/github.png")
totoro_b64   = img_to_base64("assets/ghibli/totoro.png")

st.title("📞 Contactez-moi")

st.markdown(f"""
<div class="info-box" style="margin:auto; width:65%;">
    <h4>🚀 Envie de collaborer ?</h4>
    <p>Je serais ravie d’échanger avec vous autour d’un projet, d’une opportunité ou d’une belle idée ✨</p>
    <h4>✉️ Email</h4>
    <p>daichenelodie@gmail.com</p>
    <h4>🌐 Réseaux</h4>
    <div style="display:flex; align-items:center; gap:15px; margin-top:5px;">
        <div style="display:flex; align-items:center; gap:5px;">
            <img src="data:image/png;base64,{linkedin_b64}" width="30"/>
            <a href="https://www.linkedin.com/in/dai-elodie/" target="_blank" style="color:#f5f5f5; text-decoration:none;">LinkedIn</a>
        </div>
        <div style="display:flex; align-items:center; gap:5px;">
            <img src="data:image/png;base64,{github_b64}" width="30"/>
            <a href="https://github.com/Nunyuki" target="_blank" style="color:#f5f5f5; text-decoration:none;">GitHub</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div style="display:flex; align-items:center; justify-content:center; gap:20px; margin-top:10px;">
    <img src="data:image/png;base64,{totoro_b64}" width="100"/>
    <p style="margin:0; font-size:16px;">✨ Totoro est là pour accueillir vos messages ✨</p>
</div>
""", unsafe_allow_html=True)