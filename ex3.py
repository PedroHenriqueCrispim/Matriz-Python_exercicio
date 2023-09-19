def exibir(matriz):
    # exibe a matriz
    print()
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end='\t')
        print()

# preenche a matriz
matriz = []
for i in range(3):
    linha = []
    for j in range(5):
        n = int(input('Numero: '))
        linha.append(n)
    matriz.append(linha)
exibir(matriz)

# altera os valores maiores que 100 para 0
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if matriz[i][j] > 100:
            matriz[i][j] = 0
exibir(matriz)