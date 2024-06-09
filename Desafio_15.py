# Curso Básico de Python
# Nome do desenvolvedor: João Eduardo Souza Barbosa
# Versão 1.0
# Exercício de lógica de programação 
# com a linguagem de programação Python
# Exercício de validação par ou ímpar#
#15) Escreva um programa que leia o peso e a altura de uma pessoa, calcule o IMC e informe a categoria:

# Abaixo do peso: IMC < 18.5
# Peso normal: 18.5 <= IMC < 24.9
# Sobrepeso: 25 <= IMC < 29.9
# Obesidade grau I: 30 <= IMC < 34.9
# Obesidade grau II: 35 <= IMC < 39.9
# Obesidade grau III: IMC >= 40

print("")

print("Vamos calcular o IMC de uma pessoa")

peso = float(input("Digite o seu peso (kg): "))

print("")

print("OBS: Cuidado ao digitar a altura e o peso, utilizar ponto para separar (ex.: 1.75) ")
altura = float(input("Digite a sua altura (m): "))

imc = peso / (altura * altura)

if imc < 18.5:
    print(f"Você está abaixo do peso\nO seu IMC é: {round(imc, 2)}")
    
elif 18.5 <= imc < 24.9:
    print(f"Você está com o peso ideal\nO seu IMC é: {round(imc, 2)}")
    
elif 25 <= imc < 29.9:
    print(f"Você está com sobrepeso\nO seu IMC é: {round(imc, 2)}")
    
elif 30 <= imc < 34.9:
    print(f"Você está com obesidade grau I\nO seu IMC é: {round(imc, 2)}")
    
elif 35 <= imc < 39.9:
    print(f"Você está com obesidade grau II\nO seu IMC é: {round(imc, 2)}")
    
else:
    print(f"Você está com obesidade grau III\nO seu IMC é: {round(imc, 2)}")

print("")
