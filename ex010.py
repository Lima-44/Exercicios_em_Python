#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

din = float(input('Digite um valor: R$ '))
us = din / 6.18
print('Você pode comprar: {:.2f} doláres'.format(us))