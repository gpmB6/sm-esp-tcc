from config import *
from utils import *
import utime, urequests, secrets, sys

sensVal = 0
motorVal = 0
readingNum = 0

logic_state2 = False

print('\nObtendo lista de treinamentos...')

#URL do sheetsu
url = secrets.url

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
  tamanho = str(len(lista))
  print('\nA lista contem: ' + tamanho + ' conjuntos.')
  quant = int(input('\nCerto. Quantos conjuntos de treinamento deseja utilizar? '))
  
  while int(quant) > int(tamanho):
    print('quantidade eh maior do que o numero de conjuntos disponiveis\n')
    quant = int(input('Quantos conjuntos deseja? '))

  ELEMENT_COUNT_MAX_READ = quant
  sensArray = [0] * ELEMENT_COUNT_MAX_READ
  actArray = [0] * ELEMENT_COUNT_MAX_READ
    
  for i in range(quant):
    escolha = int(input('\n\nEscolha um conjunto de treinamentos de 1 a ' + tamanho + ':'))
    #como a primeira posicao comeca no 0, vamos subtrair em 1 a escolha do usuario
    escolha -= 1
    conjunto = lista[escolha]
    print('\n', conjunto)
    # atribui às variáveis os valores selecionados, convertendo-os para inteiros
    motorVal = int(lista[escolha]['Motor'])
    sensVal = int(lista[escolha]['Sensor'])
    sensArray[readingNum] = sensVal
    actArray[readingNum] = motorVal
    readingNum += 1
    
  print('\nSmartMotors treinado. \nSe deseja retornar ao menu, pressione o Botao 2')
   
  while True:
    sensVal = getSensor()
    motorVal = getCtrl()
    button2Val = Pin(button2Pin).value()
  
    closestPos = 0
    minDiff = abs(sensArray[0] - sensVal)
    for i in range(readingNum):
      if abs(sensArray[i] - sensVal) < minDiff:
        minDiff = abs(sensArray[i] - sensVal)
        closestPos = i
    writeActuator(actArray[closestPos])
    utime.sleep_ms(30)
    if button2Val:
      print("Retornando...")
      logic_state2 = True
      break
      
if logic_state2 == True or consulta_treinamento == "2":
  exec(open('main.py').read())
