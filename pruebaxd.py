import time
from socket import socket

def main(s):
    
    
    
    while True:
       msg=raw_input("> ")
       s.send(msg)
       respuesta=s.recv(4096)
       print(respuesta)
       if respuesta == "exit":
           break
 

    

if __name__ == "__main__":
    
    s = socket()
    s.connect(("192.168.137.132", 6030))

    main(s)
        
    s.close()

                
