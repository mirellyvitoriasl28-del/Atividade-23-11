10. Gere um número aleatório de 1 a 50 e peça palpites dando dicas ("Maior" ou "Menor") até o usuário acertar.
R:
import random

secreto = random.randint(1, 50)
tentativas = 0
while True:
    palpite = int(input("Palpite (1-50): "))
    tentativas += 1
    if palpite == secreto:
        print(f"Acertou em {tentativas} tentativas!")
        break
    print("Maior" if palpite < secreto else "Menor")
