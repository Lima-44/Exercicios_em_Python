#Ordem de precedência na matemática em PYTHON:
# 1) ()             PARÊNTESES
# 2) **             POTÊNCIA
# 3)  *, /, //, %   MULTIPLICAÇÃO, DIVISÃO, DIVISÃO INTEIRA E RESTO DA DIVISÃO
# 4) +, -           MAIS E MENOS
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {}'.format(s, m, d)) 
#Neste caso o resultado da divisão foi 1.3333333333, se eu quiser o ponto com três casas depois e ou flutuantes, terei que usar na linha de comando 13 a seguinte programação ( e a divisão é {:.3f}) o resultado seria = 1.333
print('Divisão inteira {} e potência {}'.format(di, e))
#Para que os dois prints saiam na mesma linha no final é só usar= , end=' ')
#Exemplo: print('A soma é {}, o produto é {} e a divisão é {}'.format(s, m, d), end=' ') 
#Para quebrar a linha dentro do print= \n
#Exemplo: print('A soma é {}, \n o produto é {} e a \n divisão é {}'.format(s, m, d)) 