# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para  o usuário tentar descobrir qual foi o número ecolhido pel computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
from time import sleep # Faz o PC processar, é uma função que você escolhe o tempo de processamento


escolhido = random.randint(0,5) # Faz o computador pensar
n = int(input('Digite um número e tente acertar o número que será escolhido pelo PC: '))
print('Número escolhido pelo computador foi: {}'.format(escolhido))
print('Processando...')
sleep(3)
if  escolhido == n:
    print('Parabéns! Você acertou:')            
else:
    print('Você perdeu! Tente de novo!')
      
       
