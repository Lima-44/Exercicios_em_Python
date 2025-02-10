#############      FATIAMENTO       ############

# frase[9] = Ele vai identificar dentro da cadeia de caracter somente a letra 9
# Ex: C u r s o   e m   V  í  d  e o      P  y t  h  o  n
#     0-1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-16-17-18-19-20 
#OBS: O Python diferencia maisúscula de minúscula

# frase [9:13] = Ele vai identificar do 'V' até o 'e'.' É sempre um a menso no final,então neste caso ele não vai identificar o 13, a frase ficaria 'Víde'.

# frase [9:21] = Ele vai identificar do até o 20 9'V' até o 'n', então, seria a frase 'Vídeo Python'

# frase [9:21:2] = Faz a contagem pulando de dois em dois.Vai do número 9 até o 21 sempre pulando duas casas. Olhando a frase de exemplo lá em cima,ficaria assim ' Vdo Pto'.

# frase [:5] = Quando eu não coloco o início de onde ele vai começar, ele começa do caracter 0.
# Então a frase ficaria assim: 'Curso' - Lembrando sempre que última casa não conta, indo até a 4.

# frase [15:] = Neste caso está indicando o início mas não indica o final, então vai até o final da string. A frase ficaria assim: 'Python'

# frase [9::3] = Faz a contagem pulando de três em três.Vai do número 9 até o fim, pulando três casas
# então neste exemplo a frase ficaria 'VePhn'


#############      ANÁLISE       ############


# len(frase) = Significa o comprimento da frase, que no caso seria 21 , sendo do 0 ao 20.
# Ex: C u r s o   e m   V  í  d  e o      P  y t  h  o  n
#     0-1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-16-17-18-19-20 

# frase.count('o') = Estou pedindo para o programa contar quantas vezes tem a letra 'o' na frase.

# frase.count('o', 0, 13) = Faz uma contagem já com fatiamento. Vai contar do '0' até o '13', lembrando que o programa não faz a contagem do último número, então irá até o '12' contando a quantidade da letra 'o' na frase.

# frase.find('deo') = Quantas vezes ele encontrou a palavra 'deo'
# neste caso ele vai indicar que o 'deo' começou no número 11.

# frase. find('Android') = Dentro do exemplo acima não tem a string Android. Então como não existe ele vai retornar o -1, que significa que a palavra Android não existe.

# 'Curso' in frase = Dentro da frase existe a palavra 'Curso'? Ele vai retornar dizendo 'True'. Isso não é uma funcionalidade é um operador.


#############      TRANSFORMAÇÃO       ############

# frase.replace('Python', 'Android') = Neste caso o programa vai procurar pela palavra 'Paython' e substituir pela palavra 'Android'.

# frase.upper() = (Upper é um método) Todas as letras que estão em minúsculas ele joga para maiúsculas.

# frase.lower() = Todas as letras que estão em maiúsculas ele joga para minúsculas.

# frase.capitalize() = Coloca todos os caracteres para minúsculas e só primeiro caracter ele coloca em maiúsculo. Ex: 'Curso em vídeo python' somente o C fica maiúsculo.

# frase.title() = Ele faz uma analise mais profunda  da frase na string e faz um 'capitalize' em todas as palavras. Ex: 'Curso Em Vídeo Python' ou seja, todo o início de palavra começará com maiúscula.

# Vejamos agora a palavra         A p r e n d a     P y  t  h  o  n
########################    0-1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-16-17-18

# frase.strip() = Remove espaços no começo e no final de frase. No exemplo acima removeria os números de 0 a 2 e 17 a 18

# frase.rstrip() = Remove somente os últimos espaços. Neste exemplo removeria o 17 e 18.

# frase.lstrip() = Remove somente os começo da frase. Neste caso removeria o 0, 1, e 2.


#############      DIVISÃO          #############

#     C u r s o   e m   V í d e o   P y t h o n
#     0-1-2-3-4   0-1   0-1-2-3-4   0-1-2-3-4-5

# frase.split() = Ocorre um divisão nos espaços vazios criando blocos com númeração 
# Ex:  Curso em Vídeo Python = Então 'Curso' seria o bloco 1 de 0 a 4, 'em' seria o bloco 2 de 0 a 1, 'Vídeo' o bloco 3 de 0 a 4, 'Python o bloco 5 de 0 a 5



#############      JUNÇÃO          #############

# '-'.join(frase) = Comando para fazer a junção utilizando hífen
# Ex: Curso-em-Vídeo-Python

frase = 'Curso em Vídeo Python'
print(frase.lower().find('vídeo')) #Aqui ele joga a letra 'V' maiúscula para  'v' minúscula e procura onde ela começa. E o resultado é 9.
print(frase.replace('Python', 'Android'))#Nesta situação o programa troca a palavra 'Python' pela palavra 'Android'.
print(frase.split)#Aqui ele cria uma lista em colchetes separados por vírgula ['Curso', 'em', 'Vídeo', 'Python']
dividido = frase.split()
print(dividido[0])#Neste caso vai imprimir a palavra 'Curso'.
dividido = frase.split()
print(dividido[2][3])#Pegue o divido dois = Que neste caso é a palvra 'Vídeo' e mostre o caracter 3,que é a letra 'e'   