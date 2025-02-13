# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite o seu nome: ').strip().upper())
n_desejado = 'SILVA'
if n_desejado in nome:
    print(f"A palavra '{n_desejado.title().upper()}'foi encontrado no nome digitado!")
else:
    print(f"A palavra '{n_desejado.title().upper()}'não foi encontrado no nome digitado!")

# Na programação acima ele vai dizer se tem 'SILVA' no nome 
# OBS: O programa vai retirar os espaços, pouco importa se a pessoa escreva em maiúscula ou minúscula. Usando o strip() para retirar os espaços e o upper() passando toda a escrita para maiúscula
# Ex: 'João da Silva'  Resposta: A palavra 'SILVA' foi encontrado no nome digitado!
# Ex: 'João da Silva'  Resposta: A palavra 'SILVA' não foi encontrado no nome digitado!



# Neste caso abaixo o programa apenas vai dizer se é FALSE ou TRUE
# Ex: Seu nome tem Silva? Resposta: TRUE
# Ex: Seu nome tem Silva? Resposta: FALSE
# OBS: O programa vai retirar os espaços, pouco importa se a pessoa escreva em maiúscula ou minúscula. Usando o strip() para retirar os espaços e o upper() passando toda a escrita para maiúscula
nome = str(input('Digite o seu nome:')).strip().upper()
print('Seu nome tem Silva? {}'.format('SILVA' in nome))