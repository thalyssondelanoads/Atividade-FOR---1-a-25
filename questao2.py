def main():
  print('Números Inteiros Pares de 1 até N\n-------------------')
  n = int(input('Até Qual Valor Deseja Mostrar os Números Inteiros Pares: '))
  numeros = 0
  
  for x in range (1, n):
      numeros += 1
      if x % 2 == 0:
          print(x)

main()
