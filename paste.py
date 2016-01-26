#! /usr/bin/env python3
# coding: utf-8

import sys

DELIMITADOR = "\t"

def checa_delimitador():
    global DELIMITADOR
    previous = ""
    for i, parametro in enumerate(sys.argv):
        if previous == "-d":
            DELIMITADOR = parametro
            break
        previous = parametro
    else:
        return
    del sys.argv[i]
    del sys.argv[i - 1]

checa_delimitador()

if len(sys.argv) < 3:
    print("Passe pelo menos dois nomes de arquivo", file=sys.stderr)
    sys.exit(1)

with open(sys.argv[1]) as arq1,  open(sys.argv[2]) as arq2:
    for linha1, linha2 in zip(arq1, arq2):
        print (linha1.strip("\n"), linha2.strip("\n"), sep=DELIMITADOR)
