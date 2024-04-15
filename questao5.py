def main():
    print('Fatorial de um Número\n-----------------------')

    n = int(input('Digite o Número que Deseja Calcular: '))
    
    fatorial = 1
    for sequencia in range(1,n+1):
        fatorial *= sequencia
        print(sequencia,end=' ')
        print('x' if sequencia < n else '=',end=' ')
    
    print(fatorial)

main()
