import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="ALAS v5.0",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        "About": "ALAS v5.0 · 15 Seksi (A-O) · 12 Modul\n© 2025 Alhumaira Store\nobrolanpintar1987@gmail.com"
    }
)

st.markdown("""<style>
#MainMenu,header,footer,[data-testid="stHeader"],
[data-testid="stToolbar"],[data-testid="stDecoration"],
.stDeployButton{display:none!important;visibility:hidden!important}
.main .block-container{padding:0!important;margin:0!important;max-width:100%!important}
.main{padding:0!important}
html,body{margin:0!important;padding:0!important;overflow-x:hidden}
iframe{width:100%!important;border:none!important;display:block!important}
</style>""", unsafe_allow_html=True)

html_path = Path(__file__).parent / "dashboard.html"
if not html_path.exists():
    st.error("dashboard.html tidak ditemukan.")
    st.stop()

components.html(
    html_path.read_text(encoding="utf-8"),
    height=5000,
    scrolling=True
)
