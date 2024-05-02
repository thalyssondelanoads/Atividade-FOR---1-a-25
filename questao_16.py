def main():
  N = int(input("Insira o valor de N (Maior ou Igual a 2): "))
  fib1, fib2 = 0, 1

  print(fib1)
  print(fib2)

  for x in range(2, N):
      fib_atual = fib1 + fib2
      print(fib_atual)
      fib1, fib2 = fib2, fib_atual
  
main()
