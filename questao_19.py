def main():
  N = int(input("Insira o valor de N: "))

  total = 0
  sequencia = ""
  for i in range(1, N + 1):
      if i % 2 == 0:
          total -= i / (N - (i - 1))
          sequencia += f"- {i}/{N - (i - 1)}"
      else:
          if i == 1:
              sequencia += f"{i}/{N - (i - 1)}"
          else:
              sequencia += f"+ {i}/{N - (i - 1)}"

      if i != N:
          sequencia += " "
        
  print(sequencia, "=", total)

main()
