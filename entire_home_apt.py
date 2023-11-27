# Visualização dos 100 tipos de imoveis entire home/apt

colunas = ['room_type', 'latitude', 'longitude']
linhas = data.loc[:, 'room_type'] == 'Entire home/apt'

data_plot = data.loc[linhas, colunas].sample(100)

# Desenhar o mapa

map = folium.Map()

for index, location_info in data_plot.iterrows():
  folium.Marker([location_info['latitude'],
                 location_info['longitude']],
                popup=location_info['room_type']
                ).add_to(map)

map