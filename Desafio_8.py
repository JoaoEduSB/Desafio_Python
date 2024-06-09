# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de validação par ou ímpar#
#8) Escreva um programa que leia a nota de um aluno e converta-a para conceito: A (nota >= 9), B (7 <= nota < 9), C (5 <= nota < 7), D (3 <= nota < 5) e F (nota < 3).

print("")

print("Vamos ler a nota de um aluno e converter para uma letra")

nota_aluno = float(input("Digite a nota do aluno: "))

print("")

while nota_aluno < 0 or nota_aluno > 10:
    print("A nota digitada é inválida. Digite novamente: ")
    nota_aluno = float(input())

if nota_aluno < 3:
    print(f"A nota do aluno é F ({nota_aluno}).")
    
elif 3 <= nota_aluno < 5:
    print(f"A nota do aluno é D ({nota_aluno}).")
    
elif 5 <= nota_aluno < 7:
    print(f"A nota do aluno é C ({nota_aluno}).")
    
elif 7 <= nota_aluno <= 9:
    print(f"A nota do aluno é B ({nota_aluno}).")
    
else:
    print(f"A nota do aluno é A ({nota_aluno}).")

print("")