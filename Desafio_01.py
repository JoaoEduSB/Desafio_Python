# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de validação par ou ímpar#
#1) Escreva um programa que leia um número inteiro e informe se ele é par ou ímpar.

print("")

print("Vamos criar um programa que informa se o número é ímpar ou par")

numero = int(input("Digite o número: "))

print("")

if (numero % 2 == 0):
    print("O número", numero, "é par.")

else:
    print("O número", numero, "é ímpar.")
    
print("")