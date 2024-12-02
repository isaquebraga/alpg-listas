"""
Faça um algoritmo que irá fazer o cadastro de usuário. Para isso, solicita o nome do usuário, e a senha. Depois, pede que o usuário confirme novamente a senha. O sistema deverá verificar se as senhas digitadas são iguais. Se forem iguais, informar que o cadastro está correto. Se não forem iguais, informar que o cadastro não foi realizado porque as senhas não conferem.
"""

nomeUsuario = input("Digite seu nome: ")
senhaUsuario = input("Digite sua senha: ")
confirmacaoSenha = input("Confirme sua senha: ")

while senhaUsuario != confirmacaoSenha:
    print("\nCadastro não realizado! As senhas digitadas não são iguais.")
    confirmacaoSenha = input("Confirme novamente a sua senha: ")

print("Cadastro feito com sucesso.")