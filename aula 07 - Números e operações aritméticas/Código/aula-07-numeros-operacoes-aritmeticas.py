# Tipo de dado Inteiro

idade1 = 20
idade2 = int(20)
print(type(idade1))
print(type(idade2))
print(idade1, idade2)

idade3 = input('Digite a sua idade: ')
print(type(idade3))

#soma = idade3 + 10 

idade4 = (int(input('Digite a sua idade novamente: ')))
print(type(idade4))

soma1 = idade4 + 10
print('Somando idade: ' + str(soma1))

# Tipo de dado Float
altura1 = 1.75 # Perceber que se usa ponto no lugar da vírgula
altura2 = float(1.75) # Perceber que se usa ponto no lugar da vírgula
print(type(altura1))
print(type(altura2))
print(altura1, altura2)

altura3 = input('Digite sua altura: ')
print(type(altura3))

soma2 = float(altura3) + 0.25
print('Somando altura: ' + str(soma2))

# Problema da precisão do tipo de dado Float

teste = 4.35 * 100 # Operações aritméticas entre float e int retornam float
print('Problema da Precisão de números ponto flutuante: ' + str(teste))

# Inteiros e Floats são imutáveis

a = 1
print('Endereço de memória: ' + str(id(a)))

a = 2
print('Endereço de memória: ' + str(id(a)))

# Operações Aritméticas

x = 30
y = 20
soma = x + y
subtracao = x - y 
multiplicacao = x * y
divisao_exata = x // y
divisao = x / y
modulo = x % y
negacao = -x
potencia = x ** y
raiz_quadrada = x ** (1/2)
print('Soma: ' + (str(soma)))
print('Subtração: ' + (str(subtracao)))
print('multiplicação: ' + (str(multiplicacao)))
print('Divisão exata: ' + (str(divisao_exata)))
print('Divisão: ' + (str(divisao)))
print('Módulo: ' + (str(modulo)))
print('Negação: ' + (str(negacao)))
print('Potência: ' + (str(potencia)))
print('Raiz quadrada: ' + (str(raiz_quadrada)))

# Operações compostas f(x) = 5x + 30 onde x = 10
f = (5 * 10) + 30
print('Resultado equação: ' + str(f))


# Funções úteis
# Potência
print('Potência: ' + str(pow(x, y)))

# Valor absoluto
print('Valor absoluto: ' + str(abs(-100)))

# Arrendodar um número decimal 
print('Arredondando:  ' + str(round(320.5678, 2)))

# Obter quociente e resto
print('Quociente e resto são: ' + str(divmod(x, y)))

# Converter inteiro para binário
print('255 em binário é: ' + str(bin(255)))

# Converter inteiro para Octal
print('255 em octal é: ' + str(oct(255)))

# Converter inteiro para Hexadecimal
print('255 em hexadecimal é: ' + str(hex(255)))

# Exercícios
# 1) Faça um programa que converta metros para centímetros. Peça o usuário para digitar o comprimento em metros.

metro = float(input('Digite o valor em metro para ser convertido: '))
metro_para_centimetro = metro * 100
print('A conversão do valor ' + str(metro) + 'm para centimetro é ' + str(metro_para_centimetro) + 'cm')

# 2) Peça usuário para digitar 4 notas e retorne a média aritmética deles.
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

total_avaliacoes = 4

soma_notas = nota1 + nota2 + nota3 + nota4
media_aritmetica = soma_notas / total_avaliacoes
print('A sua média foi de: ' + str(media_aritmetica))

