"""
    Verificação Básica de Igualdade: Peça ao estudante para escrever um programa que compara dois números (por exemplo, 10 e 20) usando o operador == e imprime o resultado.
"""

primeiro_numero = int(input("Digite um número: "));
segundo_numero = int(input("Digite um segundo número para que eu possa os comparar: "));

if (primeiro_numero == segundo_numero):
    print(f"O números digitados ({primeiro_numero} e {segundo_numero}) são iguais.");

else:
    print(f"O números digitados ({primeiro_numero} e {segundo_numero}) não são iguais.");