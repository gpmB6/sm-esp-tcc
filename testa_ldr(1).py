# Testa se o sensor está funcional ## Sensor (LDR):# GND1, GPIO16(D0) e A0 (compartilhada com o potenciometro)from machine import Pin, ADCfrom time import sleepsens = Pin(16, Pin.OUT)analog = ADC(0)while True:  pot.off()  sens.on()  analog_value = analog.read()  print(analog_value)  sleep(1)