from utils.setup import setup_page, st
from utils.style import img_to_base64, project_block_info
from utils.projets import get_projets 

setup_page("💻 Mes Projets")

moro_b64 = img_to_base64("assets/ghibli/moro.png")

st.markdown("""
<p style="text-align:center; font-size:16px;">
Découvrez mes projets réalisés en cours et en autonomie, avec les technologies utilisées et les liens vers le code.
</p>
""", unsafe_allow_html=True)

projets = get_projets()

col1, col2 = st.columns(2)
for i, proj in enumerate(projets):
    col = [col1, col2][i % 2]  # alterne entre les 3 colonnes
    with col:
        project_block_info(
            title=proj["title"],
            description=proj["description"],
            tools=proj["tools"],
            links=proj.get("links", []),
            images=proj["images"],
            details_texts=proj["details_text"]
        )

st.markdown(f"""
<div style="display:flex; align-items:center; justify-content:center; gap:20px; margin-top:20px;">
    <img src="data:image/png;base64,{moro_b64}" width="100"/>
    <p style="margin:0; font-size:16px;">🐺 Moro inspire mes projets, m’incitant à avancer avec courage et détermination. 🐺</p>
</div>
""", unsafe_allow_html=True)

