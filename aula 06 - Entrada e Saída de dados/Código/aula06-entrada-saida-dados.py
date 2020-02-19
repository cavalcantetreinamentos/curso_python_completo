# Lendo dados e imprimindo na tela

input('Digite seu nome: ')

nome = input('Digite seu nome: ')

print("Seja bem vindo")
print("Seja bem vindo " + nome)

nome_pessoa = 'João'
idade = '2'
sexo = 'M'

print(nome_pessoa, sexo, idade)
print(nome_pessoa, sexo, idade, sep=':')
print(nome_pessoa, sexo, idade, sep=':', end='')
print('Só para testar se vai ter nova linha')

print('Nome: ' + nome_pessoa + 'Sexo: ' + sexo + 'Idade: ' + idade)