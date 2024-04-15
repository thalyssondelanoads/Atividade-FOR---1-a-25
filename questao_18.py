def calcular_e_mostrar_soma(n):
  soma = 0
  for numerador in range(n,0,-1):
    denominador = n - numerador + 1
    soma += (numerador/denominador)
    print(f'{numerador}/{denominador}',end='')
    print(' + ' if numerador > n else ' = ' , end='')

  return soma

def main():
  print('Soma de Frações, Ex : 1/N + 2/N-1 + 3/N-2\n------------------------------')
  n = int(input('Digite o Número de Somas que Deseja : '))

  print('-'*30)
  soma = calcular_e_mostrar_soma(n)

  print(f'{soma:.3f}')

main()
