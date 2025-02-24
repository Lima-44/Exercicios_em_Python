# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrupassar 80Km/h, mostre uma mensagem dizendo que ele foi multado
# A multa vai custar R$7,00 reais por cada Km acima do limite. 

vel = int(input('Digite a velocidade do carro: '))
m = vel - 80
if vel > 80:
    print('Você foi multado')  
    print('A multa vai custar R$ 7,00 reais por cada Km acima do limite.') 
    print('Valor total por km/h ultrapassado R$ {} reais'.format(m * 7)) 
else:    
    print('Você não foi multado')
    
    
    
    
    
    #print('Você foi multado a {} km/h  e mais R$ {} reais por km/h acima do limite: '.format(m,7)) 
    #print(' Valor total da multa R$ {} reais'.format(vel - 80)*(7))