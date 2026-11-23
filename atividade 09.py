9. Solicite um número N e imprima os N primeiros termos da sequência de Fibonacci. 
R:
n = int(input("Termos: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
