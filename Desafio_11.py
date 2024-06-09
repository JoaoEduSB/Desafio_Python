# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de validação par ou ímpar#
#11) Escreva um programa que leia um número e verifique se ele está no intervalo de 10 a 20 (inclusive).

print("")

print("Vamos validar se um número está entre 10 e 20")

print("")

numero = int(input("Digite um número: "))

if numero < 10 or numero > 20:
    print(f"O número {numero} não está entre 10 e 20")
    
else:
    print(f"O número {numero} está entre 10 e 20")

print("")