# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de validação par ou ímpar#
#5) Escreva um programa que leia três notas de um aluno e calcule a média. Informe se o aluno está aprovado (média >= 7), em recuperação (5 <= média < 7) ou reprovado (média < 5).

print("")

print("Vamos calcular a nota média de um aluno, serão digitadas 3 notas.")

print("")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print("")

if media >= 7:
    print(f"O aluno está aprovado, com média: {media:.2f}")
    
elif media >= 5:
    print(f"O aluno está de recuperação, com média: {media:.2f}")
    
else:
    print(f"O aluno está reprovado, com média: {media:.2f}")
    
print("")