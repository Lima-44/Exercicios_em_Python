#Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

temp = float(input('Informe a temperatura em celsius: '))
conver = (temp * 1.8) + 32
print('A temperatura em celsius informada é de {} °C e {} °F para fahrenheit'.format(temp, conver))