print('Soma Dos Números Entre 1 e N\n-----------------------')
n = int(input('Até Qual Número Deseja Somar: '))

numeros = 0
soma = 0
for x in range (1,n+1):
    numeros += 1
    soma += numeros
print(f'-------------------------\nA Soma de Todos os Números entre 1 e {n} = {soma}')
