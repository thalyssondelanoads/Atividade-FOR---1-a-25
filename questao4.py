def main():
  print("Progressão Geométrica\n-------------------")
  A0 = int(input("Valor inicial : "))
  Limite = int(input("Insira o Limite : "))
  R = int(input("Razão : "))
  
  atual = A0
  while atual < Limite:
      print(atual)
      atual *= R

main()
