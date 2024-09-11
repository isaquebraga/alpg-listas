"""
    Maior ou Menor?: Solicite a criação de um script que compare dois números (como 15 e 30) usando os operadores > e <, imprimindo os resultados dessas comparações.
"""

primeiro_numero = int(input("Digite um número: "));
segundo_numero = int(input("Digite um segundo número para que eu descubra quem é o maior: "));

if (primeiro_numero > segundo_numero):
    print(f"O número {primeiro_numero} é maior que o número {segundo_numero}.");

elif (primeiro_numero < segundo_numero):
    print(f"O número {primeiro_numero} não é maior que o número {segundo_numero}.");

else:
    print(f"O números digitados ({primeiro_numero} e {segundo_numero}) são iguais.");