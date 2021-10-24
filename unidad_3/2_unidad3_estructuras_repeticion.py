# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 16:22:04 2021

@author: Odette
"""

#ESTRUCTURAS DE REPETICIÓN E ITERACIÓN

##LISTAS


lista= [1, 2.5, "Devcode", [5,6],4]

print(lista[0]) #1
print(lista[1]) #2.5
print(lista[2]) #Devcode
print(lista[3]) #[5,6]
print(lista[3][0]) #5
print(lista[3][1]) #6
print(lista[1:3]) #[2.5,Devcode]
print(lista[1:6]) #[2.5,Devcode,[5,6],4]
print(lista[1:6:2]) #[2.5,[5,6]]


##OPERADORES DE PERTENENCIA
a=[1,2,3,4,5]
print(3 in a) #TRUE
print(12 not in a) #TRUE
print(1 not in a) #FALSE

##OPERADORES DE IDENTIDAD IS/ IS NOT
a=3
b=3
c=4
print(a is b) #TRUE
print(a is not b) #FALSE
print(a is not c) #TRUE

x=1
y=x
z=y
print(z is 1) #TRUE
print(z is x) #true

#


