


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

#Encoder fuer PT8A977 Chip ( Fernsteuerchip )

#Sync 4* 1500us high 500us low
#Data  n* 500us 500us    hier 40
#Footer 4* Sync 2* Data

def code(dev):

    sync=(1500-240)/1000000           # Zeit in microsekunden
    short=(500-240)/1000000           # Zeit in microsekunden
    code=int(dev["code"])
    tx_pin=dev["tx_pin"]

    #
    import time
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.output(tx_pin, GPIO.LOW)
    
    for x in range(5):
        for i in range(4):          # Sync 4* 1500 500
            GPIO.output(tx_pin, GPIO.HIGH)
            time.sleep(sync)
            GPIO.output(tx_pin, GPIO.LOW)
            time.sleep(short)
            
        for i in range(code):       # Code n*  500 500
            GPIO.output(tx_pin, GPIO.HIGH)
            time.sleep(short)
            GPIO.output(tx_pin, GPIO.LOW)
            time.sleep(short)
            
        for i in range(4):          # Footer  4* 1500 500    4* 500 500
            GPIO.output(tx_pin, GPIO.HIGH)
            time.sleep(sync)
            GPIO.output(tx_pin, GPIO.LOW)
            time.sleep(short)
            
        for i in range(4):
            GPIO.output(tx_pin, GPIO.HIGH)
            time.sleep(short)
            GPIO.output(tx_pin, GPIO.LOW)
            time.sleep(short)

    GPIO.output(tx_pin, GPIO.LOW)
    return "500","500","500","0101" # Dummy Return for Output















