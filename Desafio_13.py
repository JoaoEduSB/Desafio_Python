# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de validação par ou ímpar#
#13) Escreva um programa que leia o valor de uma compra e a categoria do cliente (1 para comum, 2 para associado e 3 para VIP). Aplique os seguintes descontos:

# Comum: Sem desconto

# Associado: 10% de desconto

# VIP: 20% de desconto

# Informe o valor final da compra.

print("")

print("")

print("Vamos validar a categoria do cliente e o valor de sua compra")

print("Categorias Disponíveis: \n" +
        "1 - Comum \n" +
        "2 - Associado \n" +
        "3 - VIP \n")

valor_compra = float(input("Digite o valor da sua compra: "))

print("")

categoria = int(input("Digite a sua categoria com um número inteiro: "))

while categoria not in [1, 2, 3]:
    categoria = int(input("Categoria inválida. Digite novamente: "))

if categoria == 2:
    valor_compra -= valor_compra * 0.1
    print(f"O valor da sua compra foi: R${valor_compra:.2f}")
    
elif categoria == 3:
    valor_compra -= valor_compra * 0.2
    print(f"O valor da sua compra foi: R${valor_compra:.2f}")
    
else:
    print(f"O valor da sua compra foi: R${valor_compra:.2f}")

print("")