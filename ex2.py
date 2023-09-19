# preenche a matriz
matriz = []
for i in range(6):
    lista = []
    for j in range(6):
        if i == j:              # indice de linha igual ao indice de coluna
            lista.append(1)
        else:
            lista.append(0)
    matriz.append(lista)
print(matriz)

# exibe a matriz
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j], end='\t')
    print()