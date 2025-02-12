# Crie um programa que leia o nome completo de uma pessoa e mostre:

# 1- O nome com todas as letras maiúsculas
# 2- O nome com todas as minúsculas
# 3- Quantas letras ao todo sem considerar espaços
# 4- Quantas letras tem o primeiro nome

nome = str(input('Digite o seu nome: ')).strip()
print('Analisando o seu nome...')
print('Seu nome em maiúsculo: {}'.format(nome.upper()))
print('Seu nome em minúsculo: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
# Abaixo estou dando um outro exemplo de como pode ser feito
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa [0], len(separa[0])))
