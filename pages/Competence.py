import streamlit as st
from utils.style import load_css, img_to_base64, create_skill

st.set_page_config(page_title="Mes Compétences", layout="wide")
load_css()

calcifer_b64   = img_to_base64("assets/calcifer.png")

st.title("🛠 Mes Compétences")

col1, col2 = st.columns(2)

blocks = [
    ("💻 Développement & Langages", ["Python", "Java", "JavaFX", "C", "OCaml", "XML"]),
    ("📊 Base de données & ETL", ["MySQL", "PostgreSQL", "Microsoft SQL Server", "Talend", "Datastage Server IBM", "SSRS", "PL/SQL", "Trigger"]),
    ("🛠 Frameworks & Outils", ["Angular", "Spring Boot", "Figma", "Unity", "Google Cloud Platform", "Swagger", "Microservice", "Streamlit"]),
    ("🛠 IDE & Outils", ["IntelliJ IDEA", "VSCode", "PyCHARM", "Eclipse", "GitHub", "VS2022"]),
    ("🗂 Structure de données & Algorithmes", ["Liste doublement chaînée", "Table de Hashage", "Arbre", "Graphe", "Schéma E/A", "Modèle relationnel", "Calcul relationnel", "Algèbre relationnelle","SQL"]),
    ("💻 Systèmes d'exploitation", ["Windows", "Ubuntu"]),
    ("💡 Soft Skills", ["Assidue", "Travail en équipe", "Adaptabilité", "Créativité", "Gestion du temps"])
]

for i, (title, skills) in enumerate(blocks):
    if i % 2 == 0:
        with col1:
            st.markdown(create_skill(title, skills), unsafe_allow_html=True)
    else:
        with col2:
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

st.markdown(f"""
<div style="display:flex; align-items:center; justify-content:center; gap:20px; margin-top:10px;">
    <img src="data:image/png;base64,{calcifer_b64}" width="100"/>
    <p style="margin:0; font-size:16px;">💡 Calcifer présente les compétences qui font briller mes projets 💡</p>
</div>
""", unsafe_allow_html=True)