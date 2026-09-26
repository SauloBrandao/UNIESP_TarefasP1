"""
#Q1


nome = input('Digite seu nome: ')
curso = input('Digite seu curso: ')
periodo = input('Digite seu periodo: ')

print(f"Aluno: {nome}, Curso: {curso}, Periodo: {periodo}")

#-------------------------------------------

#Q2

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
num3 = int(input("Digite outro numero: "))

soma = num1 + num2 + num3

print(soma)

#-------------------------------------------

#Q3

num = float(input("Digite um numero: "))

divisao = num / 3

print(f"A Terça parte de: {num} é:{divisao}")

#-------------------------------------------

#Q4

quilometros_percorridos = float(input("Digite a distancia percorrida (KM): "))
combustivel_consumido = float(input("Digite a quantidade de combustivel consumida: "))

consumo_medio = quilometros_percorridos / combustivel_consumido

print(f"O Consumo medio é: {consumo_medio}")

#-------------------------------------------

#Q5

salario = float(input("Digite o Salario do funcionario: "))

aumento = (salario * 0.15) + salario

print(f"O Salario de: {salario} / com aumento de 15%: {aumento}")

#-------------------------------------------

#Q6

idade = int(input("Digite sua idade: "))

calculo_meses = idade * 12

print(f"você tem aproximadamente: {calculo_meses} meses de vida")

#-------------------------------------------

#Q7

altura = float(input("Digite a altura: "))
base = float(input("Digite a base: "))

resultado = (base * altura) / 2

print(f"A área do triangulo: {resultado}")

#-------------------------------------------

#Q8

valor = float(input("Digite um valor: "))
percentual_desconto = float(input("Digite o percentual de desconto: "))

desconto = (valor * percentual_desconto) / 100
desconto_aplicado = valor - desconto

if percentual_desconto <= 0:
    print("Esse desconto não será possível")
elif percentual_desconto < 100:
    print(f"Com o desconto de: {percentual_desconto}% o valor do produto fica: {desconto_aplicado}")
elif percentual_desconto == 100:
    print(f"Com o desconto de: {percentual_desconto}% o valor do produto fica: 0")
else:
    print("Esse desconto não será possível")

#-------------------------------------------

#Q9

temp = float(input("Digite um temperatura em Celsius: "))
transformacao_F = (temp * 1.8) + 32

print(f"A Temperatura: {temp} Celsius em Fahrenheit: {transformacao_F} Fahrenheit")

#-------------------------------------------

#Q10

nome = input("Digite seu nome: ")
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"O Aluno: {nome} tem a média {media}")
"""
