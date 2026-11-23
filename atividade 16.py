16. Implemente criptografar(texto, deslocamento) e descriptografar(texto, deslocamento) usando a Cifra de César.
R:
def criptografar(texto, deslocamento):
    res = []
    for c in texto:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            res.append(chr((ord(c) - base + deslocamento) % 26 + base))
        else:
            res.append(c)
    return "".join(res)

def descriptografar(texto, deslocamento):
    return criptografar(texto, -deslocamento)
