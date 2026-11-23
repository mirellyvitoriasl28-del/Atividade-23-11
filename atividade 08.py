8. Peça um número inteiro e exiba sua tabuada de 1 a 10 com um laço for.
R:
n = int(input("Número: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
