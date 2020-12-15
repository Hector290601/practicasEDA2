#-*- coding: utf-8 -*-
import time

def crearDatos(longitud):
    lista = []
    for i in range(longitud):
        lista.append(i)
    return lista

def bsuquedaBinaria(llave, arreglo):
    longitud = len(arreglo)
    fin = longitud
    mitad = longitud // 2
    inicio = 0
    posicion = arreglo[mitad]
    lugar = mitad
    while posicion != llave and longitud >= 1:
        time.sleep(0.5)
        if llave > posicion:
            longitud = len(arreglo[mitad:fin])
            inicio = mitad
            mitad = longitud // 2
            lugar += mitad
            posicion = arreglo[inicio + mitad]
        elif llave < posicion:
            longitud = len(arreglo[inicio:mitad])
            fin = mitad
            mitad = longitud // 2
            lugar -= fin
            posicion = arreglo[fin - mitad]
        else:
            return -1
    return lugar

if __name__ == '__main__':
    datos = crearDatos(10)
    print(datos)
    print(bsuquedaBinaria(8, datos))

