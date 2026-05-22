# ALAS v4.0 — Academic Literature Analysis System

Dashboard akademik berbasis AI untuk mendukung penelitian ilmiah.

## Fitur Utama

- **12 Modul** penelitian lengkap (Modul 0–10)
- **Core Layer v4.0** — 13 seksi (A–M), Mode TAK, PUBEI
- **Seksi L** — Mesin Parameter Konteks (Bidang/Level/Target)
- **Seksi M** — Protokol Analisis Statistik Multivariat
- **Modul 10** — 10 Rekomendasi Judul (Statistik Multivariat)
- **Anti-halusinasi** aktif + 9 gerbang kualitas
- Kompatibel: ChatGPT, Claude, Gemini, Grok, Copilot

## Cara Penggunaan

1. Pilih konteks penelitian (Bidang / Level / Target) di Beranda
2. Navigasi ke modul yang dibutuhkan via sidebar kiri
3. Klik "Copy Prompt" → paste ke AI manapun
4. Ikuti instruksi di setiap modul

## Deploy

```
streamlit run app.py
```

## Stack

- Python + Streamlit (wrapper)
- HTML/CSS/JS (dashboard ALAS)
- Tidak memerlukan database atau API key
