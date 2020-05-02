# Detlev Aschhoff info@vmais.de
# The MIT License (MIT)
#
# Copyright (c) 2020
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.




def tx433(data,tx_pin):
    sync=int(data[0])/1000000           # Zeit in microsekunden
    short=(int(data[1])-240)/1000000   # -240 us Korrektur for Pi2 b
    long= (int(data[2])-240)/1000000
    code=data[3]
      
        
    GPIO.output(tx_pin, GPIO.LOW)
    for t in range(10):
        GPIO.output(tx_pin, GPIO.HIGH)       #header
        time.sleep(short)

        for i in code:
          if i == '0':
            GPIO.output(tx_pin, GPIO.LOW)
            time.sleep(short)
            GPIO.output(tx_pin, GPIO.HIGH)
            time.sleep(long)
          elif i == '1':
            GPIO.output(tx_pin, GPIO.LOW)
            time.sleep(long)
            GPIO.output(tx_pin, GPIO.HIGH)
            time.sleep(short)
          else:
            continue
        GPIO.output(tx_pin, GPIO.LOW)        #Footer
        time.sleep(sync)
        GPIO.output(tx_pin, GPIO.HIGH)
        #time.sleep(0.05)
    GPIO.output(tx_pin, GPIO.LOW)            # Transmit off  
#---------------------------- Main -----------------------------------

import time
import socket
import sys
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
if len(sys.argv) > 1:
   uname = sys.argv[1]
   #state =sys.argv[2]

print("TX433: ",uname)

# lade config.py mit Devices Protokoll und Daten

from tx433_config import * # importiere config mit var Namen
GPIO.setup(tx_pin, GPIO.OUT) # GPIO as output

sys.path.append("./tx433_encoder")
dirs = os.listdir( "./tx433_encoder")
for prot in dirs:
  if prot[-3:]==".py":
    a=prot[:-3]   # Name des Dekodiermoduls aus Directory tx433_encoder
    locals()[a]=__import__(a)
    # erzeuge locale Variable aus String a => 
    # import modul mit Name aus Variable a

#---------------------------------------------------------------------
print("Start Tx433")
# Daten vom Device suchen
if uname!="rawdata":
  dev=devices[uname]
  bef=dev["prot"]+".code(dev)" # erkanntes Protokoll in bef
  data=eval(bef)   # eval => ausfueren von String bef als Befehl

else:
  dataraw=devices[uname] 
  data=dataraw["sync"],dataraw["short"],dataraw["long"],dataraw["code"]
print(data)
tx433(data,tx_pin)
  



