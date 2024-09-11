"""
Comparando Múltiplos Valores: Proponha que os alunos escrevam um programa que verifica se um número (por exemplo, 5) é menor que 10 e maior que 3, usando operadores relacionais combinados com operadores lógicos, e imprima o resultado.
"""

primeiro_numero = int(input("Digite um número: "));
segundo_numero = int(input("Digite um segundo número: "));
terceiro_numero = int(input("E por sim, digite um terceiro número: "))

if (primeiro_numero < segundo_numero < terceiro_numero):
    print(f"{primeiro_numero} é menor que {segundo_numero} que é menor que {terceiro_numero}.")

elif (primeiro_numero > segundo_numero > terceiro_numero):
    print(f"{primeiro_numero} é maior que {segundo_numero} que é maior que {terceiro_numero}.")