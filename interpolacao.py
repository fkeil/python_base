#!/bin/usr/env python3
""" Imprime a mensagem de um email

NAO MANDE SPAM!!!
"""
__version__ = "0.1.1"
__author__ = "Fernando Keil"

import os
import sys

arguments = sys.argv[1:]
if not arguments:
    print("Informe o nome do arquivo que contem os enderecos de email")
    sys.exit(1)


filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path,filename)
templatepath = os.path.join(path, templatename)

clientes = []
for line in open(filepath):
    name, email = line.split(",")
    
    # TODO: Substituir por servidor smtp para envio de emails
    print (f"Enviando email para: {email}")
    print(
        open(templatepath).read()
        %{
            "nome" : name,
            "produto" : "camera",
            "texto" : "fabricados de maneira ecologica",
            "link" : "https://bit.ly/uos80Us",
            "quantidade" : 2,
            "preco" : 15.42,
        }
    )
    print("-" * 50)
