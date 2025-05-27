import streamlit as st
import pandas as pd
from PIL import Image
from utils.klasifikasi import klasifikasikan_gambar

def show():
    st.title("📤 Upload Foto Jalan Rusak")

    uploaded_file = st.file_uploader("Upload Foto Jalan", type=["jpg", "png"])
    lat = st.number_input("Latitude", format="%.6f")
    lon = st.number_input("Longitude", format="%.6f")

    if uploaded_file and lat and lon:
        img = Image.open(uploaded_file)
        st.image(img, caption="Foto Jalan", use_column_width=True)

        if st.button("🔍 Klasifikasikan"):
            hasil = klasifikasikan_gambar(img)
            st.success(f"Hasil Klasifikasi: **{hasil}**")

            # Simpan hasil
            df = pd.read_csv("data/data_jalan_rusak.csv")
            df = df.append({"latitude": lat, "longitude": lon, "hasil": hasil}, ignore_index=True)
            df.to_csv("/workspaces/GUSKRISPI/data/Kordinat+prediksi.csv", index=False)
