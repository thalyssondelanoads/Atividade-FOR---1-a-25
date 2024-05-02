def main():
  print("Progressão Geométrica\n-------------------")
  a0 = int(input("Valor inicial : "))
  limite = int(input("Insira o Limite : "))
  r = int(input("Razão : "))
  
  atual = a0
  while atual < limite:
      print(atual)
      atual *= r

main()
