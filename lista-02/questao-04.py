"""
    Escreva um algoritmo que leia o nome de uma pessoa, o ano em que ela nasceu. Em seguida imprima uma mensagem que diga "Olá, [nome], hoje você tem [idade] anos". Considere que os dados de entrada devem ser armazenados em variáveis distintas, e o cálculo da idade deve se basear no ano atual.
"""

import datetime;

nome = str(input("Digite o seu nome: "));
ano_nascimento = int(input("Digite a data do seu nascimento: "));
ano_atual = datetime.datetime.now().year;

print(f"Olá, {nome}, hoje você tem {ano_atual-ano_nascimento} anos.");