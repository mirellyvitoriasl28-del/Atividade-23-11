11. Crie uma função que receba uma lista de números e retorne (maior, menor, media) sem usar max() ou min().
R:
def analisar_lista(numeros):
    maior = menor = numeros[0]
    soma = 0
    for n in numeros:
        if n > maior: maior = n
        if n < menor: menor = n
        soma += n
    return (maior, menor, soma / len(numeros))
