from machine import Pin, ADC, PWM
import utime, secrets

#compartilham o input no ADC(0)
sensorPort = 16
potPin = 5
analog = ADC(0)

buttonPin = 4
button2Pin = 0
ledPin = 12
servoPin = 14
servo = PWM(Pin(servoPin), freq=50, duty=0)
sensorVal = 0
actuatorVal = 0
buttonVal = 0
lastButtonVal = 0
buttonCounter = 0
trainingNum = 0

buttonPressed = False
buttonHeld = False
trainingDone = False

ELEMENT_COUNT_MAX = 50
sensorArray = [0] * ELEMENT_COUNT_MAX

actuatorArray = [0] * ELEMENT_COUNT_MAX

led = Pin(ledPin, Pin.OUT)
sens = Pin(sensorPort, Pin.OUT)
pot = Pin(potPin, Pin.OUT)

def setup():
    print("Running setup")

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

while True:
    buttonVal = Pin(buttonPin).value()
    #button2Val = Pin(button2Pin).value()
    sensorVal = getSensor()
    actuatorVal = getCtrl()

    buttonHeld = (not buttonVal and lastButtonVal and buttonCounter > 15)
    buttonPressed = (not buttonVal and lastButtonVal and not buttonHeld)

    if buttonHeld:
        trainingDone = True
        led.off()
        print("Botao pressionado")
        print("Training Num: ", trainingNum)
        for i in range(1, trainingNum):
          #print('Valore da posicao do sensor: ', sensorArray[i])
          #print('Valores da posicao do motor: ', actuatorArray[i])
          dados = {'value1':actuatorArray[i], 'value2':sensorArray[i]} 
          #print('\n', dados)
          request_headers = {'Content-Type': 'application/json'}
          request = urequests.post(
            'http://maker.ifttt.com/trigger/inserir/with/key/' + secrets.api_key,
            json=dados,
            headers=request_headers)
          
          print(request.text)
          request.close()
          
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

    elif buttonPressed:
        led.on()
        sensorArray[trainingNum] = sensorVal
        actuatorArray[trainingNum] = actuatorVal
        trainingNum += 1

    else:
        writeActuator(actuatorVal)

    utime.sleep_ms(30)
    lastButtonVal = buttonVal


