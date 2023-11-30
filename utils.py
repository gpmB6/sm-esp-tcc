from config import *

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
    mapped_val = map_range(val, 0, 948, 40, 115)
    servo.duty(mapped_val)
