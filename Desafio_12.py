# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de validação par ou ímpar#
#12) Escreva um programa que leia um número e verifique se ele é maior que 100. Se não for, informe o dobro desse número.

print("")

print("Vamos ler um número e validar se ele é maior que 100, caso não for, dobrar.")

numero = int(input("Digite um número: "))

print("")

if (numero < 100):
    print(f"Dobrando o número, temos: {numero * 2}")
    
elif (numero == 100):
    print(f"O número {numero} é igual a 100.")
    
else:
    print(f"O número {numero} é maior que 100.")

print("")