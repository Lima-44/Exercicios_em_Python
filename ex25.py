# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite o nome da cidade: ').strip().upper())
n_desejado = 'SILVA'
if n_desejado in nome:
    print(f"A palavra '{n_desejado.title().upper()}'foi encontrado no nome digitado!")
else:
    print(f"A palavra '{n_desejado.title().upper()}'não foi encontrado no nome digitado!")