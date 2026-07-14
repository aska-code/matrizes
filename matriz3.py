'''
Faça um programa que leia as dimensões de duas matrizes A e B, e depois leia as duas
matrizes (os elementos devem ser inteiros). Se as matrizes forem de tamanhos compatíveis para
multiplicação, multiplique as matrizes. Imprima as matrizes A, B e a matriz resultante da
multiplicação.
'''
matriz1 = []
matriz2 = []
linha1 = int(input("digite quantas linhas a primeira matriz terá: "))
coluna1 = int(input("digite quantas colunas a primeira matriz terá: "))
for i in range(linha1):
    linha = []
    for j in range(coluna1):
        linha.append(int(input(f"digite o numero {i, j} da primeira matriz: ")))
    matriz1.append(linha)

linha2 = int(input("digite quantas linhas a segunda matriz terá: "))
coluna2 = int(input("digite quantas colunas a segunda matriz terá: "))
for i in range(linha2):
    linha = []
    for j in range(coluna2):
        linha.append(int(input(f"digite o numero {i, j} da segunda matriz: ")))
    matriz2.append(linha)

print(f"primeira matriz {matriz1}")
print(f"sefunda matriz {matriz2}")

if coluna1 == linha2:
    matriz3 = []
    for i in range(linha1):
        linha = []
        for j in range(coluna2):
            total = 0
            for k in range(coluna1):
                total += (matriz1[i][k] * matriz2[k][j])
            linha.append(total)
        matriz3.append(linha)
    print(f"resultado da multiplicação das matrizes {matriz3}")
else:
    print("as matrizes são incompativeis para multiplicar")