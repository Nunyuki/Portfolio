import streamlit as st
from utils.setup import setup_page
from utils.ui import formation_block_info
from utils.formation import formations
from utils.images import PONYO

setup_page("🎓 Mon Parcours de Formation")

st.markdown("""
<p style="text-align:center; font-size:17px;">
Chaque étape de mon parcours a renforcé mes compétences techniques, ma rigueur analytique et ma passion pour l’innovation numérique.
</p>
""", unsafe_allow_html=True)

for f in formations:
    formation_block_info(f['title'], f.get('subtitle',''), f.get('years',''), f.get('details',''))

from utils.ui import mascot_row
mascot_row(PONYO, "🐠 Ponyo veille sur mon parcours et chaque étape me fait grandir ! 🐠", size=90)