# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 16:05:28 2021

@author: Odette
"""

#ESTRUCTURAS DE CONTROL DE FLUJO

edad=int(input("Ingrse su edad como número: "))

#if edad>=18:
#   print("Usted es mayor de edad")
#else:
#    print("Usted es menor de edad")



if edad<18:
    print("Usted es menor de edad")
elif edad<45:  
    print("Usted es un adulto joven")
elif edad<60:  
    print("Usted es un adulto")

else:
    print("Usted es un adulto mayor")

