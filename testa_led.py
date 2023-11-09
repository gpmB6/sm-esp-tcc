# Testa se o led está funcional #

# Led:
# GND3 e GPIO12(D6)

from machine import Pin
from time import sleep

print('##Testando Led##')

led = Pin(12, Pin.OUT)

for i in range(2):
  print('Led acende')
  led.on()
  sleep(2)
  print('Led apaga')
  led.off()
  sleep(2)
