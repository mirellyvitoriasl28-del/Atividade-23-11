12. Crie uma função que verifique se uma palavra ou frase é um palíndromo, ignorando espaços e maiúsculas.
R:
def eh_palindromo(texto):
    limpo = "".join(c.lower() for c in texto if c.isalnum())
    return limpo == limpo[::-1]
