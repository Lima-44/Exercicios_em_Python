#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

n = int(input('Digite um valor: '))
suc = (n + 1)
ant = (n - 1)
#print('O sucessor é: {}'.format(suc))
#print('O antecessor é: {}'.format(ant))

#Esse acima está certo, mas farei de uma maneira diferente logo abaixo

print('Analisando o valor digitado: {}, o sue antecessor é: {} e o sucessor é: {}'.format(n, ant, suc)) 

#Usando apenas uma variável o programa ficaria assim:

# n = int(input('Digite um valor: '))
# print('Analisando o valor digitado: {}, o sue antecessor é: {} e o sucessor é: {}'.format(n, (n-1), (n+1)))