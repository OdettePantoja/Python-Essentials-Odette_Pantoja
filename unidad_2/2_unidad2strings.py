# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 17:53:53 2021

@author: Odette
"""

#STRINGS

#RESALTAR PALABRAS CON COMILLAS DENTRO DE STRINGS
cadena_1="Palabra a resaltar: 'PRUEBA'"
print(cadena_1)


#SECUENCIAS DE ESCAPE
cadena_2="Palabra a resaltar: \"PRUEBA\""
print(cadena_2)

##SALTOS DE LÍNEA
print("Mensaje de prueba uno\nSegunda línea del mensaje")

##SANGRÍA PARA LA SEGUNDA FRASE
print("Mensaje de pruebauno\tSegunda línea del mensaje")

print("Mensaje de pruebauno\tSegunda línea del mensaje")

print("Mensaje \nde prueba uno \nSegunda línea \ndel mensaje")

print("Mensaje \t\t de prueba uno \nSegunda línea \ndel mensaje")

##UNIR VARIOS STRINGS
print("El siguiente es un número entero: ",50)

print("El siguiente es un número entero: ",50, "Número decimal: ",78.92)

print("El siguiente es un número entero: ",50, "\nNúmero decimal: ",78.92)

##ROMPER LÍNEAS DE CÓDIGO
print("El siguiente es un número entero: ",
      50,
      "\nNúmero decimal: ",
      78.92)

#PRUEBAS CON STRINGS
var1="Texto1"
var2=643
var3=4.67
var4="Texto2"

print(var1,var2,var3,var4)

##DECLARACIONES de concatenación con funciones constructoras
print(var1+str(var2)+str(var3)+var4)

print("texto prueba"+str(var2)+str(var3)+"89")

##STRING CON FUNCIÓN F
print(f"Variable1: {var1}\nVariable2: {var2}\nVariable3: {var3}\nVariable 4: {var4}")

print(f"Variable1: {var1*2}\nVariable2: {var2/2}\nVariable3: {var3}\nVariable4: {var4}")

#NÚMEROS EN FORMA DE TEXTO
print("89+var2-var3")

#Método FORMAT, 
#permite utilizar los valores de posición

print("Mi nombre es: {},mi apellido es {}, mi edad es: {}".format("Odette", "Pantoja",33))

var5="Mi nombre es: {},mi apellido es {}, mi edad es: {}".format("Odette", "Pantoja",33)
print(var5)

print("Mi nombre es: {1},mi apellido es {1}, mi edad es: {1}".format("Odette", "Pantoja",33))

print("Mi nombre es: {1},mi apellido es {2}, mi edad es: {0}".format("Odette", "Pantoja",33))

print("Mi nombre es: {nombre},mi apellido es {apellido}, mi edad es: {edad}".format(nombre="Odette", apellido="Pantoja",edad=33))

