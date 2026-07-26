'''
aprimore o desafio anterior. Mostre no final: a soma de todos os valores pares digitados, a soma dos valores da terceira coluna, o maior valor da segunda linha
'''

soma_par = 0
soma_coluna = 0
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f'digite o numero para {i, j}: ')))
    matriz.append(linha)

print("-=" * 30)
for i in range(3):
    maior = 0
    for j in range(3):
        #soma dos valores pares
        if matriz[i][j] % 2 == 0:
            soma_par += matriz[i][j]

        #soma dos valores da terceira coluna
        valor = matriz[i][2]
        if matriz[i][j] == valor:
            soma_coluna += valor

        #maior valor da segunda linha
        if matriz[1][j] > maior:
            maior = matriz[1][j]

        #matriz
        print(f'[{matriz[i][j]:^5}]', end=' ')
    print()

print(f'a soma dos valores pares digitados na matriz é {soma_par}')
print(f'a soma dos valores da terceira coluna é {soma_coluna}')
print(f'o maior valor da segunda linha é {maior}')


