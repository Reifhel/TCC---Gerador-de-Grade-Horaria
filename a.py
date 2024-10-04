def encontrar_gaps(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    gaps = []

    # Iterar por cada coluna
    for col in range(colunas):
        valores_na_coluna = [matriz[linha][col] for linha in range(linhas)]

        # Verifica gaps entre valores diferentes de 0
        for i in range(1, linhas - 1):
            if valores_na_coluna[i] == 0 and valores_na_coluna[i-1] != 0 and valores_na_coluna[i+1] != 0:
                gaps.append((i, col))

    return gaps


# Exemplo de uso
matriz = [[1, 2, 3], [0, 0, 3], [2, 3, 0]]
gaps = encontrar_gaps(matriz)
print("Gaps encontrados nas posições:", gaps)
