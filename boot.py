# This file is executed on every boot (including wake-boot from deepsleep)
#//uos.dupterm(None, 1) # disable REPL on UART(0)

import uos, machine
import os
import esp
import time
#//from umqttsimple import MQTTClient
#import ubinascii
esp.osdebug(None)
#import webrepl
#webrepl.start()
import gc
gc.collect()


print("""\


  /$$$$$$                                      /$$           /$$      /$$             /$$                                  
 /$$__  $$                                    | $$          | $$$    /$$$            | $$                                  
| $$  \__/ /$$$$$$/$$$$   /$$$$$$   /$$$$$$  /$$$$$$        | $$$$  /$$$$  /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$   /$$$$$$$
|  $$$$$$ | $$_  $$_  $$ |____  $$ /$$__  $$|_  $$_/        | $$ $$/$$ $$ /$$__  $$|_  $$_/   /$$__  $$ /$$__  $$ /$$_____/
 \____  $$| $$ \ $$ \ $$  /$$$$$$$| $$  \__/  | $$          | $$  $$$| $$| $$  \ $$  | $$    | $$  \ $$| $$  \__/|  $$$$$$ 
 /$$  \ $$| $$ | $$ | $$ /$$__  $$| $$        | $$ /$$      | $$\  $ | $$| $$  | $$  | $$ /$$| $$  | $$| $$       \____  $$
|  $$$$$$/| $$ | $$ | $$|  $$$$$$$| $$        |  $$$$/      | $$ \/  | $$|  $$$$$$/  |  $$$$/|  $$$$$$/| $$       /$$$$$$$/
 \______/ |__/ |__/ |__/ \_______/|__/         \___/        |__/     |__/ \______/    \___/   \______/ |__/      |_______/ 
 /$$$$$$ /$$$$$$$$ /$$$$$$$   /$$$$$$        /$$$$$$$                                                                      
|_  $$_/| $$_____/| $$__  $$ /$$__  $$      | $$__  $$                                                                     
  | $$  | $$      | $$  \ $$| $$  \__/      | $$  \ $$  /$$$$$$   /$$$$$$                                                  
  | $$  | $$$$$   | $$$$$$$/|  $$$$$$       | $$$$$$$/ /$$__  $$ |____  $$                                                 
  | $$  | $$__/   | $$__  $$ \____  $$      | $$____/ | $$  \ $$  /$$$$$$$                                                 
  | $$  | $$      | $$  \ $$ /$$  \ $$      | $$      | $$  | $$ /$$__  $$                                                 
 /$$$$$$| $$      | $$  | $$|  $$$$$$/      | $$      |  $$$$$$/|  $$$$$$$                                                 
|______/|__/      |__/  |__/ \______/       |__/       \______/  \_______/                                                 
                                                                                                                           

""")

def connect():
  import network
  import secrets
  print('Iniciando conexao na rede:', secrets.SSID)
  sta_if = network.WLAN(network.STA_IF)
  if not sta_if.isconnected():
    sta_if.active(True)
    sta_if.connect(secrets.SSID, secrets.SENHA)
    while not sta_if.isconnected():
      time.sleep(3) #espera
      print('Ainda nao conectado, valide se no secrets.py a rede desejada esta descomentada.')
      print('Após ajustar o arquivo, pode ser necessario um reboot: Ctrl + D')
  print('Configuracao bem sucedida:\n', sta_if.ifconfig())
  
connect()
