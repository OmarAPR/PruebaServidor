#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#      client.py
#
#      Copyright 2014 Recursos Python - www.recursospython.com
#
#
import time
from socket import socket

def main(n,s):
    
    
    
    while True:
        
        if(n==0):
            f = open("amor.jpeg", "rb")
        if(n==1):
            f = open("nene.jpeg", "rb")
        if(n==2):
            f = open("amor.jpeg", "rb")
        '''
        if(n==1):
            f = open("amor.jpeg", "rb")
        if(n==0):
            f = open("gemidos.mp3", "r")
        '''
        content = f.read(1024)
        while content:
            # Enviar contenido.
            s.send(content)
            content = f.read(1024)
        
        break
    
    
    # Se utiliza el caracter de código 1 para indicar
    # al cliente que ya se ha enviado todo el contenido.
    try:
        s.send(chr(1))
    except TypeError:
        # Compatibilidad con Python 3.
        s.send(bytes(chr(1), "utf-8"))

    # Cerrar conexión y archivo.
    
    f.close()
    print("El archivo ha sido enviado correctamente.")

  

if __name__ == "__main__":
    r=0
    s = socket()
    #s.connect(("0.0.0.0", 6030))
    s.connect(("192.168.137.132", 6030))

    while r<3:
        main(r,s)
        '''while True:
            respuesta=s.recv(4096)
            if respuesta == "exit":
                break'''
        r+=1
        time.sleep(1)
    s.close()

                
