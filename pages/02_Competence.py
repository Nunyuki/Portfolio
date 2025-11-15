import streamlit as st
from utils.setup import setup_page
from utils.style import create_skill
from utils.images import CALCIFER

setup_page("🛠 Mes Compétences")

blocks = [
    ("💻 Développement & Langages", ["Python", "Java", "JavaFX", "C", "OCaml", "XML"]),
    ("📊 Base de données & ETL", ["MySQL", "PostgreSQL", "Microsoft SQL Server", "Talend", "Datastage Server IBM", "SSRS", "PL/SQL", "Trigger"]),
    ("🛠 Frameworks & Outils", ["Angular", "Spring Boot", "Figma", "Unity", "Google Cloud Platform", "Swagger", "Microservice", "Streamlit"]),
    ("🛠 IDE & Outils", ["IntelliJ IDEA", "VSCode", "PyCHARM", "Eclipse", "GitHub", "VS2022", "BlueJ"]),
    ("🗂 Structure de données & Algorithmes", ["Liste doublement chaînée", "Table de Hashage", "Arbre", "Graphe", "Schéma E/A", "Modèle relationnel", "Calcul relationnel", "Algèbre relationnelle","SQL"]),
    ("💻 Systèmes d'exploitation", ["Windows", "Ubuntu"]),
    ("💡 Soft Skills", ["Assidue", "Travail en équipe", "Adaptabilité", "Créativité", "Gestion du temps"])
]

col1, col2 = st.columns(2)
for i, (title, skills) in enumerate(blocks):
    target = col1 if i % 2 == 0 else col2
    with target:
        st.markdown(create_skill(title, skills), unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-box" style="width:100%; margin-bottom:10px;">
        <h5>🌐 Langues</h5>
        <p>Français</p>
        <div class="lang-bar-bg">
            <div class="lang-bar-fill" style="width:100%; font-size:16px;"></div>
        </div>
        <p>Chinois</p>
        <div class="lang-bar-bg">
            <div class="lang-bar-fill" style="width:100%; font-size:16px;"></div>
        </div>
        <p>Anglais</p>
        <div class="lang-bar-bg">
            <div class="lang-bar-fill" style="width:65%; font-size:16px;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

from utils.ui import mascot_row
mascot_row(CALCIFER, "💡 Calcifer présente les compétences qui font briller mes projets 💡", size=100)