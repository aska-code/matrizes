'''
Faça um programa que leia uma matriz 3x3 de inteiros e multiplique os elementos da diagonal principal da matriz por um número k. Imprima a matriz na tela antes e depois da multiplica•ção.
'''

matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f"digite o número {i, j}: ")))
    matriz.append(linha)

print(matriz)

numero = int(input(f"digite o número que você quer mutiplicar a diagonal: "))

for i in range(3):
    for j in range(3):
        if i == j:
            matriz[i][j] = matriz[i][j] * numero
print(matriz)