13. Receba um texto e retorne um dicionário com a contagem de frequência de cada palavra (minúscula e sem pontuação).
R:
import string

def contar_palavras(texto):
    palavras = texto.translate(str.maketrans("", "", string.punctuation)).lower().split()
    freq = {}
    for p in palavras:
        freq[p] = freq.get(p, 0) + 1
    return freq
