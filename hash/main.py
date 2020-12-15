#-*- coding:utf-8 -*-
import random

modulo = 10

def hash(num):
    global modulo
    return num%modulo

def hacerDatosFicticios():
    global modulo
    listaNumeros = []
    for i in range(modulo):
        listaNumeros.append(random.randint(0, (modulo * 10)))
    return listaNumeros

def hacerListaParaHash():
    global modulo
    listaHash = []
    for i in range(modulo):
        listaHash.append([])
    return listaHash

def guardarPorHash(listaNumeros, listaHash):
    for i in range(len(listaNumeros)):
        listaHash[hash(listaNumeros[i])].append(listaNumeros[i])
    return listaHash

def buscarPorHashSencillo(llave, listaHash):
    posicion = hash(llave)
    for i in range(len(listaHash[posicion])):
        if listaHash[posicion][i] != llave:
            pass
        else:
            return [posicion, i]
    return [posicion, -1]

def test():
    listaNumeros = hacerDatosFicticios()
    listaHash = hacerListaParaHash()
    listaHash = guardarPorHash(listaNumeros, listaHash)
    print(listaNumeros)
    print(listaHash)
    print(buscarPorHashSencillo(4, listaHash))

if __name__ == '__main__':
    test()

