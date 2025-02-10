#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

m = float(input('Digite um valor: '))
cen = m * 100
mil = m * 1000
print('O valor em centímetros é: {:.0f} cm'.format(cen))
print('O valor em milímetros é: {:.0f} mm'.format(mil))