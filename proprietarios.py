# Distribuição de proprietarios por imoveis?

colunas = ['host_id', 'calculated_host_listings_count']

linhas = data.loc[:, 'calculated_host_listings_count'] <= 10

data_plot = data.loc[linhas, 'calculated_host_listings_count']

plt.hist( data_plot, bins=10 );
plt.title( 'A distribuição de proprietário por imóveis cadastrados');
plt.xlabel( 'Quantidade de Imóveis Cadastrados' );
plt.ylabel( 'Quantidade de Proprietários' );
