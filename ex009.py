#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

tabuada = int(input('Digite a tabuada desejada: '))
aux = 0
print('-' *12)
print('tabuada de {}'.format(tabuada))
print('-' *12)
while(aux <= 10):
    print('{0} x {1} = {2}'.format(aux, tabuada, (aux * tabuada)))
    aux = aux + 1  
print('Decorou?')    
