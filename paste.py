#! /usr/bin/env python3
# coding: utf-8

import sys

DELIMITADOR = "\t"

if len(sys.argv) < 3:
    print("Passe pelo menos dois nomes de arquivo", file=sys.stderr)
    sys.exit(1)

def le_linha(arq):
    arq_acabou = False
    try:
        linha = next(arq)
    except StopIteration:
        arq_acabou = True
        linha = ""
    return linha, arq_acabou


with open(sys.argv[1]) as arq1,  open(sys.argv[2]) as arq2:
    arq1_acabou  = arq2_acabou = False
    while not (arq1_acabou and arq2_acabou):
        linha1, arq1_acabou = le_linha(arq1)
        linha2, arq2_acabou = le_linha(arq2)
        print (linha1.strip("\n"), linha2.strip("\n"), sep=DELIMITADOR)
