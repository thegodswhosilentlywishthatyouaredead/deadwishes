# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ds9gLvPUSqV13ELC8REyXLxUFcOfqMcz
"""

pip install streamlit_folium

import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium
import streamlit as st

# Title
st.title('Bazar Ramadan Locations in Kuala Lumpur 2025')

# Load the data
data = pd.read_csv('/content/bazar_ramadan_full_locations_2025_3.csv')

# Initialize the map centered around Kuala Lumpur
m = folium.Map(location=[3.1390, 101.6869], zoom_start=12)

# Add a marker cluster
marker_cluster = MarkerCluster().add_to(m)

# Add markers to the map
for idx, row in data.iterrows():
    lat, lon = map(float, row['GPS Coordinates'].split(','))
    popup_info = f"""
    <b>Location:</b> {row['Location']}<br>
    <b>Number of Stalls:</b> {row['Number of Stalls']}<br>
    <b>Remarks:</b> {row['Remarks']}
    """
    folium.Marker(
        location=[lat, lon],
        popup=folium.Popup(popup_info, max_width=300),
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(marker_cluster)

# Display the map in Streamlit
st_folium(m, width=700, height=500)