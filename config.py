from machine import Pin, ADC, PWM

#compartilham o input no ADC(0)
sensorPort = 16
potPin = 5
analog = ADC(0)
#demais portas e definicoes
buttonPin = 4
button2Pin = 0
ledPin = 12
servoPin = 14
servo = PWM(Pin(servoPin), freq=50, duty=0)
led = Pin(ledPin, Pin.OUT)
sens = Pin(sensorPort, Pin.OUT)
pot = Pin(potPin, Pin.OUT)
button2 = Pin(button2Pin, Pin.IN)
