"""
# Questão 1 

lista_numeros = []
maior_numero = 0
posicao = 0

for i in range(9):
    numero = int(input("Digite numeros inteiros: "))
    lista_numeros.append(numero)

for x in lista_numeros:
    if x > maior_numero:
        maior_numero = x
        posicao = lista_numeros.index(x)

print(f"Maior número: {maior_numero} ")
print(f"Posição: {posicao}")

# Questão 2 

lista_numeros = []
lista_pares = []
lista_impares = []

for i in range(10):
    numeros = int(input("Digite números: "))
    lista_numeros.append(numeros)

for x in lista_numeros:
    if (x % 2 == 0):
        lista_pares.append(x)
    elif (x % 2 == 1):
        lista_impares.append(x)

print(f"Lista original:", *lista_numeros, "\n")
print(f"Lista de Pares:", *lista_pares, "\n")
print(f"Lista de Pares:", *lista_impares)

# Questão 3

notas = []
notas_acima_media = []
soma = 0 

for i in range(5):
    nota = float(input("Digite as notas dos alunos: "))
    notas.append(nota)

for x in notas:
    soma += x

media_turma = soma / len(notas)

for n in notas:
    if n > media_turma:
        notas_acima_media.append(n)

print("Notas acima da média: ", *notas_acima_media)

# Questão 4

lista_num = []
positivos = 0
negativos = 0
zeros = 0


for i in range(1, 11):
    numero = int(input("Digite os números: "))
    lista_num.append(numero)

for x in lista_num:
    if (x > 0): 
        positivos += 1
    elif (x < 0): 
        negativos += 1
    else:
        zeros += 1

print("Os números inseridos foram: ", *lista_num, ", Eles contém:")
print(f"Quantidade de positivos: {positivos}\n Quantidade de Negativos: {negativos}")
print(f"Quantidade de Zeros: {zeros}")

# Questão 5

lista_num1 = []
repetidos = False

for i in range(1, 9):
    num = int(input("Digite os números: "))
    lista_num1.append(num)

for x in lista_num1:
    if (lista_num1.count(x) > 1):
        repetidos = True

if repetidos == True:
    print("Existem números repetidos")
elif repetidos == False:
    print("Não existem números repetidos")

# Questão 6 

lista_num = []
mun_atsil = []

for i in range(1, 11):
    num = int(input("Digite um número: "))
    lista_num.append(i)

for x in range(len(lista_num) - 1, -1, -1): 
    mun_atsil.append(lista_num[x])

print("Lista original: ", *lista_num)
print("Lista invertida: ", *mun_atsil)

# Questão 7

lista_num = []
soma_pares = 0
soma_impares = 0

for i in range(1, 11):
    num = int(input("Digite os números: "))
    lista_num.append(num)

for x in lista_num:
    if (x % 2 == 0):
        soma_pares += x
    elif (x % 2 == 1):
        soma_impares += x

print(f"A Soma dos pares: {soma_pares}\nA Soma dos impares: {soma_impares}")

# Questão 8

lista_num = []

for i in range(1, 11):
    num = int(input("Digite os números: "))
    lista_num.append(num)

valor_busca = int(input("Digite o número para ser buscado: "))
aparacioes = lista_num.count(valor_busca)

print(f"O Número {valor_busca} apareceu {aparacioes} vezes.")

# Questão 9

lista_num = []
lista_maior_10 = []

for i in range(1, 11):
    num = int(input("Digite os números: "))
    lista_num.append(num)

for x in lista_num:
    if (x > 10):
        lista_maior_10.append(x)

print("Lista original: ",*lista_num,"\nLista maiores que 10: ",*lista_maior_10)

# Questão 10
"""

COSNT_media = 7.0
lista_nomes = []
lista_notas = []

for n in range(1, 6):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do Aluno: "))

    lista_nomes.append(nome)
    lista_notas.append(nota)

for i in range(len(lista_nomes)):
    nome = lista_nomes[i]
    nota = lista_notas[i]

    if nota >= COSNT_media:
        print(f"Aluno: {nome}\nNota: {nota}\nSituação: Aprovado")
    else:
        print(f"Aluno: {nome}\nNota: {nota}\nSituação: Reprovado")