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
buttonPressed = 0
buttonHeld = 0
trainingDone = 0
sensorArray = [None] * element_count_max
actuatorArray = [None] * element_count_max

print('Iniciando a definicao de funcoes...')

# Funcoes
def estado_botao1():
  print('retorna o estado do botao1')

def estado_botao2():
  print('retorna o estado do botao2')

def estado_sensor():
  print('retorna o estado do sensor - valores de 49 a 966 no simulador VALIDAR')

def estado_potenciometro():
  print('retorna o estado do controle (potenciometro)')

def estado_motor():
  print('')
 
print('Definicao de funcoes concluida...')
 
# sintaxe da chamada da funcao
# estado_botoes()  

print('Validando os estados atuais...')

# Validacao do estado atual

estado_logico1 = botao1.value()
estado_logico2 = botao2.value()
#acrescentar linha que pega o estado do valor do sensor

print('Validacao de estados concluida...')
