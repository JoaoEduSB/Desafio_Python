# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de validação par ou ímpar#
#14) Escreva um programa que leia um número e informe se ele é positivo ou negativo. Se for positivo, calcule a raiz quadrada; se for negativo, informe o número ao quadrado.

import math

print("")

print("Vamos ler um número, informar se ele é positivo ou negativo e tratar a sua condição")
print("Caso o número seja negativo, vamos calcular o quadrado do número, \n" + 
        "caso seja positivo, a raiz quadrada.")

print("")

numero = float(input("Digite um número: "))

if numero == 0:
    print(f"O número {numero} é positivo")
    
elif numero < 0:
    potencia = math.pow(numero, 2)
    print(f"O número {numero} é negativo.")
    print(f"O quadrado do {numero} é: {potencia}")
    
else:
    raiz_quadrada = math.sqrt(numero)
    print(f"O número {numero} é positivo.")
    print(f"A raiz quadrada de {numero} é: {round(raiz_quadrada, 2)}")

print("")