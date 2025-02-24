# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

dis = int(input('Qual é a distância da viagem em Km: '))
ate = dis <= 200 
aci = dis > 200
if dis <= 200:
    print('O preço da sua passagem ficará em R$ {}'.format((.50 / ate)* dis))
else:
    print('Para viagens acima de 200 km, neste caso o preço da passagem é de: R$ {} reais '.format((.45 / aci)* dis))

