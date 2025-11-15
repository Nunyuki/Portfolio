import streamlit as st
from .style import load_css


def setup_page(title):
  st.set_page_config(page_title=title, layout="wide")
  load_css()
  st.title(title)