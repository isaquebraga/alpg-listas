"""
 Faça um algoritmo que lê dois números, e verifica se o primeiro número é igual ao segundo número. Se forem iguais, escrever "Números iguais". Se não, escrever "Números diferentes".
 """

numeros = []

for i in range(2):
    numeros.append(int(input("Digite um número: ")))

if numeros[0] == numeros[1]:
    print("Números iguais.")

else:
    print("Números diferentes.")