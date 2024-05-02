def main():
  N = int(input("Insira o valor de N: "))

  total = 0
  sequencia = ""
  for i in range(1, N + 1):
      if i % 2 == 0:
          total -= 1 / i
          sequencia += f"- 1/{i}"
      else:
          if i == 1:
              sequencia += f"1/{i}"
          else:
              sequencia += f"+ 1/{i}"

      if i != N:
          sequencia += " "

  print(sequencia, "=", total)

main()
