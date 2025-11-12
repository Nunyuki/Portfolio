import streamlit as st

st.title("Bonjour, je suis Elodie DAI")
st.subheader("Diplômée de la formation Master MIAGE à l'Université Paris Dauphine - PSL")

st.button("Voir mes projets")
st.button("Télécharger mon CV")

page = st.selectbox("Naviguer vers :", ["Accueil", "Projets", "Contact"])

if page == "Accueil":
    st.header("Accueil")
    st.write("Voici un petit aperçu de moi et de mes compétences.")
    st.write("- Développement Python, Web et Data")  
    st.write("- Projets personnels et professionnels")  

elif page == "Projets":
    st.header("Mes Projets")
    st.write("Voici quelques-uns de mes projets réalisés :")
    st.write("1. Projet A")
    st.write("2. Projet B")
    st.write("3. Projet C")

elif page == "Contact":
    st.header("Contact")
    st.write("📬 Vous êtes ici pour me contacter ?")
    st.write("[Cliquez ici pour aller à la page Contact](./pages/00_Contact.py)")

# Bouton direct vers la page Contact
if st.button("📞 Me contacter"):
    st.write("Cliquez ici pour accéder à la page Contact :")
    st.markdown("[Aller à la page Contact](./pages/00_Contact.py)")
