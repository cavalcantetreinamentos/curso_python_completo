# -*- coding: utf-8 -*-
"""Resolução Exercícios 5 e 6 referentes a aula07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-gZ6slYh_g6RRZNZzxckEU7w-OhfNucy

# 5 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
	
  >Celsius to Fahrenheit:   °F = °C × 1,8 + 32
  
  >Fahrenheit to Celsius:   °C = (°F − 32) / 1,8
"""

graus_C = float(input('Digite a temperatura (C): '))
graus_F = (graus_C * 1.8) + 32
print('A conversão de ' + str(graus_C) + " para fahrenheit é: " + str(graus_F))

"""# 6 - Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: 
>(72.7*altura)  58
"""

altura = float(input('Digite a sua altura: '))
peso_ideal = (72.7 * altura) - 58
print('O seu peso ideal é: ' + str(round(peso_ideal, 2)))