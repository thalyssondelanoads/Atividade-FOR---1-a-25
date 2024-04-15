def main():
    print(''' ==== Informação Salarial ====
\033[36mPAGAMENTOS\033[m : R$ 12.00 / Hora
R$ 40.00 Reais / Dependentes
\033[31mDESCONTOS\033[m : 8.5% para o INSS
5% para o IR
==============================''')
    
    qtd_funcionarios = int(input('Digite a Quantidade de Funcionários : '))
    print('_'*30)

    for qtd_funcionarios in range(1,qtd_funcionarios+1):
        horas_trabalhadas = int(input('Digite a Quatidade de Horas Trabalhadas : '))
        numero_dependentes = int(input('Digite o Nº de Dependentes : '))

        salario_bruto = (horas_trabalhadas * 12) + (numero_dependentes * 40)
        desconto_inss = salario_bruto * 0.085
        desconto_ir = salario_bruto * 0.05
        salario_liquido = salario_bruto - desconto_inss- desconto_ir

        print(f'''\033[32mINFORMAÇÕES DO FUNCIONÁRIO\033[m \033[33m{qtd_funcionarios}\033[m:
\033[35mSALÁRIO BRUTO\033[m : R${salario_bruto:.2f}
\033[31mDESCONTOS\033[m : INSS = R${desconto_inss:.2f}
IR = R${desconto_ir:.2f}
\033[36mSALÁRIO LÍQUIDO\033[m : R${salario_liquido:.2f}
==============================================''')

main()
