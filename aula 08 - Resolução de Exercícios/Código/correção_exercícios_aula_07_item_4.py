# -*- coding: utf-8 -*-

# 4) Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math
raio = float(input('Digite o raio do círculo(cm): '))
area_circulo = math.pi * (raio ** 2)
print('A área do círculo é (cm): ' + str(round(area_circulo, 2)))

