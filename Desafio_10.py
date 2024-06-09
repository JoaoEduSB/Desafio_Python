# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de validação par ou ímpar#
#10) Escreva um programa que leia dois números e uma operação (adição, subtração, multiplicação ou divisão) e realize a operação correspondente.

print("")

print("Vamos fazer uma operação matemática, basta digitar o primeiro número, \n" + 
        "selecionar o operador e digitar o segundo número, então terá o resultado.")

print("")

print("Os operadores são: \n" +
        "+ (soma) \n" +
        "- (subtração) \n" +
        "/ (divisão) \n" +
        "x (multiplicação)")

print("")

valor1 = int(input("Digite o primeiro valor: "))

operador = input("Digite o operador matemático: ")

while ((operador != "+") & (operador != "-") & (operador != "x") & (operador != "/")):
    operador = input("Operador inválido, digite novamente: ")

valor2 = int(input("Digite o segundo valor: "))

if operador == "+":
    print(f"{valor1} + {valor2} = {valor1 + valor2}")
    
elif operador == "-":
    print(f"{valor1} - {valor2} = {valor1 - valor2}")
    
elif operador == "x":
    print(f"{valor1} x {valor2} = {valor1 * valor2}")
    
elif operador == "/":
    print(f"{valor1} / {valor2} = {valor1 / valor2}")
    
print("")