'''
Faç•a um programa que leia uma matriz 3x3 de inteiros e retorne a linha de maior soma.
Imprima na tela a matriz, a linha de maior soma e a soma.
'''

matriz = []
maior = 0
linha_maior = ''
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f"digite o número{i, j}: ")))
    matriz.append(linha)

print(matriz)
for i in matriz:
    soma = 0
    for p in i:
        soma += p
        if soma > maior:
            maior = soma
            linha_maior = i

print(f"a linha de maior soma é {linha_maior} e a soma é {maior}")