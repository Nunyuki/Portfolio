import streamlit as st
import base64

def load_css():
    st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(to bottom, #000000 60%, #4B0000 100%);
        color: #f5f5f5;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    h1, h2 { text-align: center; }
    h3, h4, h5, h6, p, a, button { color: #f5f5f5; text-align: left; }

    /* Conteneur général */
    .info-box {
        background-color: rgba(255, 255, 255, 0.07);
        padding: 15px 30px;
        border-radius: 20px;
        font-size: 16px;
        margin-bottom: 15px;
    }

    /* Badges standard */
    .skill-badge, .skill-badge-inline {
        display:inline-block;
        background-color: #550000;
        padding: 5px 10px;
        border-radius: 5px;
        color: #f5f5f5;
        font-size: 14px;
        transition: transform 0.2s, background-color 0.2s;
        cursor: default;
    }

    .skill-badge:hover, .skill-badge-inline:hover {
        background-color: #770000;
        transform: scale(1.05);
    }

    /* Langues - barres */
    .lang-bar-bg {
        background-color: rgba(255,255,255,0.1);
        border-radius: 5px;
        height: 20px;
        width: 100%;
        margin-bottom: 10px;
    }

    .lang-bar-fill {
        background-color: #550000;
        height: 100%;
        border-radius: 5px;
        text-align:center;
        line-height:20px;
        color:#f5f5f5;
        font-weight:bold;
    }
    </style>
    """, unsafe_allow_html=True)


def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def create_skill(title, skills):
    badges_html = "".join([f'<div class="skill-badge-inline">{skill}</div>' for skill in skills])
    return f"""
    <div class="info-box" style="width:100%; margin-bottom:15px;">
        <h5>{title}</h5>
        <div style="display:flex; flex-wrap:wrap; gap:10px;">{badges_html}</div>
    </div>
    """
    
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
            
def experience_block_info(title, company, place, period, tools, summary, details):
    tools_html = "".join([f'<div class="skill-badge-inline">{tool}</div>' for tool in tools])
    
    with st.container():
        st.markdown(f"""
        <div class="info-box" style="margin-bottom:10px;">
            <h4>{title} | {company} | {place} </h4>
            <p style="margin:0; font-size:15px;"><i>{period}</i></p>
            <p style="margin-top:8px;">{summary}</p>
            <div style="display:flex; flex-wrap:wrap; gap:8px; margin-top:5px;">
                {tools_html}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        with st.expander("🧾 En savoir plus"):
            st.markdown(details, unsafe_allow_html=True)