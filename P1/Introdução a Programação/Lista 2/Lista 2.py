"""
#Q1

idade = int(input("Digite sua idade: "))
idade_minima = 16

if idade < idade_minima:
    print("O Cidadão não pode votar")
else:
    print("O Cidadão pode votar")

#--------------------------------------------
#Q2

temperatura = float(input("Digite sua temperatura: "))

if temperatura < 30:
    print("A Temperatura esta Fria")
else:
    print("A Temperatura esta Quente")

#--------------------------------------------
#Q3
salario = float(input("Digite o salario: "))

if salario > 2000:
    print("Você recebe mais que 2000 Reais")
elif salario == 2000:
    print("Você recebe 2000 Reais")
else:
    print("Você recebe menos que 2000 Reais")

#--------------------------------------------
#Q4

numero = int(input("Digite um numero: "))

if numero % 2 == 0:
    print("O Numero é par")
else:
    print("O Numero é impar")

#--------------------------------------------
#Q5


aluno = input("Digite o aluno: ")
nota = float(input("Digite a primeira nota: "))

if nota >= 7:
    print(f"O Aluno {aluno} foi APROVADO")
else:
    print(f"O Aluno {aluno} foi REPROVADO")

#--------------------------------------------
#Q6

idade = int(input("Digite sua idade: "))

if idade > 18:
    print("Entrada no evento permitida")
else:
    print("Entrada no evento negada")

#--------------------------------------------
#Q7

numero = float(input("Digite um numero: "))

if numero > 10:
    print(f"O numero: {numero} é MAIOR que 10")
elif numero == 10:
    print(f"O numero: {numero} é IGUAL que 10")
else:
    print(f"O numero: {numero} é MENOR que 10")

#--------------------------------------------
#Q8

faltas = int(input("Digite a quantidade de faltas: "))
limite = 10

if faltas > limite:
    print("O Aluno esta acima do limite de faltas")
else:
    print("O Aluno esta dentro do limite de faltas")

#--------------------------------------------
#Q9

senha_usuario = input("Digite sua senha: ")
senha_correta = "python123"

if senha_usuario == senha_correta:
    print("Senha Correta")
else:
    print("Senha Incorreta")

#--------------------------------------------
#Q10
"""
num1 = float(input("Digite um numero: "))
num2 =float(input("Digite outro numero: "))

if num1 > num2:
    print(f"{num1} é MAIOR que {num2}")
elif num1 < num2:
    print(f"{num2} é MAIOR que {num1}")
else:
    print("os numeros sao IGUAIS")

