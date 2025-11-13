import streamlit as st
from utils.style import load_css, img_to_base64

st.set_page_config(page_title="À propos de moi", layout="wide")
load_css()

haku_b64 = img_to_base64("assets/haku.png")
instagram_b64 = img_to_base64("assets/instagram.png")

st.title("✨ À propos de moi")
st.markdown("""
<p style="text-align:center; font-size:16px;">
Découvrez un aperçu de mes passions et de mon univers personnel.
</p>
""", unsafe_allow_html=True)


col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="info-box">
        <h4>🌍 Voyages</h4>
        <h6>Chaque voyage est une nouvelle source d’inspiration</h6>
        <p>Chine, Italie, Portugal, Iles Canaries, Belgique, Alpes, Annecy, Strasbourg</p>
    </div>
    """, unsafe_allow_html=True)
 
    st.markdown("""
    <div class="info-box">
        <h4>💡 Traits de personnalité</h4>
        <h6>J’aime apprendre, explorer et relever de nouveaux challenges.</h6>
        <p>Curieuse, créative, persévérante, prête à relever un nouveau défi.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-box">
        <h4>🎮 Activités</h4>
        <h6>S’amuser et se challenger font partie de ma vie quotidienne.</h6>
        <p>Escape game, Action game, Arcade, Accrobranche, Karting</p>
    </div>
    """, unsafe_allow_html=True)
        
    st.markdown("""
    <div class="info-box">
        <h4>🏃 Sport</h4>
        <h6>Le sport me permet d’aborder mes journées avec dynamisme.</h6>
        <p>Salle de sport, Course, Badminton, Escalade, Natation</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
  
    st.markdown("""
    <div class="info-box">
        <h4>🎵 Divertissement</h4>
        <h6>Rire, s’émerveiller et se divertir sont essentiels pour garder l’esprit créatif.</h6>
        <p>Animé, Manga, Musique,  Jeux de rythme, Cinéma</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <h4>🎨 Loisirs créatifs</h4>
        <h6>Chaque création devient un reflet de ma créativité.</h6>
        <p>Crochet, Broderie, Bracelet, Pâte Fimo, Terre cuite, Pâtisserie, Dessin</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown(f"""
<div class="info-box" style="text-align:center;">
    <h4>📸 Mes créations</h4>
    <p style="font-style:italic;">Un petit aperçu de mes créations manuelles et photos pour éveiller votre curiosité !</p>
    <div style="display:flex; align-items:center; justify-content:center; gap:15px; margin-top:5px;">
        <div style="display:flex; align-items:center; gap:5px;">
            <img src="data:image/png;base64,{instagram_b64}" width="30"/>
            <a href="https://www.instagram.com/nunyuki_crochet" target="_blank" style="color:#f5f5f5; text-decoration:none;">Portfolio_craft</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div style="display:flex; justify-content:center; align-items:center; gap:15px; margin-top:20px;">
    <img src="data:image/png;base64,{haku_b64}" width="100"/>
    <p style="margin:0; font-size:16px;">🐉 Haku m’inspire à rester libre et fidèle à mes passions, comme un souffle entre ciel et eau. 🐉</p>
</div>
""", unsafe_allow_html=True)
