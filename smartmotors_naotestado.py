# Botao1: 3V e GPIO4(D2)
# Botao2: 3V e GPIO0(D3)
# Led: GND3 e GPIO12(D6)
# Potenciometro: GND1, GPIO5(D1) e A0 (compartilhada com o sensor)
# Sensor (LDR): GND1, GPIO16(D0) e A0 (compartilhada com o potenciometro)
# Motor (servo): GND1, VCC3.3_2 e GPIO14(D5)

from machine import Pin, ADC, PWM
from time import sleep

# Definicao de variaveis
botao1 = Pin(4, Pin.IN)
botao2 = Pin(0, Pin.IN)
led = Pin(12, Pin.OUT)
sens = Pin(16, Pin.OUT)
pot = Pin(5, Pin.OUT)
analog = ADC(0)
servo = PWM(Pin(14), freq=50)

# Inteiros
trainingNum = 0
buttonCounter = 0
element_count_max = 50

# Booleanos
buttonPressed = False
buttonHeld = False
trainingDone = False
sensorArray = [None] * element_count_max
actuatorArray = [None] * element_count_max

print('Iniciando a definicao de funcoes...')

# Funcoes
def estado_botao1():
  print('retorna o estado do botao1')

def estado_botao2():
  print('retorna o estado do botao2')

def estado_sensor():
  #return(analogRead(sensorPort)); // 49 - 966
  print('retorna o estado do sensor - valores de 49 a 966 no simulador VALIDAR')

def estado_potenciometro():
  #return(analogRead(potPin)); // 0 - 1023
  print('retorna o estado do controle (potenciometro)')

def estado_motor():
  #void write Actuator(int val) //altera o estado do motor
    #val = map(val, 0, 1023, 0, 180); //mapeia valor de entrada (val-> 0 - 1023 para angulo dos servo 0 - 180 graus)
    #servo.write(val); //coloca o servo no angulo definido em val
  print('posiciona o motor no angulo definido em val')
  
print('Definicao de funcoes concluida...')
 
# sintaxe da chamada da funcao
# estado_botoes()  

print('Validando os estados atuais...')

# Validacao do estado atual

estado_logico1 = botao1.value()
estado_logico2 = botao2.value()
#acrescentar linha que pega o estado do valor do sensor

print('Validacao de estados concluida...')

# loop (main) ########
while(1):
  #pega o estado atual do botao 1
  buttonVal1 = estado_logico1 = botao1.value()
  #pega o estado atual do botao 2
  buttonVal2 = estado_logico2 = botao2.value()
  #pega o valor atual do sensor
  pot.off()
  sens.on()
  analog_value = analog.read()
  sensorVal = analog_value
  sleep(1)
  #pega o valor atual do potenciometro
  sens.off()
  pot.on()
  analog_value = analog_read()
  actuatorVal = analog_value
  sleep(1)
  
  #verifica o que deve ser feito
  #valida se algum botao foi pressionado
  #se o botao 2 for ativado
  if buttonVal2:
    trainingDone = True
    print('Botao 2 pressionado, treinamento concluido')
  
  if trainingDone:
    print('trainingDone verdadeiro, mudar os valores')
    #if trainingDone:
    #closestPos = 0
    #minDiff = abs(sensorArray[i] - sensorVal);
    #for (int i=0; i<trainingNum; i++){ // percorre o nro de amostras realizadas no treinamento (podia comecar na pos=1)
  	#if (abs(sensorArray[i] - sensorVal) < minDiff) { // encontra a menor diferenca entre estado atual e vetor
        #minDiff = abs(sensorArray[i] - sensorVal); // atualiza o valor da menor diferenca
        #closestPos = i; // atualiza a posicao com a menor diferenca
      #}
    #}
    #writeActuator(actuatorArray[closestPos]); // altera o atuador com o valor da posicao encontrada
  
  # AINDA EM TREINAMENTO  
  elif buttonVal1:
    print('Botao 1 pressionado, treinamento iniciado')
    sensorArray.append = sensorVal
    actuatorArray.append = actuatorVal
  else:
    print('Botoes nao pressionados, aguardando')
    print('Mudamos o valor do motor durante o treinamento')
    writeActuator(actuatorVal)
 
sleep(1)
print('dormiu 1 segundo')
lastButtonVal1 = buttonVal1
lastButtonVal2 = buttonVal2
