# Visualização com os imoveis mais baratos por região?

colunas = ['price', 'neighbourhood_group','latitude', 'longitude']

colunas_groupby = 'neighbourhood_group'
data_plot = data.loc[:, colunas].groupby(colunas_groupby).min().reset_index()

data_plot

# desenhar o mapa
map = folium.Map()

for index, location_info in data_plot.iterrows():
  folium.Marker([location_info['latitude'],
                location_info['longitude']],
                popup=location_info[['neighbourhood_group', 'price']]
                ).add_to(map)
map