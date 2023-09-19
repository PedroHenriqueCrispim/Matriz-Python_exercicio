# preenche a matriz
matriz = []
for i in range(3):                  # linha
    linha = []
    for j in range(5):              # coluna
        n = int(input('Numero: '))
        linha.append(n)
    matriz.append(linha)

print(matriz)

# exibe a matriz
for i in range(len(matriz)):         # linhas
    for j in range(len(matriz[0])):  # colunas
        print(matriz[i][j], end='\t')
    print()
