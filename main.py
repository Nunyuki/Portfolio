import streamlit as st

st.set_page_config(page_title="Mon Portfolio", layout="wide")

# CSS pour le lien
st.markdown("""
<style>
.contact-link {
    font-weight: bold;
    color: white;
    background-color: #4CAF50;  /* vert joyeux */
    padding: 10px 20px;
    border-radius: 8px;
    text-decoration: none;
}
.contact-link:hover {
    background-color: #45a049;
}
</style>
""", unsafe_allow_html=True)

# --- Header avec lien Me contacter ---
col1, col2 = st.columns([1, 5])  # 1/6 pour le lien, 5/6 pour le titre
with col1:
    st.markdown(
        '<a class="contact-link" href="https://nunyuki-portfolio-dev.streamlit.app/pages/00_Contact" target="_blank">📞 Me contacter</a>',
        unsafe_allow_html=True
    )
with col2:
    st.title("Bonjour, je suis Elodie DAI")
    st.subheader("Diplômée de la formation Master MIAGE à l'Université Paris Dauphine - PSL")

# --- Boutons ---
col3, col4 = st.columns(2)
with col3:
    if st.button("Voir mes projets"):
        st.write("➡️ Ici tu peux ajouter un lien ou faire défiler vers tes projets.")

with col4:
    if st.button("Télécharger mon CV cc" ):
        st.write("➡️ Ici tu peux mettre un lien pour télécharger ton CV PDF.")