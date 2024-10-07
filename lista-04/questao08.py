"""
Elabore um algoritmo que solicita duas informações do usuário. A primeira, pergunta se possui bolsa família (S ou N), e a segunda, se possui mais de três filhos (S ou N). Se for contemplado pelo bolsa família e possuir mais de três filhos, deverá retornar Verdadeiro, significando que pode acessar à vaga de cotista.
"""

recebeBolsaFamilia = input("Você recebe Bolsa Família? (sim/não): ").lower()

while recebeBolsaFamilia != "sim" and recebeBolsaFamilia != "não":
    print("\nResposta inválida! Tente novamente.")
    recebeBolsaFamilia = input("Você recebe Bolsa Família? (sim/não): ").lower()

quantidadeFilhos = input("Você possui mais de três filhos? (sim/não): ").lower()

while quantidadeFilhos != "sim" and quantidadeFilhos != "não":
    print("\nResposta inválida! Tente novamente.")
    quantidadeFilhos = input("Você possui mais de três filhos? (sim/não): ").lower()

if recebeBolsaFamilia == "sim" and quantidadeFilhos == "sim":
    print("Você pode acessar à vaga de cotista.")
    
else: 
    print("Seu acesso à vaga de cotista foi negado.")