# Testa se o motor está funcional #

# Motor (servo):
# GND1, VCC3.3_2 e GPIO14(D5)

from machine import Pin, PWM
from time import sleep

servo = PWM(Pin(14), freq=50)

# Minimum position (angle 0)
servo.duty(40)

# Maximun position (angle 180)
servo.duty(40)

# center position (angle 90)
servo.duty(40)

# swipping servo
step = 2
for i in range (40, 115, step):
    servo.duty(i)
    sleep (0.1)
    step = -1*step

for i in range (115, 40, step):
    servo.duty(i)
    sleep (0.1)
    servo.duty(77)
