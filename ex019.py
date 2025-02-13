# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random

#um = str(input('Digite o nome do 1º aluno: '))
#dois = str(input('Digite o nome do 2º aluno: '))
#tres = str(input('Digite o nome do 3º aluno: '))
#quat = str(input('Digite o nome do 4º aluno: '))

#lista = [um, dois, tres, quat]
#escolhido = random.choice(lista)
#print('O nome escolhido foi: {}'.format(escolhido))

#Aqui abaixo vou mostrar como criar uma lista de nomes e solicitar para sortear aleatoriamente dois nomes usando o K=2

nome = ['André', 'Luiz', 'Leandro', 'João', 'Renato', 'Barbosa']

sorteados = random.sample(nome, k=2)
print('Os nomes sorteados foram:\n {}'.format(sorteados)) # \n servve para pular linha o nome dos sorteados ficará logo abaixo