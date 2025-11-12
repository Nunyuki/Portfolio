import streamlit as st
from utils.style import load_css, img_to_base64

st.set_page_config(page_title="Mon Portfolio", layout="wide")

load_css()
suie_b64 = img_to_base64("assets/suie.png")

st.title("🚀 Coucou, je suis Elodie DAI !")
st.subheader("Développement le jour, créativité toujours. J’aime construire mes projets avec la même attention que je mets dans mes créations personnelles.\n")

col1, col2 = st.columns([5, 2]) 

with col1:
    st.markdown("""
    <div class="info-box">
    <h3>🎓 Formation</h3>
    <p>Diplômée d’un Master MIAGE à l’Université Paris Dauphine – PSL</p>
    <h3>💼 Expérience</h3>
    <p>Trois années d’alternance enrichissantes au sein de SwissLife Banque Privée</p>
    <h3>🔍 Objectif</h3>
    <p>Ouverte à un CDI stimulant au sein d’une équipe collaborative et dynamique</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="contact-box">
    <h3>Contactez-moi</h3>
    <p>Impatiente de collaborer avec vous sur des projets stimulants et enrichissants !</p>
    <h3>✉ Email</h3>
    <p>daichenelodie@gmail.com</p>
    """, unsafe_allow_html=True)

    with open("assets/CV.pdf", "rb") as f:
        pdf_bytes = f.read()

    st.download_button(
        label="📄 Télécharger mon CV",
        data=pdf_bytes,
        file_name="CV_Elodie_DAI.pdf",
        mime="application/pdf",
        key="cv_download",
        help="Cliquez pour télécharger mon CV"
    )

st.markdown(f"""
<div style="display:flex; align-items:center; justify-content:center; gap:20px; margin-top:2px;">
    <img src="data:image/png;base64,{suie_b64}" width="100"/>
    <p style="margin:0; font-size:18px;">🐾 Les petites boules de suie sont là pour vous guider dans mon univers créatif 🐾</p>
</div>
""", unsafe_allow_html=True)