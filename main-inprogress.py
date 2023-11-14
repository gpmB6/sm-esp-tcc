import urequests
import sys

# HEADER DO SMARTMOTORS IFRS

def exibir_menu():
  print('Escolha uma opcao:')
  print('1. Executar o SmartMotors')
  print('2. Inserir manualmente um treinamento')
  print('3. Escolher um treinamento anterior')
  print('4. Sair')

# FUNCAO 1
# EXECUTA O CODIGO DO SMART MOTORS

# FUNCAO 2
# PERMITE INSERIR MANUALMENTE UM TREINAMENTO

# FUNCAO 3
# PERMITE ESCOLHER UM TREINAMENTO ANTERIOR

def consulta_treinamento():
  print('Obtendo lista de treinamentos...')
  #URL do sheetsu
  url = "https://sheetsu.com/apis/v1.0su/52d37fb77dc7"
  #utiliza o urequests para pegar o conteúdo da URL
  retorno = urequests.get(url)
  #coloca esse conteúdo na variavel lista como json
  lista = retorno.json()
  #imprime tudo que a API retornou
  print("\nLista dos ultimos treinamentos:\n\n", lista)
  print('\n####################################\n')
  print('1. Selecionar um treinamento anterior para executar')
  print('2. Voltar ao menu anterior')
  
  consulta_treinamento = input("O que deseja fazer? ")
  
  if consulta_treinamento == "1":
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
    print('Agora tenho que mandar esses dados pra executar')
    retorno.close()

  else:
    print('Voltando ao menu principal...\n')
    main()
# FUNCAO 4
# SAIR DO PROGRAMA

# caso queira acessar por meio da Data (ou horario)
#for i in range(len(lista)):
#  if lista[i]['Data'] == '13/11/2023':
#    print(f'Parametro: {lista[i]['Motor']} no motor')
#    print(f'Parametro: {lista[i]['Sensor']} no sensor')
# print('\n####################################\n')

def main():
    while True:
        exibir_menu()
        
        opcao = input("\nEscolha uma opcao: ")
        
        if opcao == "1":
            print('fazer executar o codigo do smartmotors')
            #executar_sm()
        elif opcao == "2":
            print('fazer inserir manualmente com ifttt')
            #exibir_tarefas()
        elif opcao == "3":
            print('fazer consultar treinamentos anteriores')
            consulta_treinamento()
        elif opcao == "4":
            print('Saindo...')
            sys.exit()
        else:
            print("Opção invalida...")

if __name__ == "__main__":
    main()
