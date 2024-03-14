print('Progressão Aritmética\n------------')
a0 = int(input('Digite o início da Progressão: '))
r = int(input('Digite a Razão Da Progressão: '))
limite = int(input('Digite o Termo Limite da Progressão: '))

for x in range(a0,limite+1, r):
    print(x)
