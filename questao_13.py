def main():
    print('Maior Número da Lista\n-----------------------')

    n = int(input('Quantos Números Deseja Digitar : '))

    for x in range (1,n+1):
        numero = float(input(f'Digite o {x}º Número : '))

        if x == 1:
            numero_maior = numero
        else:
            if numero > numero_maior:
                numero_maior = numero
        
    print(f'-----------------------\nMaior Número : \033[36m{numero_maior}\033[m')
            
main()
