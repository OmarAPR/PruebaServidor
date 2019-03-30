import os
import time
import serial
import string
import pynmea2

#loop fpr the GPS

while True:
   
    ser = serial.Serial("/dev/ttyS0",9600)
    
    dataout = pynmea2.NMEAStreamReader()
    newdata = ser.readline()

    if newdata[0:6] == '$GPGGA':
        newmsg = pynmea2.parse(newdata)
        lat = newmsg.latitude
        print (lat)
        lng = newmsg.longitude
        print (lng)
        cadena=str(lat)+','+str(lng)
        print(cadena)
        f=open('prueba.json','w')
        f.write(cadena)
        f.close()
        break
        time.sleep(10)
        
