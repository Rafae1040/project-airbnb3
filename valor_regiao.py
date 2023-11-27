# Menor valor de aluguel por região

data.loc[:,['latitude', 'neighbourhood_group',]].groupby(['neighbourhood_group']).min().reset_index()
