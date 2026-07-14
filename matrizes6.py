'''
Crie uma matriz 3x3 preenchida pelo usuário e exiba todos os valores na tela.
'''

matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f"digite o número {i, j}: ")))
    matriz.append(linha)

print(matriz)