import streamlit as st
import pages.intro as intro
#import pages.peta as peta
import pages.upload_klasifikasi as upload_klasifikasi

st.set_page_config(page_title="Laporan Jalan Rusak", layout="wide")

pages = {
    "📌 Halaman Awal": intro.show,
    #"🗺️ Peta Persebaran Jalan Rusak": peta.show,
    "📤 Upload & Klasifikasi": upload_klasifikasi.show,
}

page = st.sidebar.selectbox("Pilih Halaman", list(pages.keys()))
pages[page]()
