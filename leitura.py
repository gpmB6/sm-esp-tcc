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
#pega o tamanho da lista pra informar ao usuario
tamanho = str(len(lista))

print('\n\nEscolha um dos treinamentos de 0 a ' + str(len(lista)) + ':')
escolhe = input("Escolhe: ")
print(escolhe)

inputa = 1
conjunto = lista[inputa]
print(conjunto)
#conjunto_escolhido = lista[escolha]
#print(conjunto_escolhido)

#print('\n####################################\n')

# de toda a lista, pega um parametro do motor:
# usa o tamanho da lista para localizar o paramtro desejado
#for i in range(len(lista)):
#  if lista[i]['Data'] == '13/11/2023':
#    print(f'Parametro: {lista[i]['Motor']} no motor')
#    print(f'Parametro: {lista[i]['Sensor']} no sensor')

#parei aqui
# for i in range(tamanho):
#  if lista[i]['Data'


print('\n####################################\n')

#escolha = input("\nEscolha uma posicao: ")

# tipo str
# person = '{"name": "Bob", "languages": ["English", "French"]}'
# tipo dict
# person_dict = ujson.loads(person)
# print( person_dict)
# print("tipo do person_dict", type(person_dict))
# print(person_dict['languages'])

retorno.close()
