#!/usr/bin/env python3
""" Calculadora infix,

Funcionamento:
[operacao] [n1] [n2]

Operacoes:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$infixcalc.py sum 5 2
7

$infixcalc.py mul 10 5
50

$infixcalc.py
operacao: sum
n1: 5
n2: 4
9

Salva os logs das operacoes no arquivo infixcalc.log
"""
__version__ = "0.1.1"
author = "Fernando Keil"

import sys
import os
from datetime import datetime

variables = {
    "opr": None,
    "n1": None,
    "n2": None,
}

operacoes = {
    "sum": "+",
    "sub": "-",
    "mul": "*",
    "div": "/",
}

arguments = sys.argv[1:]


# TODO: Exceptions
if not arguments:
    operation = input("Qual a operacao matematica desejada? ")
    n1 = input("Qual o valor do primeiro numero? ")
    n2 = input("Qual o valor do segundo numero? ")
    arguments = [operation, n1, n2]

elif len(arguments) != 3:
    print("Numero de argumentos invalidos!")
    print("ex: 'sum 5 5'")
    sys.exit(1)

operation, *nums = arguments

valid_operations = ("sum", "sub", "mul", "div")
if operation not in valid_operations:
    print(f"Operacao invalida '{operation}'")
    print("Estas sao as operacoes validas: ", valid_operations)
    sys.exit(1)

validated_nums = []
for num in nums:
    # TODO: repeticao while + exeptions
    if not num.replace(".", "").isdigit():
        print(f"Numero invalido '{num}'!")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)

n1, n2 = validated_nums

# TODO: Usar dicionario de funcoes
if operation == "sum":
    result = n1 + n2
if operation == "sub":
    result = n1 - n2
if operation == "mul":
    result = n1 * n2
if operation == "div":
    result = n1 / n2

path = os.curdir
filepath = os.path.join(path, "infixcalc.log")
timestamp = datetime.now().isoformat()
user = os.getenv("USER", "anonymous")

with open(filepath, "a") as file_:
    file_.write(
        f"{user} || {timestamp} ---> {operation}, {n1}, {n2} = {result}\n"
    )

print(f"O resultado da operacao e {result}")
