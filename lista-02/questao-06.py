"""
    Escreva um algoritmo que solicita ao usuário uma quantidade de tempo em segundos e então a converte para horas. Por exemplo, se o usuário inserir 3666 segundos, o programa deve imprimir "1 hora", sem considerar os segundos restantes.
"""

segundos = int(input("Digite a quantidade de segundos que você deseja tranformar em horas: "));
horas = segundos // 3600;

print(f"{segundos} segundos equivale(m) a {horas} hora(s).");