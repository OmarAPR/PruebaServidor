import os
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(20,GPIO.IN)
GPIO.setup(21,GPIO.IN)
while True:
    input1=GPIO.input(20)
    input2=GPIO.input(21)
    if(input1 == True and input2==True):
        os.system('python get_gps.py')
        os.system('python codigo_cliente.py')
        while True:
            os.system('python get_gps.py')
            os.system('python cliente_ubicacion.py')
            time.sleep(5)
            
    
