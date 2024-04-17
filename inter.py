import folium
map = folium.Map(location=[26.917352525602915, 80.70342311181138], zoom_start=15)
folium.CircleMarker(location=[26.917352525602915, 80.70342311181138], radius=50, popup="anyplace").add_to(map)
folium.Marker([26.917352525602915, 80.70342311181138], popup = "unknown place").add_to(map)
folium.Marker([26.782735771895954, 79.02783602026649], popup = "place").add_to(map)
folium.Marker([28.5019207, 77.2297379], popup = "place").add_to(map)
folium.PolyLine(locations=[(26.782735771895954, 79.02783602026649),[26.917352525602915, 80.70342311181138]], line_opacity = 0.6).add_to(map)

map.save("map.html")
