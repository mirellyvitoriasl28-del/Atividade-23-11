20. Encontre o caminho de 'I' até 'F' em um labirinto 2D ('0' livre, '1' parede) usando recursão e backtracking.
R:
def resolver_labirinto(labirinto):
    linhas, colunas = len(labirinto), len(labirinto[0])
    caminho, visitados = [], set()
    inicio = next((r, c) for r in range(linhas) for c in range(colunas) if labirinto[r][c] == 'I')

    def backtrack(r, c):
        if not (0 <= r < linhas and 0 <= c < colunas) or labirinto[r][c] == '1' or (r, c) in visitados:
            return False
        caminho.append((r, c))
        visitados.add((r, c))
        if labirinto[r][c] == 'F':
            return True
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if backtrack(r + dr, c + dc):
                return True
        caminho.pop()
        return False

    return caminho if backtrack(*inicio) else "Sem saída"
