19. Leia um arquivo logs.txt, conte ocorrências de [INFO], [WARNING] e [ERROR], e salve em relatorio.txt.
R:
def analisar_logs(entrada="logs.txt", saida="relatorio.txt"):
    contagem = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    with open(entrada, "r", encoding="utf-8") as f:
        for linha in f:
            for nivel in contagem:
                if f"[{nivel}]" in linha:
                    contagem[nivel] += 1
                    break
    with open(saida, "w", encoding="utf-8") as out:
        for nivel, total in contagem.items():
            out.write(f"{nivel}: {total}\n")
