"""
ALAS v4.0 — Academic Literature Analysis System
Streamlit Cloud Wrapper
Deploy: share.streamlit.io
"""

import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# ─── Page config ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="ALAS v4.0 — Academic Literature Analysis System",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        "Get Help": None,
        "Report a bug": None,
        "About": "ALAS v4.0 — Academic Literature Analysis System\nCore Layer 13 Seksi (A–M) | 12 Modul | PUBEI | Mesin Konteks"
    }
)

# ─── Hide Streamlit chrome for full-screen feel ──────────────────────────────
st.markdown("""
<style>
  /* Hide Streamlit default header and footer */
  #MainMenu { visibility: hidden; }
  header { visibility: hidden; }
  footer { visibility: hidden; }

  /* Remove default padding so dashboard fills screen */
  .block-container {
      padding-top: 0 !important;
      padding-bottom: 0 !important;
      padding-left: 0 !important;
      padding-right: 0 !important;
      max-width: 100% !important;
  }
  .stApp {
      background: #1a1a2e;
  }
</style>
""", unsafe_allow_html=True)

# ─── Load dashboard HTML ─────────────────────────────────────────────────────
html_path = Path(__file__).parent / "dashboard.html"

if not html_path.exists():
    st.error("❌ File dashboard.html tidak ditemukan. Pastikan file ada di folder yang sama dengan app.py")
    st.stop()

html_content = html_path.read_text(encoding="utf-8")
html_size_kb = len(html_content) / 1024

# ─── Render dashboard ────────────────────────────────────────────────────────
components.html(
    html_content,
    height=950,
    scrolling=False
)

# ─── Debug info (hidden in production) ───────────────────────────────────────
# Uncomment below for debugging if dashboard doesn't load:
# st.write(f"Dashboard loaded: {html_size_kb:.1f} KB")
