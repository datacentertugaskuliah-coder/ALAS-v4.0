"""
ALAS v5.0 — Academic Literature Analysis System
Streamlit Cloud Wrapper
"""

import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="ALAS v5.0 — Academic Literature Analysis System",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={"About": "ALAS v5.0 — 15 Seksi (A–O) | 12 Modul | Core Layer Profesional"}
)

# Sembunyikan UI default Streamlit
st.markdown("""
<style>
  #MainMenu,header,footer{visibility:hidden}
  .block-container{
    padding:0 !important;
    max-width:100% !important
  }
  .stApp{background:#f0eeea}
  iframe{border:none !important}
</style>
""", unsafe_allow_html=True)

# Muat dashboard HTML
html_path = Path(__file__).parent / "dashboard.html"
if not html_path.exists():
    st.error("❌ dashboard.html tidak ditemukan.")
    st.stop()

html_content = html_path.read_text(encoding="utf-8")

# Render dashboard penuh
components.html(html_content, height=960, scrolling=False)
