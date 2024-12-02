"""
Elabore um algoritmo para representar um sistema de compra de produtos agrícolas de uma feira, mas que só permite compras à vista.
"""

produtos = {
    'Alface': 2.00,
    'Batata': 3.50,
    'Cebola': 3.00,
    'Cenoura': 4.00,
    'Tomate': 5.00
}

def exibirProdutos():
    print("Produtos disponíveis na feira:")
    for nomeProduto, precoProduto in produtos.items():
        print(f"{nomeProduto}: R$ {precoProduto:.2f}")

def calcularTotal(compra):
    total = 0
    for produto, quantidade in compra.items():
        total += produtos[produto] * quantidade
    return total

def realizar_compra():
    compra = {}
    exibirProdutos()

    while True:
        produto = input("\nDigite o nome do produto que deseja comprar (ou 'sair' para finalizar): ").capitalize()
        
        if produto == 'Sair':
            break

        if produto in produtos:
            quantidade = int(input(f"Digite a quantidade de {produto} que deseja comprar: "))
            compra[produto] = compra.get(produto, 0) + quantidade
        else:
            print("Produto não disponível. Tente novamente.")

    if compra:
        total = calcularTotal(compra)
        print(f"\nValor total da compra: R$ {total:.2f}.")
        print("\nEste sistema aceita apenas compras à vista.")
        confirmar = input("Deseja confirmar a compra? (sim/não): ").lower()
        
        if confirmar == "sim":
            pagamento = float(input("\nDigite o valor do pagamento à vista: R$ "))

            while pagamento < total:
                print("\nPagamento insuficiente. Tente novamente.")
                pagamento = float(input("Digite o valor do pagamento à vista novamente: R$ "))
            
            troco = pagamento - total

            if troco > 0:
                print(f"\nCompra realizada com sucesso! Seu troco é: R$ {troco:.2f}")
            else: 
                print("\nCompra realizada com sucesso!")

            print("Obrigado e volte sempre!")
        else:
            print("\nCompra cancelada.")
    else:
        print("\nNenhum item no carrinho. Compra cancelada.")

realizar_compra()
