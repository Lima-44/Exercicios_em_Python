# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

dis = float(input('Qual é a distância da viagem em Km: '))
ate = dis <= 200 
aci = dis > 200
if dis <= 200:
    print('O preço da sua passagem ficará em R$ {:.2f}'.format((.50 / ate)* dis))
else:
    print('Para viagens acima de 200 km, neste caso o preço da passagem é de: R$ {:.2f} reais '.format((.45 / aci)* dis))

#preco = dis * 0.50 if dis <= 200 else dis *0.45 -----> Este é o inline, um comando simplificado.