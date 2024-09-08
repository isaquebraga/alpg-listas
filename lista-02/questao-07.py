"""
    Escreva um algoritmo que solicita ao usuário uma temperatura em graus Celsius e a converte para graus Fahrenheit e Kelvin. Use as fórmulas Fahrenheit = Celsius * 1.8 + 32 e Kelvin = Celsius + 273.15 para realizar as conversões.
"""

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = celsius * 1.8 + 32;
kelvin = celsius + 273.15;

print(f"A temperatura {celsius:.2f} °C equivale a {fahrenheit:.2f} °F e {kelvin:.2f} K.")