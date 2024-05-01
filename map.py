import folium
import pandas as pd

# Reading the map data from the csv file
data = pd.read_csv("Volcanoes.csv")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="cartodb positron")

# Adding Future group
fg = folium.FeatureGroup(name="My Map")

# Adding Marker and change icon colour
for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el) + " m", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")
