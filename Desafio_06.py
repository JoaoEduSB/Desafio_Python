# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de validação par ou ímpar#
#6) Escreva um programa que leia um ano e verifique se ele é bissexto. Um ano é bissexto se for divisível por 4, mas não por 100, exceto se for divisível por 400.

print("")

ano = int(input("Escreva o Ano: "))

if ano % 4 == 0:
    
    if ano % 100 != 0:
        print("O ano digitado é bissexto.")
        
    elif ano % 400 == 0:
        print("O ano digitado é bissexto.")
        
    else:
        print("O ano digitado não é bissexto.")
        
else:
    print("O ano digitado não é bissexto.")

print("")