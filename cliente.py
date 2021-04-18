# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 21:37:18 2021

@author: sebas
"""
import socket
import random as rd
import time 
import numpy as np 
import matplotlib.pyplot as plt

idC= 0         
promedio = 0.1
solicitud = [0]         
acceso = 120

host = socket.gethostname()
port = 9999


while(acceso>0):
    
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    idC = rd.randint(0, 119)
    mensaje = idC.to_bytes(2, 'big')
    
    Espera = rd.expovariate(1.0/promedio)
    solicitud.append(Espera)
    acceso -= 1
    
    clientsocket.connect((host, port))
    
    clientsocket.send(mensaje)
    permiso = clientsocket.recv(1024)
    
    
    if (permiso == bytes(1)):
        print(str(idC) + ' USUARIO ACCEDIENDO')
        
    elif(permiso == bytes(0)):
        print(str(idC) + ' ACCESO AL USUARIO CANCELADO')
        
    else:
        print(str(idC) + ' EL CLIENTE ESTA SALIENDO...')
    time.sleep(Espera)
    
    
    
    clientsocket.close()



