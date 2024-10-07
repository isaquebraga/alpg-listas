"""
Elabore um algoritmo para que só possa autorizar a entrada na loja, àqueles que estão com a anuidade de associação em dia ou pagar o valor de 25 reais na entrada.
"""

anuidadeEmDia = input("Você está com a anuidade de associação em dia? (sim/não): ").lower()

while anuidadeEmDia != "sim" and anuidadeEmDia != "não":
    print("Resposta inválida! Tente novamente.")
    anuidadeEmDia = input("Você está com a anuidade de associação em dia? (sim/não): ").lower()

if anuidadeEmDia == "sim":
    print("Acesso a entrada na loja autorizado.")
elif anuidadeEmDia == "não":
    print("Você não possui acesso a entrada na loja.")
    print("No entanto, pode conseguir acesso pagando uma taxa de R$25,00.")

    pagamento = input("Deseja pagar? (sim/não): ").lower()

    while pagamento != "sim" and pagamento != "não":
        print("Resposta inválida! Tente novamente.")
        pagamento = input("Deseja pagar? (sim/não): ").lower()

    if pagamento == "sim":
        print("Acesso liberado via pagamento.")
    else:
        print("Acesso negado.")
