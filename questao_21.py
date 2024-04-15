def calcular_e_mostrar_soma(n):
    numerador = 1
    soma = 0
    for denominador in range(1,n+1):
        soma += (numerador/denominador)
        print(f'{numerador}/{denominador}',end='')
        print(' + ' if denominador < n else ' = ', end='')
        numerador += 2

    return soma

def main():
    print('Soma de Frações, Ex : 1/1 + 3/2 + 5/3\n---------------------')
    n = int(input('Digite o Número de Somas que Deseja : '))

    print('-'*30)
    soma = calcular_e_mostrar_soma(n)

    print(f'{soma:.3f}')

main()
