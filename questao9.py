def main():
  print('Números Pares entre Limites\n--------------------------')
  limite_inferior = int(input('Digite o Limite Inferior : '))
  limite_superior = int(input('Digite o Limite Superior : '))
  
  for x in range (limite_inferior,limite_superior):
    if x % 2 == 0:
      print(x)

main()
