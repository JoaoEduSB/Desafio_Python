# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de validação par ou ímpar#
#2) Escreva um programa que leia um número inteiro e informe se ele é positivo, negativo ou zero.

print("")

print("Vamos criar um programa que informa se o número é positivo, negativo ou zero")

numero = int(input("Digite o número: "))

print("")

if (numero == 0):
    print("O número", numero, "é zero.")

elif (numero > 0):
    print("O número", numero, "é negativo.")
    
else:
    print("O número", numero, "é positivo.")

print("")