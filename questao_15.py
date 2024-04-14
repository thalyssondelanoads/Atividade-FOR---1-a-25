def main():
  print('Termos de um Sequência, Ex : 1,3,6,10,15...\n----------------------------------')
  n = int(input('Quantos Termos da Sequência Deseja Ver : '))

  contador = 0
  numero = 0
  for x in range (1,n+1):
    contador += 1
    sequencia = numero + contador
    numero = sequencia 
    print(numero,end=' ')
    
main()
