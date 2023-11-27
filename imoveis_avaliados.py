# Imoveis que possuem o maior numero de avaliações?

colunas = ['number_of_reviews', 'neighbourhood_group', 'latitude', 'longitude']

colunas_groupby = 'neighbourhood_group'
data_plot = data.loc[:, colunas].groupby( colunas_groupby ).max().reset_index()


data_plot

# Desenhar o mapa
map = folium.Map()

for index, location_info in data_plot.iterrows():
  folium.Marker([location_info['latitude'],
                 location_info['longitude']],
                popup=location_info['neighbourhood_group']
                ).add_to(map)
map
