"""
    Área de um Triângulo: Escreva um algoritmo que solicita ao usuário a base e a altura de um triângulo, depois calcula e exibe a área do triângulo. A fórmula para calcular a área de um triângulo é: área = (base x altura) / 2.
"""

base = float(input("Digite a base do triângulo: "))
altura = float(input("Digite o altura do triângulo: "))

area = (base * altura) / 2;

print(f"A área do triângulo descrito é {area:.2f}.")