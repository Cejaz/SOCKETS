# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 16:38:05 2021

@author: sebas
"""
import socket
import numpy as np
import matplotlib.pyplot as plt

usuarios = []         
Acceso = 0              
aforo = 20                     
personasingresadas = []                    
cantidadUsuarios = []           

while(len(usuarios)<aforo):
    Aleatorio = np.random.randint(0, 119)
    if(not(Aleatorio in usuarios)):
        usuarios.append(Aleatorio)
    
print(usuarios)
    
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999
serversocket.bind((host, port))
serversocket.listen(5)


for k in range(120):
    
    clientsocket,addr = serversocket.accept()
    
    
    idC = clientsocket.recv(1024)
    mensaje = int.from_bytes(idC, 'big')
    
   
    if(mensaje in usuarios):   
        if (not(mensaje in personasingresadas)):
            Acceso = bytes(1)
            if(len(personasingresadas)<=aforo):
                Acceso = bytes(1)
                personasingresadas.append(mensaje)
                cantidadUsuarios.append(len(personasingresadas))
            else:
                Acceso = bytes(0)
        else: 
            Acceso = bytes(2)
            personasingresadas.remove(mensaje)
            cantidadUsuarios.append(cantidadUsuarios[-1]-1)   
    else: 
        Acceso = bytes(0)
        
    
    clientsocket.send(Acceso)
    clientsocket.close()


plt.grid(True)
plt.plot(cantidadUsuarios)
plt.show()
