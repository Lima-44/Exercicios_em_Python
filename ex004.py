n = input('Digite algo: ')
print('O tipo primitivo desse valor é:', type(n))
print('Tem espaço? ', n.isspace()) # Se tiver espaço é verdadeiro caso ao contrário é falso
print('É um número? ',n.isnumeric()) #Se for númerico é true se for letras e false
print('É alfabético? ', n.isalpha())
print('É alfanumérico?', n.isalnum())
print('Está em maiúscula? ', n.isupper())
print('Está em minúscula? ', n.islower())
print('Está capitalizada? ', n.istitle())