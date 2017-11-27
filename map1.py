# Folium is a Python Library that enables you to create different types of Leaflet maps
import folium
# Pandas is a Python package providing fast, flexible, and expressive data structures designed to make working with “relational” or “labeled” data both easy and intuitive.
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(el)+" m",
    fill_color=color_producer(el), fill=True,  color = 'grey', fill_opacity=0.7))

fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
	style_function=lambda x: {'fillColor':'green'}))

map.add_child(fg)

map.save("Map1.html")