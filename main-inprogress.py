import urequests
import sys
import webrepl
import smart
from smart import sensorArray, trainingNum, actuatorArray
import secrets

def exibir_menu():
  print('Escolha uma opcao:')
  print('1. Executar o SmartMotors')
  print('2. Inserir manualmente um treinamento')
  print('3. Escolher um treinamento anterior')
  print('4. Sair')

# FUNCAO 1
# EXECUTA O CODIGO DO SMART MOTORS
def executar_sm():
  exec(open('smart.py').read())

# FUNCAO 2
# PERMITE INSERIR MANUALMENTE UM TREINAMENTO
def insere_treinamento():
  print('\nPreparando para insercao manual...')


  try:
    motor_inserido = int(input('\nInforme o valor do motor: '))
    sensor_inserido = int(input('\nInforme o valor do sensor: '))
  
    dados = {'value1':motor_inserido, 'value2':sensor_inserido}
    print(dados)
    request_headers = {'Content-Type': 'application/json'}

    request = urequests.post(
    'http://maker.ifttt.com/trigger/inserir/with/key/' + secrets.api_key,
    json=dados,
    headers=request_headers)

    print(request.text)
    print('\nProcedimento concluido!\n')
    request.close()

  except OSError as e:
    print('Falha ao inserir os dados. Por favor, tente novamente mais tarde.')


  print('\n####################################\n')

  print('1. Inserir mais um treinamento')
  print('2. Voltar ao menu anterior')
  
  treinamento_manual = input("O que deseja fazer? ")
  
  if treinamento_manual == "1":
    print('Ok, vamos inserir um novo treinamento')
    insere_treinamento()
    
  else:
    print('Escolheu voltar para o menu principal\n')
    main()
    
# FUNCAO 3
# PERMITE ESCOLHER UM TREINAMENTO ANTERIOR

def consulta_treinamento():
  print('\nObtendo lista de treinamentos...')
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
    escolha = int(input('\n\nEscolha um dos treinamentos de 0 a ' + tamanho + ':'))
    conjunto = lista[escolha]
    print('\n', conjunto)
    print('\n####################################\n')
    # de toda a lista, pega um parametro do motor:
    # usa o tamanho da lista para localizar o paramtro desejado
    print('\nOs parametros selecionados sao:\n')
    print('Motor:', lista[escolha]['Motor'])
    print('Sensor:', lista[escolha]['Sensor'])
    print('\nEnviando parametro para execucao...\n')
    moto_val = lista[escolha]['Motor']
    sens_val = lista[escolha]['Sensor']
    moto_convert = int(moto_val)
    sens_convert = int(sens_val)
    sensorArray[trainingNum] = sens_convert
    actuatorArray[trainingNum] = int(moto_val)
    closestPos = 0
    minDiff = abs(sensorArray[0] - sens_convert)
    for i in range(trainingNum):
        if abs(sensorArray[i] - sens_convert) < minDiff:
            minDiff = abs(sensorArray[i] - sens_convert)
            closestPos = i
    writeActuator(actuatorArray[closestPos])

  else:
    print('Escolheu voltar para o menu principal')
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
            print('Escolheu executar o SmartMotors. Programa em execucao...')
            executar_sm()
        elif opcao == "2":
            insere_treinamento()
            #exibir_tarefas()
        elif opcao == "3":
            consulta_treinamento()
        elif opcao == "4":
            print('Saindo...')
            sys.exit()
        else:
            print("Opção invalida...")

if __name__ == "__main__":
    main()
