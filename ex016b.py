# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira. Ex: Digite um número: 6.127 O número 6.127 tem a parte inteira 6.

import math
#Foi realizado de três maneiras, todas estão corretas

#num = float(input('Digite um número qualquer:'))
#num_inteiro = math.floor(num)
#print('O número digitado foi: {}, e a sua parte inteira é: {}'.format(num, num_inteiro))

#********************************************************************************************

#from math import trunc
#num = float(input('Digite um valor: '))
#print('O valor digitado foi {} e a porção inteira é {}'.format(num, trun(num)))


#********************************************************************************************

num = float(input('Digite um valor:'))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))
