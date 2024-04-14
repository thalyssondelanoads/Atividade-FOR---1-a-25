def calcular_soma(n):
  soma = 0
  for x in range(1,n+1):
    soma += 1/x
    print(f'1/{x}',end='')
    print(' + ' if x < n else ' = ' , end='')
  
  return soma

def main():
  print('Soma de Frações, Ex : 1/1 + 1/2 + 1/3\n------------------------------')
  n = int(input('Digite o Número de Somas que Deseja : '))

  print('-'*30)
  soma = calcular_soma(n)

  print(f'{soma:.3f}')

main()
