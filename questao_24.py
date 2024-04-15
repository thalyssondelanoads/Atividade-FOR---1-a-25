def main():
  print('Pesquisa IBGE\n------------------------')
  n = int(input('Digite o Número de Habitantes da Pesquisa : '))

  qtd_habitantes = 0
  salario_total = 0
  salarios_baixos = 0
  total_filhos = 0
  for x in range (1,n+1):
    qtd_habitantes += 1
    print(f'--------------\nDados do(a) Habitante {qtd_habitantes} : \n--------------')
    
    salario = float(input('Digite seu Salário : '))
    salario_total += salario
    if salario <= 1000:
      salarios_baixos += 1

    n_filhos = int(input('Digite o Número de Filhos : '))
    total_filhos += n_filhos

  media_salarial = salario_total / qtd_habitantes
  media_filhos = total_filhos / qtd_habitantes
  percentual_salarios_baixos = (salarios_baixos / qtd_habitantes) * 100

  print(f'''========= RELATÓRIO =========

  MÉDIA SALARIAL DA POPULAÇÃO : R$ {media_salarial:.2f}
  MÉDIA DE FILHOS POR HABITANTE : {media_filhos:.1f}
  PERCENTUAL DE SALÁRIOS ABAIXO DE R$ 1000.00 : {percentual_salarios_baixos:.1f}%''')
  
main()
