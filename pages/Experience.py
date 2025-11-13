import streamlit as st
from utils.style import load_css, img_to_base64, experience_block_info
from utils.experiences import experiences 

st.set_page_config(page_title="Mes Expériences", layout="wide")
load_css()

# Image pour la page
noface_b64 = img_to_base64("assets/noface.png")

st.title("💼 Mes Expériences Professionnelles")



# Générer automatiquement tous les blocs depuis le JSON importé
for exp in experiences:
    experience_block_info(
        title=exp["title"],
        company=exp["company"],
        place=exp["place"],
        period=exp["period"],
        tools=exp["tools"],
        summary=exp["summary"],
        details=exp["details"]
    )

# Illustration / mascotte
st.markdown(f"""
<div style="display:flex; align-items:center; justify-content:center; gap:20px; margin-top:20px;">
    <img src="data:image/png;base64,{noface_b64}" width="100"/>
    <p style="margin:0; font-size:16px;">👻 NoFace gagne de l'expérience avec moi à chaque endroit ! 👻</p>
</div>
""", unsafe_allow_html=True)
