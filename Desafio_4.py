# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de validação par ou ímpar#
#4) Escreva um programa que leia três lados de um triângulo e verifique se eles formam um triângulo válido. Para isso, a soma de dois lados deve ser sempre maior que o terceiro lado.


print("")

print("Vamos verificar se um triângulo é válido ou não")

print("")

lado_a = int(input("Digite o valor do lado esquerdo triângulo: "))
lado_b = int(input("Digite o valor do lado direito do triângulo: "))
lado_c = int(input("Digite o valor da base do triângulo: "))

print("")

if (lado_a + lado_b > lado_c) and (lado_b + lado_c > lado_a) and (lado_a + lado_c > lado_b):
    print("As medidas formam um triângulo.")
else:
    print("As medidas não formam um triângulo.")

print("")