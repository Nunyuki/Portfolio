import streamlit as st
from utils.setup import setup_page
from utils.images import TOTORO, GITHUB, LINKEDIN

setup_page("📞 Contactez-moi")

st.markdown(f"""
<div class="info-box" style="margin:auto; width:65%;">
    <h4>🚀 Envie de collaborer ?</h4>
    <p>Je serais ravie d’échanger avec vous autour d’un projet, d’une opportunité ou d’une belle idée ✨</p>
    <h4>✉️ Email</h4>
    <p>daichenelodie@gmail.com</p>
    <h4>🌐 Réseaux</h4>
    <div style="display:flex; align-items:center; gap:15px; margin-top:5px;">
        <div style="display:flex; align-items:center; gap:5px;">
            <img src="data:image/png;base64,{LINKEDIN}" width="30"/>
            <a href="https://www.linkedin.com/in/dai-elodie/" target="_blank" style="color:#f5f5f5; text-decoration:none;">LinkedIn</a>
        </div>
        <div style="display:flex; align-items:center; gap:5px;">
            <img src="data:image/png;base64,{GITHUB}" width="30"/>
            <a href="https://github.com/Nunyuki" target="_blank" style="color:#f5f5f5; text-decoration:none;">GitHub</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

from utils.ui import mascot_row
mascot_row(TOTORO, "✨ Totoro est là pour accueillir vos messages ✨", size=100)