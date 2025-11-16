import streamlit as st
from .style import img_to_base64

def info_box_html(inner_html: str, style: str = ""):
  st.markdown(f"<div class=\"info-box\" style=\"{style}\">{inner_html}</div>", unsafe_allow_html=True)

def badges(items):
  return "".join(f'<div class="skill-badge-inline">{i}</div>' for i in items)


def mascot_row(img_b64: str, text: str, size: int = 100):
  st.markdown(f"""
    <div style="display:flex; align-items:center; justify-content:center; gap:20px; margin-top:20px;">
      <img src="data:image/png;base64,{img_b64}" width="{size}"/>
      <p style="margin:0; font-size:16px;">{text}</p>
    </div>
  """, unsafe_allow_html=True)

def formation_block_info(title, subtitle, years, details):
    with st.container():
        st.markdown(f"""
        <div class="info-box" style="margin-bottom:10px;">
            <h4>{title}</h4>
            <p style="margin:0; font-size:15px;"><b>{subtitle}</b> | <i>{years}</i></p>
        </div>
        """, unsafe_allow_html=True)

        with st.expander("🧾 En savoir plus"):
            st.markdown(details, unsafe_allow_html=True)

def exp_block_info(title, company, place, period, tools, summary, details, logo_path=None):
    logo_b64 = img_to_base64(logo_path) if logo_path else None
    
    tools_html = "".join([f'<div class="skill-badge-inline">{tool}</div>' for tool in tools])
    
    with st.container():
        st.markdown(f"""
        <div class="info-box" style="margin-bottom:10px; display:flex; align-items:center; gap:15px;">
            {'<img src="data:image/png;base64,' + logo_b64 + '" width="100" style="border-radius:8px;">' if logo_b64 else ''}
            <div>
                <h4>{title} | {company} | {place}</h4>
                <p style="margin:0; font-size:15px;"><i>{period}</i></p>
                <p style="margin-top:8px;">{summary}</p>
                <div style="display:flex; flex-wrap:wrap; gap:8px; margin-top:5px;">
                    {tools_html}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        with st.expander("🧾 En savoir plus"):
            st.markdown(details, unsafe_allow_html=True)

# Slider / slideshow générique (utilise session_state)
def project_block_info(title, description, tools, links, images, details_texts):
    tools_html = "".join([f'<div class="skill-badge-inline">{tool}</div>' for tool in tools])
    
    if f"{title}_idx" not in st.session_state:
        st.session_state[f"{title}_idx"] = 0

    def prev_image():
        st.session_state[f"{title}_idx"] = (st.session_state[f"{title}_idx"] - 1) % len(images)

    def next_image():
        st.session_state[f"{title}_idx"] = (st.session_state[f"{title}_idx"] + 1) % len(images)

    idx = st.session_state[f"{title}_idx"]

    # Génération des liens
    links_html = ""
    if links:
        for link in links:
            links_html += f'<a href="{link["url"]}" target="_blank" style="color:#f5f5f5; margin-right:15px;">🔗 {link["name"]}</a>'

    with st.container():
        # Bloc principal full width
        st.markdown(f"""
        <div class="info-box" style="margin-bottom:10px; width:100%; max-width:1200px; margin-left:auto; margin-right:auto;">
            <h4>{title}</h4>
            <p style="margin:0; font-size:15px;">{description}</p>
            <div style="display:flex; flex-wrap:wrap; gap:6px; margin-top:5px;">
                {tools_html}
            </div>
            <p style="margin-top:5px;">{links_html}</p>
        </div>
        """, unsafe_allow_html=True)

        # Expander pour détails
        with st.expander("🧾 En savoir plus"):
            # Texte avec chevrons à gauche et droite
            col_left, col_text, col_right = st.columns([1, 9, 1])
            with col_left:
                st.button("❮", key=f"prev_{title}", on_click=prev_image, use_container_width=True)
            with col_text:
                st.markdown(f'<p style="font-size:13px; margin-top:8px;">{details_texts[idx]}</p>', unsafe_allow_html=True)
            with col_right:
                st.button("❯", key=f"next_{title}", on_click=next_image, use_container_width=True)
            st.image(images[idx], width=1000)  # image au-dessus
            