def main():
  print('Soma e Média de Números\n--------------------------')
  qtd_numeros = int(input('Quantos Número Deseja Digitar : '))
  
  soma = 0
  for x in range (1,qtd_numeros+1):
    numero = int(input('Digite o Número : '))
    soma += numero

  media = soma / qtd_numeros

  print('_____________________')
  print(f'''Soma dos Números = {soma}
Média dos Números = {media}''')
    
main()
