# Vou criar uma condição que quando digitado o meu nome 'Leandro', ele vai dizer que o meu nome é lindo, caso seja digitado qualquer outro nome diferente, apenas dará um bom dia.

# Estrutura condicionla simples
nome= str(input('Qual é o seu nome? '))
if nome == 'Leandro':
    print('Que nome lindo você tem!')
print('Bom dia, {}!'.format(nome))

# Estrutura condicional composta

nome= str(input('Qual é o seu nome? '))
if nome == 'Leandro':
    print('Que nome lindo você tem! ')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}'.format(nome))

# Estrutura condicional composta

tempo = int(input('Quantos anos tem o seu carro? '))
if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')
    print('Fim')

# Fazendo de uma forma mais enxuta
    
tempo = int(input('Quantos anos tem o seu carro? '))    
print('Carro novo' if tempo <=3 else'Carro velho')
print('-----FIM-----')


# Cálculo de média utilizando o método  condicional composta

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('Sua média foi: {:.1f} '.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS')
else:
    print('Sua média foi ruim! ESTUDE MAIS! ')

# Condição simplificada

n1 = float(input('Digit a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('PARABÉNS' if m >=6 else 'ESTUDE MAIS') 