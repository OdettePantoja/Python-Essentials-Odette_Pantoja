# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 17:50:59 2021

@author: Odette
"""

#EJERCICIOS ESTRUCTRAS

#Escribir un programa que pregunte al usuario 
#una frase y una letra, y muestre por pantalla 
#el número de veces que aparece la letra 
#en la frase.

frase=input("Digite una frase: ")
letra=input("Digite una letra: ")

cnt=0 #la variable cnt cuenta la cantidad de coincidencias
var=0 #la variable var es la variable de control

while var<len(frase):
    if frase[var]==letra:
        cnt+=1
    var+=1
print("La cantidad de veces que se repite la letra es", cnt)
