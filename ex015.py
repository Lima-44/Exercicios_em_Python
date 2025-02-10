#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 reais por dia e R$0,15 por Km rodado.
carro = int(input('Digite a quantidade de Km percorrido: '))
dias = int(input('Digite a quantidade de dias alugado: '))
preco = dias * 60
km = carro * 0.15
tt = km + preco
print('Você alugou o carro por {} dias com um valor de R$ {} reais, rodou {} Km, para cada Km rodado você paragará R$ 0,15 centavos, então o valor por Km percorrido é de R$ {} reais. O valor total a ser pago é de: R$ {} reais'.format(dias, preco, carro, km, tt ))