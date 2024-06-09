# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de validação par ou ímpar#
#9)Escreva um programa que leia o código de um produto e informe a sua categoria:

# 1 a 10: Alimento não-perecível

# 11 a 20: Alimento perecível

# 21 a 30: Vestuário

# 31 a 40: Eletrônicos

# Outros: Código inválido

print("")

print("Vamos verificar a categoria do produto de acordo com o seu código")

codigo = int(input("Digite um número de 1 a 40: "))

print("")

while ((codigo < 0) or (codigo > 40)):
    print("O produto procurado pelo código digitado não existe.")
    codigo = int(input("Digite novamente o código: "))

if ((codigo >= 1) & (codigo <= 10)):
    print("O Produto é um alimento não-perecível.")
    
elif ((codigo >= 11) & (codigo <= 20)):
    print("O Produto é um alimento perecível.")
    
elif ((codigo >= 21) & (codigo <= 30)):
    print("O Produto é um vestuário.")
    
elif ((codigo >= 31) & (codigo <= 40)):
    print("O Produto é um eletrônico.")

print("")