import streamlit as st
from utils.setup import setup_page
from utils.style import load_css, img_to_base64
from utils.images import SUIE

setup_page("🚀 Coucou, je suis Elodie DAI !")
st.subheader("Développement le jour, créativité toujours. J’aime construire mes projets avec la même attention que je mets dans mes créations personnelles.")

col1, col2 = st.columns([5, 2])

with col1:
    st.markdown("""
    <div class="info-box">
        <h4>🎓 Formation</h4>
        <p>Diplômée d’un Master MIAGE à l’Université Paris Dauphine – PSL</p>
        <h4>💼 Expérience</h4>
        <p>Trois années d’alternance enrichissantes au sein de SwissLife Banque Privée</p>
        <h4>🔍 Objectif</h4>
        <p>Ouverte à un CDI stimulant au sein d’une équipe collaborative et dynamique</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-box">
        <h4>Contactez-moi</h4>
        <p>Impatiente de collaborer avec vous sur des projets stimulants et enrichissants !</p>
        <h5>✉ Email</h5>
        <p>daichenelodie@gmail.com</p>
    </div>
    """, unsafe_allow_html=True)

    with open("assets/CV.pdf", "rb") as f:
        pdf_bytes = f.read()

    st.download_button(
        label="📄 Télécharger mon CV",
        data=pdf_bytes,
        file_name="CV_Elodie_DAI.pdf",
        mime="application/pdf",
        key="cv_download"
    )

from utils.ui import mascot_row
mascot_row(SUIE, "🐾 Les petites boules de suie sont là pour vous guider dans mon univers créatif 🐾", size=100)