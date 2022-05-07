#!/usr/bin/env python3
"""Hello World multilinguas.

Dependo da lingua configurada no ambiente (ENV) o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variavel LANG devidamente configurada ex:

    export LANG=pt_BR

Execucao:

    python3 hello.py
ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = " Fernando Keil"
__license___ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = ("Hello, World!")

if current_language == "pt_BR":
    msg = "Ola, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour, Monde!"

print(msg)
