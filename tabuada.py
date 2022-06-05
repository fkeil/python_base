#!/usr/bin/env python
"""" Imprime a tgabuada do 1 ao 10 """
__version__ = "0.0.1"
__author__ = "Fernando"

# base = [1,2,3,4,5,6,7,8,9,10]
numeros = list(range(1, 11))  # O ultimo numero ele nao gera!

# Iterable (percorriveis)

for numero in numeros:
    print("Tabuada do:", numero)
    print("----------------------")
    for outro_numero in numeros:
        print(numero * outro_numero)
    print("----------------------")
