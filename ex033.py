# Faça um programa que leia três números e mostre quel é o MAIOR e qual é o MENOR.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
maior = (n1,n2,n3)
menor = (n1,n2,n3)

print('O maior número digitado foi: {}'.format(max(maior)))

print('O menor número digitado foi: {}'.format(min(menor)))