# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de validação par ou ímpar#
#3) Escreva um programa que leia dois números inteiros e informe qual deles é o maior.

menorDeles = int(0)

print("")

print("Vamos criar um programa que lê 2 números e informa o maior")

valorA = int(input("Digite o primeiro número: "))
maiorDeles = valorA

valorB = int(input("Digite o segundo número: "))

print("")

if (valorB > maiorDeles):
    maiorDeles = valorB
    menorDeles = valorA
else:
    menorDeles = valorB

print("O maior dos valores é:", maiorDeles, "e o menor é:", menorDeles)

print("")