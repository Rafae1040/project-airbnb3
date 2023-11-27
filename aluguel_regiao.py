# Valor mais caro de aluguel de cada região

data_plot = data.loc[:,['price','neighbourhood_group']].groupby(['neighbourhood_group']).max().reset_index()
px.bar(data_plot, x='neighbourhood_group', y='price')


