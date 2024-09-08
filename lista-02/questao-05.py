"""
    Escreva um algoritmo que leia a nota de 3 estudantes e retorne a média das notas.
"""

notas = [];
quant_notas = 3;
media = 0;

for i in range(0, quant_notas):
    notas.append(float(input("Digite sua nota: ")));
    
for i in range(0, quant_notas):
    media += notas[i];
    
media /= len(notas);
print(f"A média entre as notas é: {media:.2f}.");