import streamlit as st
from utils.setup import setup_page
from utils.ui import project_block_info
from utils.projets import get_projets
from utils.images import MORO

setup_page("💻 Mes Projets")

st.markdown("""
<p style="text-align:center; font-size:16px;">
Découvrez mes projets réalisés en cours et en autonomie, avec les technologies utilisées et les liens vers le code.
</p>
""", unsafe_allow_html=True)

projets = get_projets()

col1, col2 = st.columns(2)
for i, proj in enumerate(projets):
    col = col1 if i % 2 == 0 else col2
    with col:
        project_block_info(
            title=proj["title"],
            description=proj["description"],
            tools=proj["tools"],
            links=proj.get("links", []),
            images=proj["images"],
            details_texts=proj["details_text"]
        )

from utils.ui import mascot_row
mascot_row(MORO, "🐺 Moro inspire mes projets, m’incitant à avancer avec courage et détermination. 🐺", size=100)