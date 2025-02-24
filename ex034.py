# Escreva um programa que pergunte o salário de um fincionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00 calcule um aumento de 10%.
# Para salários inferiores ou iguais, o aumento é de 15%.  

sal = int(input('Digite o seu salário: '))
if sal > 1250:
    print('O seu novo salário com o aumento de dez porcento R$ {} reais'.format(sal * .10 + sal))
else:
    print('O seu novo salário com o aumento de quinze porcento R$ {} reais'.format(sal * .15 + sal))