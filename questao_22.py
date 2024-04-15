def main():
  print('Frigorífico\n---------------------')
  n = int(input('Digite Quantos Bois Deseja Cadastrar : '))

  boi_mais_pesado = boi_mais_leve = 0
  qtd_bois = 0
  for x in range (1,n+1):
    qtd_bois += 1
    print(f'-------------------\nInformações do Boi {qtd_bois}: \n-------------------')
    n_identificaçao = int(input('Digite o Nº de Identificação do Boi : '))
    peso = float(input('Digite o Peso do Boi : '))

    #VERIFICA SE O PRÓXIMO VALOR DO LOOP É MAIOR OU MENOR QUE O ANTERIOR
    if x == 1:
      boi_mais_pesado = peso
      boi_mais_leve = peso
      id_mais_pesado = n_identificaçao
      id_mais_leve = n_identificaçao
    
    else:
      if peso > boi_mais_pesado:
        boi_mais_pesado = peso
        id_mais_pesado = n_identificaçao
      if peso < boi_mais_leve:
        boi_mais_leve = peso
        id_mais_leve = n_identificaçao

  print(f'''=========== RELATÓRIO ===========
  
Peso do Boi Mais Pesado : {boi_mais_pesado}
Nº de Identificação : {id_mais_pesado}
_____________________________________
Peso do Boi Mais Leve : {boi_mais_leve}
Nº de Identificação : {id_mais_leve}''')

main()
  
