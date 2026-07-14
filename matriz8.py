'''
Leia uma matriz 4x4 e informe qual é o maior número armazenado nela.
'''

matriz = []
maior = 0
for i in range(4):
    linha = []
    for j in range(4):
        linha.append(int(input(f"digite o número {i, j}: ")))
    matriz.append(linha)

for i in matriz:
    for p in i:
        if p > maior:
            maior = p
print(matriz)
print(f"o maior número armazenado na matriz é {maior}")