'''
• Atividade: Faça um programa que armazena os nomes e idades de 10 pessoas em uma
matriz, e imprime o nome da pessoa mais nova
'''
nova = 999
nome_nova = ''
matriz = []
for i in range(10):
    linha = []
    for j in range(1):
        linha.append((input(f"digite o nome da pessoa {i, j}: ")))
        linha.append(int(input(f"digite a idade da pessoa {i, j}: ")))
    matriz.append(linha)

print(matriz)
for p in matriz:
    if p[1] < nova:
        nova = p[1]
        nome_nova = p[0]
print(f"a pessoa mais nova é {nome_nova} com {nova} anos")