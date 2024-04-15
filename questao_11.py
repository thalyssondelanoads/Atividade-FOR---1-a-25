def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def main():
    limite_inferior = int(input('Digite o Limite Inferior : '))
    limite_superior = int(input('Digite o Limite Superior : '))

    for numeros in range (limite_inferior,limite_superior+1):
        if eh_primo(numeros):
            print(numeros)

main()
