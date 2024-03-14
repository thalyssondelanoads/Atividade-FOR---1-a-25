print('Números Inteiros Pares de 1 até N\n-------------------')
n = int(input('Até Qual Valor Deseja Mostrar os Números Inteiros Pares: '))
numeros = 0

for x in range (0, n):
    numeros += 1
    if numeros % 2 == 0:
        print(numeros)
