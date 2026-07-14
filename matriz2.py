'''
Faça um programa que leia duas matrizes A e B 2x2 de inteiros e imprima a matriz C que é a
soma das matrizes A e B
'''

matriz_A = []
matriz_B = []
for i in range(2):
    linha = []
    for j in range(2):
        linha.append(int(input(f"digite o número {i, j} da primeira matriz: ")))
    matriz_A.append(linha)
for i in range(2):
    linha = []
    for j in range(2):
        linha.append(int(input(f"digite o número {i, j} da segunda matriz: ")))
    matriz_B.append(linha)

print(f"primeira matriz {matriz_A}")
print(F"segunda matriz {matriz_B}")

matriz_C = []
for i in range(2):
    linha = []
    for j in range(2):
        linha.append(matriz_A[i][j] + matriz_B[i][j])
    matriz_C.append(linha)
print(f"soma das duas matrizes {matriz_C}")

