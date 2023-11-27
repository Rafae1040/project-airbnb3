# Media de preço de aluguel Região?

data.loc[:,['price', 'neighbourhood_group']].groupby(['neighbourhood_group']).mean().reset_index()
