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


def checa_parametros():
    if len(sys.argv) < 3:
        print("Passe pelo menos dois nomes de arquivo", file=sys.stderr)
        sys.exit(1)
    return sys.argv[1:3]

def principal(arq1_nome, arq2_nome):
    with open(arq1_nome) as arq1,  open(arq2_nome) as arq2:
        for linha1, linha2 in zip(arq1, arq2):
            print (linha1.strip("\n"), linha2.strip("\n"), sep=DELIMITADOR)

def principal_mesmo():
    checa_delimitador()
    arq1, arq2 = checa_parametros()
    principal(arq1, arq2)

if __name__ == "__main__":
    principal_mesmo()