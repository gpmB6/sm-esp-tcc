from machine import Pin, ADC, PWM
from config import *
from utils import *
import utime, secrets, urequests, sys

#define as variaveis  
sensorVal = 0
actuatorVal = 0
buttonVal = 0
lastButtonVal = 0
buttonCounter = 0
trainingNum = 0
#define as variaveis booleanas
buttonPressed = False
buttonHeld = False
trainingDone = False

ELEMENT_COUNT_MAX = 50
sensorArray = [0] * ELEMENT_COUNT_MAX
actuatorArray = [0] * ELEMENT_COUNT_MAX

print('\nSmartMotors em execucao\n')
led.on()

while True:
    buttonVal = Pin(buttonPin).value()
    sensorVal = getSensor()
    actuatorVal = getCtrl()

    buttonHeld = (not buttonVal and lastButtonVal and buttonCounter > 15)
    buttonPressed = (not buttonVal and lastButtonVal and not buttonHeld)

    if buttonHeld:
        trainingDone = True
        led.off()
        print("Botao 1 pressionado, aprendizagem finalizada.")
        for i in range(trainingNum):
          dados = {'value1':actuatorArray[i], 'value2':sensorArray[i]} 
          request_headers = {'Content-Type': 'application/json'}
          request = urequests.post(
            'http://maker.ifttt.com/trigger/inserir/with/key/' + secrets.api_key,
            json=dados,
            headers=request_headers)
          
          print(request.text)
          request.close()
          
        print('\nProcedimento concluido!')
        print('\nSmartMotors treinado. Se deseja retornar ao menu, pressione o Botao 2')
        buttonCounter = 0
        
    if buttonVal:
        buttonCounter += 1
    else:
        buttonCounter = 0

    if trainingDone:
        closestPos = 0
        minDiff = abs(sensorArray[0] - sensorVal)
        for i in range(trainingNum):
            if abs(sensorArray[i] - sensorVal) < minDiff:
                minDiff = abs(sensorArray[i] - sensorVal)
                closestPos = i
        writeActuator(actuatorArray[closestPos])
        utime.sleep_ms(30)

    elif buttonPressed:
        sensorArray[trainingNum] = sensorVal
        actuatorArray[trainingNum] = actuatorVal
        trainingNum += 1
    
    button2Val = Pin(button2Pin).value()
    if button2Val:
        print("Retornando...")
        logic_state2 = True
        break

    #se ainda estah treinando, mas o botao estah solto
    else:
        #altera o valor do atuador (muda de posicao durante o treinamento)
        writeActuator(actuatorVal)

    utime.sleep_ms(30)
    lastButtonVal = buttonVal
    
if logic_state2:
    exec(open('main.py').read())
