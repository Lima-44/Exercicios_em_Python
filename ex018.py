# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ãngulo.
import math


ang = float(input('Digite o ângulo: '))
angradius = math.radians(ang)
sen = math.sin(angradius)
cos = math.cos(angradius)
tan = math.tan(angradius)
print('O âgulo digitado foi: {:.2f}, o seu seno é: {:.2f}, o cosseno é: {:.2f}, e a tangente é: {:.2f}'.format(ang, sen, cos, tan))


#Posso também importar somente a regra da matemática que usarei, neste caso ficaria assim:

from math import radians, sin, cos, tan

ang = float(input('Digite o ângulo: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('O ângulo digitado foi: {:.2f}, o seu seno é: {:.2f}, o cosseno é: {:.2f}, e a tangente é: {:.2f}'.format(ang, sen, cos, tan))