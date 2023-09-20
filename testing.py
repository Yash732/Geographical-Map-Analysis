#district.geojson
import streamlit as st
import folium
import pandas as pd
from streamlit_folium import folium_static
st.set_page_config(layout ="wide")
json1 = f"district.geojson"

m = folium.Map(location=[10.1,76.6],tiles='OpenStreetMap', name="Light Map",
               zoom_start=8, attr="My Data attribution")

keral_data = f"dummyWasteData2.csv"
kerala_data = pd.read_csv(keral_data)

choice = ['Resultant']
choice_selected = st.selectbox("Select choice", choice)

folium.Choropleth(
    geo_data=json1,
    name="choropleth",
    data=kerala_data,
    columns=["DT_CEN_CD",choice_selected],
    key_on="feature.properties.DT_CEN_CD",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=.1,
    legend_name=choice_selected
).add_to(m)
folium.features.GeoJson('district.geojson',name="DISTRICT", popup=folium.features.GeoJsonPopup(fields=["DISTRICT"])).add_to(m)

folium_static(m, width=1600, height=950)