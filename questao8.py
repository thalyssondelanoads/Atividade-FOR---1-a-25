def main():
  print("Múltiplos de N em uma Sequência")
  n = int(input("Insira o valor de N: "))
  limite_inferior = int(input("Insira o Limite inferior: "))
  limite_superior = int(input("Insira o Limite superior: "))
  
  for x in range(limite_inferior,limite_superior+1):
      if x % n == 0:
          print(x)

main()
