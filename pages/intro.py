import streamlit as st

def show():
    st.title("📌 Selamat Datang di Aplikasi Laporan Jalan Rusak")
    st.write("Aplikasi ini digunakan untuk melaporkan dan memvisualisasikan kondisi jalan rusak di Kabupaten Sidoarjo.")
    st.markdown("**Navigasi:**")
    st.button("➡️ Ke Peta Persebaran", on_click=lambda: st.session_state.update({"page": "Peta Persebaran"}))
    st.button("📤 Upload & Klasifikasi", on_click=lambda: st.session_state.update({"page": "Upload & Klasifikasi"}))
