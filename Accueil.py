import streamlit as st

st.set_page_config(page_title="Mon Portfolio", layout="wide")

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(to bottom, #000000 60%, #4B0000 100%);
    color: #f5f5f5;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

h1, h2 {
    text-align: center;
}

h3, h4, h5, h6, p, a, button {
    color: #f5f5f5;
    text-align: left;
}

.contact-link {
    font-weight: bold;
    color: #f5f5f5;
    background-color: #330011;
    padding: 10px 20px;
    border-radius: 8px;
    text-decoration: none;
}

.contact-link:hover {
    background-color: #4d001a;
}

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
}
</style>
""", unsafe_allow_html=True)

st.title("🚀 Coucou, je suis Elodie DAI !")
st.subheader("Développement le jour, créativité toujours. J’aime construire mes projets avec la même attention que je mets dans mes créations personnelles.\n")

col1, col2 = st.columns([3, 1]) 

with col1:
    st.markdown("""
    <div class="info-box">
    <h3>🎓 Formation</h3>
    <p>Master MIAGE, Université Paris Dauphine - PSL</p>
    <h3>💼 Expérience</h3>
    <p>3 ans d’alternance à SwissLife Banque Privée</p>
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
        file_name="CV_Elodie.pdf",
        mime="application/pdf",
        key="cv_download",
        help="Cliquez pour télécharger mon CV"
    )
