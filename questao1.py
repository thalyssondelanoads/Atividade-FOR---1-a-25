def main():
  print('Números Inteiros de 1 até N\n-------------------')
  n = int(input('Até Qual Valor Deseja Mostrar os Números Inteiros: '))
  
  numeros = 0
  for x in range (0, n+1):
      numeros += 1
      print(x)

main()
