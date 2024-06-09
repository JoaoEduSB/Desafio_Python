# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de validação par ou ímpar#
#7) Escreva um programa que leia a idade de uma pessoa e informe se ela é uma criança (0-12 anos), adolescente (13-17 anos), adulto (18-59 anos) ou idoso (60 anos ou mais).

print("")

print("Vamos verificar se a pessoa é uma criança, adolescente, adulto ou idoso")

idade = int(input("Digite a idade da pessoa: "))

print("")

while idade < 0:
    idade = int(input("A idade digitada não é valida, digite novamente: "))

if (idade == 0) or (idade < 13):
    print("A pessoa é uma criança.")
    
elif (idade == 13) or (idade < 18):
    print("A pessoa é adolescente.")
    
elif (idade == 18) or (idade < 60):
    print("A pessoa é adulta.")
    
else:
    print("A pessoa é idosa.")

print("")