from machine import Pin, ADC, PWM
#from smart import read_sensor, getSensor, getCtrl, writeActuator

sensorPort = 16
sens = Pin(sensorPort, Pin.OUT)
potPin = 5
pot = Pin(potPin, Pin.OUT)
pot.off()
sens.on()
analog = ADC(0)
servoPin = 14
servo = PWM(Pin(servoPin), freq=50, duty=0)

ELEMENT_COUNT_MAX_READ = 3
sensArray = [0] * ELEMENT_COUNT_MAX_READ
actArray = [0] * ELEMENT_COUNT_MAX_READ

sensVal = 0
motorVal = 0
readingNum = 0

trainingDone = False

def map_range(value, from_low, from_high, to_low, to_high):
    from_range = from_high - from_low
    to_range = to_high - to_low
    scaled_value = (value - from_low) / from_range
    mapped_value = to_low + (scaled_value * to_range)
    return int(mapped_value)

def read_sensor(sensor_pin):
    return analog.read()

def getSensor():
    pot.off()
    sens.on()
    return read_sensor(sens)

def getCtrl():
    sens.off()
    pot.on()
    return read_sensor(pot)

def writeActuator(val):
    mapped_val = map_range(val, 0, 948, 0, 180)
    servo.duty(mapped_val)

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
    
    while True: 
        sensVal = getSensor()
        motorVal = getCtrl()
        escolha = int(input('\n\nEscolha um conjunto de treinamentos de 0 a ' + tamanho + ':'))
        conjunto = lista[escolha]
        print('\n', conjunto)
        print('\n####################################\n')
        # de toda a lista, pega um parametro do motor:
        # usa o tamanho da lista para localizar o paramtro desejado
        print('\nOs parametros selecionados sao:\n')
        print('Motor:', lista[escolha]['Motor'])
        print('Sensor:', lista[escolha]['Sensor'])
        
        # atribui às variáveis os valores selecionados, convertendo-os para inteiros
        motorVal = int(lista[escolha]['Motor'])
        sensVal = int(lista[escolha]['Sensor'])
        
        sensArray[readingNum] = sensVal
        print('readingNumcheck :', sensArray[readingNum]) 
        actArray[readingNum] = motorVal
        print('readingNumcheck :', actArray[readingNum])
      
        readingNum += 1
        
        escolha2 = int(input('\nSelecione outro conjunto de parametros: '))
        if escolha2 == -1:
          break
        
        else:
          conjunto2 = lista[escolha2]
          print('\n', conjunto2)
          print('\n####################################\n')
          
          print('\nOs parametros selecionados sao:\n')
          print('Motor:', lista[escolha2]['Motor'])
          print('Sensor:', lista[escolha2]['Sensor'])
          
          motorVal = int(lista[escolha2]['Motor'])
          sensVal = int(lista[escolha2]['Sensor'])
          
          sensArray[readingNum] = sensVal
          actArray[readingNum] = motorVal
          
          print('readingNumcheck :', sensArray[readingNum])
          print('readingNumcheck :', actArray[readingNum])
          
          print('\nEnviando parametro para execucao...\n')
          print('\n\n \n\n')
          print('teste motorVal: ', motorVal)
          print('teste actArray[closestPos]: ', actArray[closestPos]) 
          print('\n\n \n\n')
          trainingDone = True
        
          if trainingDone:
            closestPos = 0
            minDiff = abs(sensArray[0] - sensVal)
            for i in range(readingNum):
              if abs(sensArray[i] - sensVal) < minDiff:
                  minDiff = abs(sensArray[i] - sensVal)
                  closestPos = i
            writeActuator(actArray[closestPos])
      
            print('Array 1: ', sensArray)
            print('Array 2: ', actArray)
            print('Treinamento passado com sucesso.\n\n')
            
          else: 
            writeActuator(motorVal)
      
else:
    print('Escolheu voltar para o menu principal\n')
    main()
