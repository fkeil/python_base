#!/usr/bin/env python3

""" Exibe relatorio de criancas por atividade
 Imprimir a lista de criancas agrupadas por sala que frequentam em cada uma das atividades.
"""

__version__="0.1.1"

#Dados
sala1 = ["Erik","Maia","Gustavo","Manuel","Sofia","Joana"]
sala2 = ["Joao","Antonio","Carlos","Maria","Isolda"]

#Atividades
aula_ingles = ["Erik","Maia","Joana","Carlos","Antonio"]
aula_musica = ["Erik","Carlos","Maia"]
aula_danca = ["Gustavo","Sofia","Joana","Antonio"]

#Listar alunos em cada atividade por sala
atividades = [("Ingles", aula_ingles),("Musica", aula_musica),("Danca", aula_danca)]

print("*"*30)

for nome_atividade, atividade in atividades:
    atv_sl1 = set(sala1) & set(atividade)
    atv_sl2 = set(sala2).intersection(atividade)

    print(f"{nome_atividade} Sala 1 ", atv_sl1)
    print(f"{nome_atividade} Sala 2 ", atv_sl2)
    print("*"*30)
