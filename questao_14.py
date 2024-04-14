def main():
  print('Maior Quadrado Igual ou Menor que N\n--------------------------')
  numero = int(input('Digite o Número : '))

  for x in range (numero,0,-1):
    quadrado = x**0.5
    if quadrado == int(quadrado):
      print(f'_________________\nO Maior Quadrado é {x}')
      break
      
main()
