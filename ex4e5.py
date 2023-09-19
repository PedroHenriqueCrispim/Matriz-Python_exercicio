import random

def preencher(linha, coluna):
    matriz = []
    for i in range(linha):
        linha = []
        for j in range(coluna):
            n = random.randint(1, 10)
            linha.append(n)
        matriz.append(linha)
    return matriz

def exibir(matriz):
    print()
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end='\t')
        print()

def soma_diagonal_principal(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i == j:                      # indice de linha == indice de coluna
                soma += matriz[i][j]
    return soma

def soma_diagonal_secundaria(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i + j == len(matriz)- 1:
                soma += matriz[i][j]        # soma dos indices == tamanho fa matriz - 1
    return soma

matriz = preencher(5, 5)
exibir(matriz)
print(f'Soma diagonal principal: {soma_diagonal_principal(matriz)}')
print(f'Soma diagonal secundária: {soma_diagonal_secundaria(matriz)}')