import streamlit as st
from utils.setup import setup_page
from utils.images import SUIE
import json
import os
from datetime import datetime
import matplotlib.pyplot as plt

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


query_params = st.query_params
is_admin = query_params.get("admin") == "1"

FILE = "views.json"

# Charger fichier historique
if not os.path.exists(FILE):
    with open(FILE, "w") as f:
        json.dump({}, f)

with open(FILE, "r") as f:
    views = json.load(f)

today = datetime.now().strftime("%Y-%m-%d")

# Mise à jour du compteur
if today not in views:
    views[today] = 0
views[today] += 1

# Sauvegarde
with open(FILE, "w") as f:
    json.dump(views, f, indent=4)

# --- AFFICHAGE ADMIN SEULEMENT ---
if is_admin:
    st.sidebar.markdown("## 👁️ Statistiques")
    st.sidebar.write(f"Vues aujourd’hui : **{views[today]}**")

    dates = list(views.keys())
    counts = list(views.values())

    fig, ax = plt.subplots(figsize=(4, 2))
    ax.plot(dates, counts, marker="o")
    ax.set_xlabel("Date")
    ax.set_ylabel("Vues")
    ax.set_title("Vues par jour")
    plt.xticks(rotation=45, fontsize=6)
    plt.tight_layout()

    st.sidebar.pyplot(fig)
