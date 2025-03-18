# Escreva um programa que pergunte o salário de um fincionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00 calcule um aumento de 10%.
# Para salários inferiores ou iguais, o aumento é de 15%.  

sal = float(input('Digite o seu salário: '))
if sal > 1250:
    print('O seu novo salário com o aumento de dez porcento R$ {:.2f} reais'.format(sal * .10 + sal))
else:
    print('O seu novo salário com o aumento de quinze porcento R$ {:.2f} reais'.format(sal * .15 + sal))

    # Fazendo o código de uma outra maneira

salario = float(input('Qual é o salário do funcionário? R$: '))
if salario <= 1250:
    novo = salario + (salario * 15 /100)
else: 
    novo = salario + (salario * 10 /100)
    print('Quem ganhava R$ {:.2F} passa a ganhar R$ {:.2f} agora.'.format(salario, novo))