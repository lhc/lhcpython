#! /usr/bin/env python3
# coding: utf-8

import sys

DELIMITADOR = "\t"

if len(sys.argv) < 3:
    print("Passe pelo menos dois nomes de arquivo", file=sys.stderr)
    sys.exit(1)

with open(sys.argv[1]) as arq1,  open(sys.argv[2]) as arq2:
    arq1_acabou = False; arq2_acabou=False 
    while not (arq1_acabou and arq2_acabou):
        try:
            linha1 = next(arq1)
        except StopIteration:
            arq1_acabou = True
            linha1 = ""
        try:
            linha2 = next(arq2)
        except StopIteration:
            arq2_acabou = True
            linha2 = ""
        print (linha1.strip("\n"), linha2.strip("\n"), sep=DELIMITADOR)
