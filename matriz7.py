'''
Crie uma matriz 3x3 com números inteiros e mostre a soma de todos os elementos.
'''

matriz = []
soma = 0
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f"digite o número {i, j}: ")))
    matriz.append(linha)

for i in matriz:
    for p in i:
        soma += p

print(matriz)
print(f"a soma de todos os valores é: {soma}")