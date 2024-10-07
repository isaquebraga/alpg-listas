"""
Faça um algoritmo que lê dois números, e verifica se o primeiro número é maior ou igual ao segundo número. Se for, escrever "O número {valor do número 1} é maior ou igual ao número {valor do número 2}". Se não, escrever "O número {valor do número 1} é menor ou igual ao número {valor do número 2}".
"""

numeros = []

for i in range(2):
    numeros.append(int(input("Digite um número: ")))

if numeros[0] >= numeros[1]:
    print(f"O número {numeros[0]} é maior ou igual ao número {numeros[1]}.")

else:
    print(f"O número {numeros[0]} é menor que o número {numeros[1]}.")