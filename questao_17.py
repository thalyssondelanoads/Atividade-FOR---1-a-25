def calcular_e_mostrar_soma(n):
  soma = 0
  for denominador in range(1,n+1):
    soma += 1/denominador                #FUNÇÃO QUE INCREMENTA OU DECREMENTA OS NÚMEROS DAS FRAÇÕES
    print(f'1/{denominador}',end='')
    print(' + ' if denominador < n else ' = ' , end='')
  
  return soma

def main():
  print('Soma de Frações, Ex : 1/1 + 1/2 + 1/3\n------------------------------')
  n = int(input('Digite o Número de Somas que Deseja : '))

  print('-'*30)
  soma = calcular_e_mostrar_soma(n)

  print(f'{soma:.3f}')

main()
