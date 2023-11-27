# Visualização em um mapa dos tipos de imoveis em cada reagiao

data_plot = data.loc[:,['price','neighbourhood_group']].groupby(['neighbourhood_group']).max().reset_index()
px.bar(data_plot, x='neighbourhood_group', y='price')

# conjunto de dados (filtragem linhas e colunas)
colunas = ['neighbourhood_group', 'room_type', 'latitude', 'longitude']
data_plot = data.loc[:, colunas].sample(100)

# criar uma nova coluna chamada 'color'

data_plot.loc[:, 'color'] = 'NA'

linhas_private_room = data_plot.loc[:, 'room_type'] == 'Private room'
linhas_entire_apt = data_plot.loc[:, 'room_type'] == 'Entire home/apt'
linhas_shared_room = data_plot.loc[:, 'room_type'] == 'Shared room'

data_plot.loc[linhas_private_room,'color'] = 'darkgreen'
data_plot.loc[linhas_entire_apt, 'color'] = 'darkred'
data_plot.loc[linhas_shared_room, 'color'] = 'purple'

# desenhar mapa
map = folium.Map()

for index , location_info in data_plot.iterrows():
  folium.Marker(
      [location_info['latitude'], location_info['longitude']],
      popup=location_info['neighbourhood_group'],
      icon=folium.Icon(color=location_info['color'])
  ).add_to(map)
map
