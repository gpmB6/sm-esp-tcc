import urequests

#URL do sheetsu
url = "https://sheetsu.com/apis/v1.0su/52d37fb77dc7"

#utiliza o urequests para pegar o conteúdo da URL
retorno = urequests.get(url)

#coloca esse conteúdo na variavel lista como json
lista = retorno.json()

#imprime tudo que a API retornou
print("\nLista dos ultimos treinamentos:\n\n", lista)

print('\n####################################\n')

# pega o conjunto de elementos da posição solicitada da lista
# modificar para ser input do cliente selecionar a posicao da lista
# input = 1
# conjunto = lista[input]
# print(conjunto)

#pega o tamanho da lista pra informar ao usuario
tamanho = str(len(lista)-1)

escolha = int(input('\n\nEscolha um dos treinamentos de 0 a ' + tamanho + ':\n'))

conjunto = lista[escolha]
print(conjunto)

print('\n####################################\n')

# de toda a lista, pega um parametro do motor:
# usa o tamanho da lista para localizar o paramtro desejado
print('\n\nOs parametros da lista selecionadas sao:\n')
print('Motor:', lista[escolha]['Motor'])
print('Sensor:', lista[escolha]['Sensor'])

# caso queira acessar por meio da Data (ou horario)
#for i in range(len(lista)):
#  if lista[i]['Data'] == '13/11/2023':
#    print(f'Parametro: {lista[i]['Motor']} no motor')
#    print(f'Parametro: {lista[i]['Sensor']} no sensor')

print('\n####################################\n')

retorno.close()
