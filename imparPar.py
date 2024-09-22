"""
Jogue "Ímpar ou Par" com o computador. O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""

import random

# Título do Jogo
print("=" * 50)
msg = "Ímpar ou Par? O Desafio"
print(f"{msg:^50}")
print("=" * 50)

vitorias = 0

while True:
    computador = random.randint(0, 10)
    jogador = int(input("Digite um valor: "))
    resultado = computador + jogador

    parImpar = str(input("Ímpar ou Par? [i/p]: ")).upper()
    print()

    # Caso o resultado for par
    if resultado % 2 == 0:
        if parImpar == "P":
            print("Você venceu!")
            vitorias += 1
        else:
            print("Você perdeu")
            # Exibição das escolhas caso derrota
            print(f"Computador:{computador} jogador:{jogador} Resultado:{resultado}")
            break

    # Caso o resultado for ímpar
    else:
        if parImpar == "I":
            print("Você venceu!")
            vitorias += 1
        else:
            print("Você perdeu")
            # Exibição das escolhas caso derrota
            print(f"Computador:{computador} jogador:{jogador} Resultado:{resultado}")
            break

    # Exibição das escolhas caso vitória
    print(f"Computador:{computador} jogador:{jogador} Resultado:{resultado}")
    print()

# Score final
print(f"\nTotal de vitórias: {vitorias}")
