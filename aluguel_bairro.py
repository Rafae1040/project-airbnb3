# Maior valor do aluguel por bairro e tipo de imovel?

data.loc[:,['price', 'neighbourhood', 'room_type']].groupby(['neighbourhood','room_type']).max().reset_index()

