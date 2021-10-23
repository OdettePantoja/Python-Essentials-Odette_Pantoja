# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 20:23:25 2021

@author: Odette
"""

#MÉTODO STRIP Elimina espacios 
var_prueba="     MENSAJE de TRABAJOS para Pruebas   "
print(var_prueba)

#lstrip elimina los espacios a la izq
print(var_prueba.lstrip())

#rstrip elimina los espacios a la derecha
print(var_prueba.rstrip())

#strip elimina espacios a la derecha y a la izq
print(var_prueba.strip())

#MÉTODO REPLACE
var_prueba="     MENSAJE de TRABAJOS para Pruebas   "
print(var_prueba)

print(var_prueba.replace("E","100"))

#MÉTODO SPLIT permite separar las palabras y 
#crea una lista

correo_prueba="odette@epn.edu"

print(correo_prueba)
print(correo_prueba.split("@"))

#si dentro del split no se coloca nada, 
#separa entonces las palabras por los espacios 
print("hola caracola buenos días".split())
