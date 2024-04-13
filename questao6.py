def main():  
  print('Tabuada de 1 a 10\n-----------------')
  numero = int(input('Qual Tabuada Deseja Ver?: '))
  
  
  if 1 <= numero <= 10:
      tabuada = 0
      print('__________________')
      for x in range (1,10):
          tabuada += 1
          resultado = numero * tabuada
          print(f'{numero} x {tabuada} = {resultado}')
      print('__________________')
  else:
      print('-------------------\nApenas Números de 1 a 10 Serão Mostrados')

main()
