palavraSecreta = "Alagoas"
palavraTracejada = ""

for i in palavraSecreta:
    palavraTracejada += "_" + " "

palavraSecreta = palavraSecreta.lower()

print("\nTema: Estados do Brasil\n")
print(palavraTracejada)

chutes = []

while "_" in palavraTracejada:
    chute = input("\nDigite uma letra: ").lower()
    
    while chute in chutes:
        print("\nVocê já chutou essa letra, tente novamente.")
        chute = input("Digite uma letra: ").lower()
        
    chutes.append(chute)
    
    letraEncontrada = False
    
    palavraTracejadaLista = list(palavraTracejada.replace(" ", ""))
    
    for indice, letra in enumerate(palavraSecreta):
        if letra == chute:
            letraEncontrada = True
            if indice == 0: 
                palavraTracejadaLista[indice] = letra.upper() 
            else:
                palavraTracejadaLista[indice] = letra
            
    if not letraEncontrada:
        print("\nVocê errou!")
        print(f"\n{palavraTracejada}")
    else:
        palavraTracejada = " ".join(palavraTracejadaLista)
        print(f"\n{palavraTracejada}")
    
    print(f"\n{chutes}")
    
print("\nParabéns, você ganhou.")
