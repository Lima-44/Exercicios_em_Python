# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
# Ex: Ana Maria de Souza
# primerio= Ana
# último= Souza

nome = str(input('Digite o seu nome completo: '))
print(nome.title())
separa = nome.split()
print('O seu primeiro nome é: {}'.format(separa[0]))
print('O seu último nome é: {}'.format(separa[-1].capitalize()))
  
