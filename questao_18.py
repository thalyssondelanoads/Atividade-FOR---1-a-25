def calcular_e_mostrar_soma(n):
  soma = 0
  denominador = n
  for x in range(1, n + 1):
    soma += x / denominador
    print(f'{x}/{denominador}',end='')
    print(' + ' if x < n else ' = ' , end='')
    denominador -= 1

  return soma

def main():
  print('Soma de Frações, Ex : 1/N + 2/N-1 + 3/N-2\n------------------------------')
  n = int(input('Digite o Número de Somas que Deseja : '))

  print('-'*30)
  soma = calcular_e_mostrar_soma(n)

  print(f'{soma:.3f}')

main()
