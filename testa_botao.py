# Testa se os botoes estao funcionais #

# Botao1:
# 3V e GPIO4(D2)
# Botao2:
# 3V e GPIO0(D3)

from machine import Pin
from time import sleep

print('##Testando Botao##')

push_button1 = Pin(4, Pin.IN)
push_button2 = Pin(0, Pin.IN)

while True:
  logic_state1 = push_button1.value()
  logic_state2 = push_button2.value()
  if logic_state1 == True:
    print('botao 1 apertado')
    sleep(1)
  elif logic_state2 == True:
    print('botao 2 apertado')
    sleep(1)
  else:
    print('botoes nao apertados')
    sleep(1)
