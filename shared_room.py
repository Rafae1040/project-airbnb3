# Visualização dos 100 imoveis tipo shared room.

colunas = ['room_type', 'latitude', 'longitude']
linhas = data.loc[:, 'room_type'] == 'Shared room'

data_plot = data.loc[linhas, colunas].sample(100)

# Desenhar o mapa

map = folium.Map()

for index, location_info in data_plot.iterrows():
  folium.Marker([location_info['latitude'],
                 location_info['longitude']],
                popup=location_info['room_type']
                ).add_to(map)

map