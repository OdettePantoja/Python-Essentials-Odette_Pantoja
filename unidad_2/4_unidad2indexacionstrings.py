# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 20:05:58 2021

@author: Odette
"""

#INDEXACIÓN DE STRINGS

#LONGITUS DEL TEXTO
var_prueba="MENSAJE DE TRABAJOS PARA PRUEBAS"
print(len(var_prueba))

#PARA QUE MUESTRE LA LETRA DE LA POSICIÓN [0]
var_prueba="MENSAJE DE TRABAJOS PARA PRUEBAS"
print(var_prueba[0])

#CAMBIANDO ASIGNACIÓN DE LA VARIABLE
var1=90
print(var1)
var1=var1+89
print(var1)

#ACTUALIZANDO EL VALOR DE LAS VARIABLES
var_prueba="MENSAJE DE TRABAJOS PARA PRUEBAS"
print(var_prueba)

#var_prueba=var_prueba+"TEXTO ADICIONAL"
print(var_prueba+" TEXTO ADICIONAL")

#CORTAR MENSAJES
var_prueba="MENSAJE DE TRABAJOS PARA PRUEBAS"
print(var_prueba[0:7])    
#LO CPORTA DESDE LA POSICIÓN 0 hasta la 7

var_prueba="MENSAJE DE TRABAJOS PARA PRUEBAS"
print(var_prueba[7:])

print(var_prueba[-8:-1])

#CONVERTRIR EN MAYÚSCULAS. MÉTODO UPPER (LAS PONE TODAS EN MAYÚSCULAS)
var_prueba="     MENSAJE de TRABAJOS para Pruebas   "
print(var_prueba)

var_2=var_prueba.upper()
print(var_2)

#MÉTODO Mínusculas
var_2=var_prueba.lower()
print(var_2)

#MÉTODO TITLE
print(var_2.title())

#MÉTODO STRIP Elimina espacios 
var_prueba="     MENSAJE de TRABAJOS para Pruebas   "
print(var_prueba)
print(var_prueba.rstrip())


