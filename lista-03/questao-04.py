"""
    Identificando Desigualdades: Crie um exercício onde o aluno deve usar os operadores != e == para comparar números ou strings, como por exemplo, verificar se 'Python' é igual a 'python' ou se 100 é diferente de 200.
"""

opcao_escolhida = int(input(
"""
O que você deseja comparar?

    [1] - Textos
    [2] - Números

Digite aqui: """
));

while (opcao_escolhida != 1 and opcao_escolhida != 2):
    opcao_escolhida = int(input("\nOpção digitada inválida! Tente novamente: "));

if (opcao_escolhida == 1):
    primeiro_texto = input("Digite o primeiro texto ou palavra que você deseja comparar: ");
    segundo_texto = input("Agora digite o segundo texto ou palavra que você deseja comparar: ");

    if (primeiro_texto == segundo_texto):
        print("Os textos são iguais.")
    else:
        print("Os textos são diferentes.")

else:
    primeiro_numero = int(input("Digite o primeiro número que você deseja comparar: "));
    segundo_numero = int(input("Agora digite o segundo número que você deseja comparar: "));

    if (primeiro_numero == segundo_numero):
        print("Os números são iguais.")
    else:
        print("Os números são diferentes.")