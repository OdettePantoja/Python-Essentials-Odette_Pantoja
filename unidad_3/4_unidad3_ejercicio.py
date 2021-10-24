# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 17:02:19 2021

@author: Odette
"""

#EJERCICIO Escribir un código que permita 
#mostrar en pantalla lo que el usuario ingresa por 
#teclado. Cuando el usuario ingresa la palabra salir 
#(puede ser en mayúsculas o minúsculas) se debe terminar la ejecución.

usr=input("Ingrese una o más palabra: ")
while usr.lower()!="salir":
    usr=input("Ingrese una o más palabra: ")
print("Programa terminado")

    
##USO DEL BREAK
control=True
while True:
    usr_print=input("Ingrese una o más palabras: ")
    if usr_print.lower()=="salir":
        break
    print(usr_print)
print("Programa terminado")



              