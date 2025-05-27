import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

def show():
    st.title("🗺️ Peta Persebaran Jalan Rusak di Sidoarjo")

    # Baca data CSV
    df = pd.read_csv("data/data_jalan_rusak.csv")

    # Inisialisasi peta
    m = folium.Map(location=[-7.4498, 112.7015], zoom_start=14)

    # Tambahkan titik marker
    for _, row in df.iterrows():
        if row['hasil'] == "jalan_lubang":
            warna = "red"
        elif row['hasil'] == "jalan_retak":
            warna = "orange"
        elif row['hasil'] == "jalan_tidak_rusak":
            warna = "green"
        else:
            warna = "blue"  # fallback kalau ada label aneh

        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=row['hasil'],
            icon=folium.Icon(color=warna)
        ).add_to(m)

    # Tampilkan peta di Streamlit
    st_data = st_folium(m, width=700, height=500)
