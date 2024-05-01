import folium
import pandas as pd

data = pd.read_csv("Volcanoes.csv")
lat = list(data["LAT"])
lon = list(data["LON"])
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="cartodb positron")

# Adding Future group
fg = folium.FeatureGroup(name="My Map")

# Adding Marker and change icon colour
for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt, ln], popup="I'm a marker", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")
