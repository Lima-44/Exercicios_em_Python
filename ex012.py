#Faça um algoritimo que leia o preço do produto e mostre seu novo preço com 5% de desconto.

pp = float(input('Digite o preço do produto: R$'))
np = (pp * 0.05)
print('O desconto é de 5%: R$ {} reais'.format(np))
tp = pp - np
print('Total com desconto é: R$ {:.2f} reais'.format(tp))