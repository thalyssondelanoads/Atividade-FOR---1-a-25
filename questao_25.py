def vencedor_eleiçao(qtd_votos_candidato_um,qtd_votos_candidato_dois,qtd_votos_candidato_tres):
    if qtd_votos_candidato_um > qtd_votos_candidato_tres and qtd_votos_candidato_um > qtd_votos_candidato_dois:
        return 'Candidato 1'
    elif qtd_votos_candidato_dois > qtd_votos_candidato_um and qtd_votos_candidato_dois > qtd_votos_candidato_tres:
        return 'Candidato 2'
    elif qtd_votos_candidato_tres > qtd_votos_candidato_dois and qtd_votos_candidato_tres > qtd_votos_candidato_um:
        return 'Candidato 3'
    else:
        return 'EMPATE'

def main():
    print('''==== Eleição Presidencial ====
Candidato 1 : [1]
Candidato 2 : [2]
Candidato 3 : [3]
Voto Nulo : [9]
Voto em Branco [0]
==========================''') 
    
    n = int(input('Digite a Quantidade de Eleitores : '))
    
    qtd_votos_candidato_um = 0
    qtd_votos_candidato_dois = 0
    qtd_votos_candidato_tres = 0
    qtd_votos_nulos = 0
    qtd_votos_brancos = 0
    
    for x in range (1,n+1):
        voto = int(input('Digite Seu Voto : '))
        
        if voto == 1:
            qtd_votos_candidato_um += 1
        if voto == 2:
            qtd_votos_candidato_dois += 1
        if voto == 3:
            qtd_votos_candidato_tres += 1
        if voto == 9:
            qtd_votos_nulos += 1
        if voto == 0:
            qtd_votos_brancos += 1
        
    vencedor = vencedor_eleiçao(qtd_votos_candidato_um,qtd_votos_candidato_dois,qtd_votos_candidato_tres)
    print(f'''   ====== RESULTADOS ======
    VOTOS CANDIDATO 1 : {qtd_votos_candidato_um}
    VOTOS CANDIDATO 2 : {qtd_votos_candidato_dois}
    VOTOS CANDIDATO 3 : {qtd_votos_candidato_tres}
    VOTOS NULOS : {qtd_votos_nulos}
    VOTOS EM BRANCO : {qtd_votos_brancos}
    \033[36mVENCEDOR\033[m = {vencedor}''')

main()
