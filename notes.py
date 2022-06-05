#!/usr/bin/env python3
""" Bloco de notas

$ notes.py new "Minnha nota"
tag: tech
text:
Anotacao geral sobre tecnologia

$ notes.py read --tag=tech
notas com a tag tech sao exibidas
...
...
"""

__version__ = "0.1.0"

import os
import sys
from datetime import datetime

path = os.curdir
filepath = os.path.join(path, "notes.txt")

cmds = ("read", "new")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage")
    print(cmds)
    sys.exit(1)

if arguments[0] not in cmds:
    print(f"Invalid command '{arguments[0]}'")
    sys.exit(1)

if arguments[0] == "read":
    for line in open(filepath):
        user, timestamp, title, tag, text = line.split("\t")
        if tag.lower() == arguments[1].lower():
            print(f"title : {title}")
            print(f"text : {text}")
            print(f"by: {user} in {timestamp}")
            print("-" * 30)
            print()

if arguments[0] == "new":
    user = os.getenv("USER", "anonymous")
    timestamp = datetime.now().isoformat()
    if len(arguments) == 1:
        title = input("Please provide a note title: ")

    else:
        title = arguments[1]
    text = [
        f"{user}",
        f"{timestamp}",
        f"{title}",
        input("please add a tag to your note: ").strip(),
        input("type your note:\n").strip(),
    ]
    with open(filepath, "a") as file_:
        file_.write("\t".join(text) + "\n")
