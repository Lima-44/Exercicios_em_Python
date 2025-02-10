#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))
h = (l * a)
t = h / 2
print('Sua parede tem: {} metros'.format(h))
print('Você precisará de: {:.1f} litros de tinta'.format(t))