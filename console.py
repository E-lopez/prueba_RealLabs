# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 11:46:01 2022

@author: aleja
"""
import sequences_calculator as calc

print("Ejercicio 1: secuencia de números convergente a 1. \n")

stop = ""
while not (stop):
    res = 0
    count = 0
    number = input("Ingrese un número entero positivo \n")

    res_count, res_seq = calc.sequence_to_one(int(number))

    print("El número de pasos fue de {}.".format(res_count))
    print("La secuencia resultante es: {}.".format(res_seq))

    stop = input("\nEscribe Stop para terminar \nEnter para ingresar otro número\n")

print("Ejercicio 2: secuencias máximas. \n")
calc.find_sequences(10000000)
