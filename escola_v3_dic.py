#!/usr/bin/env python3

""" Exibe relatorio de criancas por atividade
 Imprimir a lista de criancas agrupadas por sala que frequentam em cada uma das atividades.
"""

__version__="0.1.2"

#Dados
salas = {
    1:{"Erik","Maia","Gustavo","Manuel","Sofia","Joana"},
    2:{"Joao","Antonio","Carlos","Maria","Isolda"}
}

#Atividades
atividades = {
    "Ingles":{"Erik","Maia","Joana","Carlos","Antonio"},
    "Musica":{"Erik","Carlos","Maia"},
   "Danca":{"Gustavo","Sofia","Joana","Antonio"}
}

#Listar alunos em cada atividade por sala

print("*"*30)

for nome_atividade, alunos_atividade in atividades.items():
    print(f"Alunos da atividade {nome_atividade}")
    print("-"*30)
    for sala, alunos_sala in salas.items():
        print(f"Sala {sala} -> ", alunos_sala.intersection(alunos_atividade))
        print("*"*30)
