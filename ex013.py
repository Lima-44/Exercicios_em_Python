#Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

s= float(input('Digite o salário do funcionário: R$ '))
aumento = (s * 0.15) + s
print('Um funcionário que ganhava R$ {:.2f} rais, com 15% de aumento passará a receber R$ {:.2f} reais'.format(s, aumento))