"""
    Faça um programa que leia o nome de uma pessoa e a sua idade. Imprima uma mensagem que diga "Olá, [nome]. Você terá  [idade] anos daqui a 10 anos". Os dados de entrada devem ser armazenados em variáveis distintas.
"""

nome = str(input("Digita o seu nome: "));
idade = int(input("Digite a sua idade: "));

print(f"Olá, {nome}. Você terá {idade+10} anos daqui a 10 anos.");