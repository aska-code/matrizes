'''
criar uma matriz 3x3 e preencha com valores lido pelo teclado, no fim mostre a matriz na tela com a formatação correta
'''

matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f'digite um valor para {i, j}: ')))
    matriz.append(linha)
        
print('-=' * 30)
for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^5}]', end=' ')
    print()