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

def main():
    s = socket()
    #s.connect(("0.0.0.0", 6030))
    s.connect(("192.168.137.132", 6030))
    
    
    while True:
        
        f = open("amor.jpeg", "rb")
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
    '''
    while True:
            respuesta=s.recv(4096)
            if respuesta == "exit":
                break'''
    s.close()
    
def main2():
    r = socket()
    #s.connect(("0.0.0.0", 6030))
    r.connect(("192.168.137.132", 6030))
    
    while True:
        f = open("nene.jpeg", "rb")
        content = f.read(1024)
        while content:
            # Enviar contenido.
            r.send(content)
            content = f.read(1024)
        break
    
    
    # Se utiliza el caracter de código 1 para indicar
    # al cliente que ya se ha enviado todo el contenido.
    try:
        r.send(chr(1))
    except TypeError:
        # Compatibilidad con Python 3.
        r.send(bytes(chr(1), "utf-8"))

    # Cerrar conexión y archivo.
    
    f.close()
    print("El archivo ha sido enviado correctamente.")
    r.close()

def main3():
    r = socket()
    #s.connect(("0.0.0.0", 6030))
    r.connect(("192.168.137.132", 6030))
    
    while True:
        f = open("gemidos.mp3", "r")
        content = f.read(1024)
        while content:
            # Enviar contenido.
            r.send(content)
            content = f.read(1024)
        break
    
    
    # Se utiliza el caracter de código 1 para indicar
    # al cliente que ya se ha enviado todo el contenido.
    try:
        r.send(chr(1))
    except TypeError:
        # Compatibilidad con Python 3.
        r.send(bytes(chr(1), "utf-8"))

    # Cerrar conexión y archivo.
    
    f.close()
    print("El archivo ha sido enviado correctamente.")
    r.close()

if __name__ == "__main__":
        main2()
        main()
        main3()
   

                

