#Crie um algoritimo que leia o seu número e mostre o seu dobro, triplo e raiz quadrada

#n = int(input('Digite um valor: '))
#d = n * 2
#t = n * 3
#r = n ** (1/2)
#print('O dobro do valor digitado é: {}'.format(d))
#print('O triplo do valor digitado é: {}'.format(t))
#print('A raiz quadrada do valor digitado é: {:.2f}'.format(r))

#OBS: Eliminando variável você economiza memória ;)

#Eliminando variável conforme abaixo:

n = int(input('Digite um valor: '))
print('O valor digitado é: {}.\nO dobro é: {}.\nO triplo é: {}.\nA raiz quadrada é: {:.2f}'.format(n, (n*2), (n*3), (n**(1/2))))
