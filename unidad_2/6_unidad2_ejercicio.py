# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 20:39:34 2021

@author: Odette
"""

#EJERCICIO: Escribir un programa que pregunte al 
#usuario los 4 productos de un carrito de compras, 
#separados por comas, 
#y muestre por pantalla cada uno 
#de los productos en una línea distinta.

compras=input("Diga los 4 productos de compra separados por comas: ")
#z=compras.split(",")
#print(z)
#print("\nArticulo 1: {}\nArticulo 2: {}\nArticulo 3: {}\nArticulo 4: {}".format(z[0],z[1],z[2],z[3]))

#compras_p=compras.replace(",","\n")
print(compras.replace(",","\n"))