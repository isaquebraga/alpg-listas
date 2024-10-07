"""
Faça um algoritmo que lê dois números, e verifica se os dois números são iguais. Se forem iguais, escrever "São iguais", se não, escrever "Não são iguais".
"""

numeros = []

for i in range(2):
    numeros.append(int(input("Digite um número: ")))

if numeros[0] == numeros[1]:
    print("São iguais.")

else:
    print("Não são iguais.")