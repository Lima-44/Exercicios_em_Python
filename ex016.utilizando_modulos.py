# Importando módulos
#Se voçê quiser funções matemáticas terá de importar as funções usando o import

#Funções da matemáticas (math)

# ceil = faz o arredondamento de um número para cima
# floor = faz o arredondamento de um número para baixo
# trunc = trunca um número da vírgula pra frente
# pow = potência, que a função da potência
# sqrt = para calcular a raiz quadrada
# factorial = para cálculo fatorial

# Import math = Vai importar toda a biblioteca podende usar todas as funcionalidades da matemática

# Posso também importar somente a funcionalidade matemática que preciso = from math import sqrt
import math

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é ugual a {}'.format(num, raiz))

# Com esse comando abixo por exemplo eu consigo arredondar a raiz para cima
print('A raiz de {} é ugual a {}'.format(num, math.ceil(raiz)))

# Com esse comando abixo por exemplo eu consigo arredondar a raiz para baixo
print('A raiz de {} é igual a {}'.format(num, math.floor(raiz)))



