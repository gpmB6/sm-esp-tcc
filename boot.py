#Funções relacionadas ao sistema operacional, manipulação de arquivos / diretorios
import uos
#Leitura e gravacao de arquivos
import os
#Funções para interagir com o hardware, como pinos GPIO
import machine
#Possibilita acessar variaveis / funcoes do interpretador
import sys
#Funcoes relacionadas ao ESP, como controle do modo de depuracao (debug)
import esp
#Funcoes com tempo
import time
#Conversoes entre binarios e ascii
import ubinascii
esp.osdebug(None)
#Ativa a rede, o WebREPL, o arquivo com chaves e a biblioteca externa UREQUESTS para manipular URLs
import network, webrepl, secrets, urequests
#Controle de coleta de lixo
import gc
gc.collect()

#Conecta a rede
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(secrets.ssid, secrets.senha)

while station.isconnected() == False:
  pass

print('Conectado.')
print(station.ifconfig())

print("""

 $$$$$$\                                     $$\           $$\      $$\            $$\                                   
$$  __$$\                                    $$ |          $$$\    $$$ |           $$ |                                  
$$ /  \__|$$$$$$\$$$$\   $$$$$$\   $$$$$$\ $$$$$$\         $$$$\  $$$$ | $$$$$$\ $$$$$$\    $$$$$$\   $$$$$$\   $$$$$$$\ 
\$$$$$$\  $$  _$$  _$$\  \____$$\ $$  __$$\\_$$  _|        $$\$$\$$ $$ |$$  __$$\\_$$  _|  $$  __$$\ $$  __$$\ $$  _____|
 \____$$\ $$ / $$ / $$ | $$$$$$$ |$$ |  \__| $$ |          $$ \$$$  $$ |$$ /  $$ | $$ |    $$ /  $$ |$$ |  \__|\$$$$$$\  
$$\   $$ |$$ | $$ | $$ |$$  __$$ |$$ |       $$ |$$\       $$ |\$  /$$ |$$ |  $$ | $$ |$$\ $$ |  $$ |$$ |       \____$$\ 
\$$$$$$  |$$ | $$ | $$ |\$$$$$$$ |$$ |       \$$$$  |      $$ | \_/ $$ |\$$$$$$  | \$$$$  |\$$$$$$  |$$ |      $$$$$$$  |
 \______/ \__| \__| \__| \_______|\__|        \____/       \__|     \__| \______/   \____/  \______/ \__|      \_______/ 
                                                                                                                         
                                                                                                                         
                                                                                                                         
$$$$$$\ $$$$$$$$\ $$$$$$$\   $$$$$$\        $$$$$$$\                                                                     
\_$$  _|$$  _____|$$  __$$\ $$  __$$\       $$  __$$\                                                                    
  $$ |  $$ |      $$ |  $$ |$$ /  \__|      $$ |  $$ | $$$$$$\   $$$$$$\                                                 
  $$ |  $$$$$\    $$$$$$$  |\$$$$$$\        $$$$$$$  |$$  __$$\  \____$$\                                                
  $$ |  $$  __|   $$  __$$<  \____$$\       $$  ____/ $$ /  $$ | $$$$$$$ |                                               
  $$ |  $$ |      $$ |  $$ |$$\   $$ |      $$ |      $$ |  $$ |$$  __$$ |                                               
$$$$$$\ $$ |      $$ |  $$ |\$$$$$$  |      $$ |      \$$$$$$  |\$$$$$$$ |                                               
\______|\__|      \__|  \__| \______/       \__|       \______/  \_______|                                               
                                                                                                                         
                                                                                                                         
                                                                                                                         
""")

webrepl.start()
