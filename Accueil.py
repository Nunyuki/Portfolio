import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(to bottom, #000000 60%, #4B0000 100%);
    color: #f5f5f5;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

h1, h2, h3, h4, h5, h6, p, a, button {
    color: #f5f5f5;
}

.contact-link {
    font-weight: bold;
    color: #f5f5f5;
    background-color: #330011; /* rouge très sombre pour le bouton */
    padding: 10px 20px;
    border-radius: 8px;
    text-decoration: none;
}

.contact-link:hover {
    background-color: #4d001a; /* légèrement plus clair au survol */
}
</style>
""", unsafe_allow_html=True)

st.markdown('<a class="contact-link" href="/pages/00_Contact">📞 Me contacter</a>', unsafe_allow_html=True)

st.title("Bonjour, je suis Elodie DAI")
st.subheader("Diplômée de la formation Master MIAGE à l'Université Paris Dauphine - PSL")

col1, col2 = st.columns(2)

with col1:
    if st.button("Voir mes projets"):
        st.write("➡️ Ici tu peux ajouter un lien ou faire défiler vers tes projets.")

with col2:
    if st.button("Télécharger mon CV"):
        st.write("➡️ Ici tu peux mettre un lien pour télécharger ton CV PDF.")
