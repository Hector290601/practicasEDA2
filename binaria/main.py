#-*- coding: utf-8 -*-
import time

def crearDatos(longitud):
    lista = []
    for i in range(longitud):
        lista.append(i*10)
    return lista
"""
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
"""

def busquedaBinaria(llave, datos):
    inicio = 0
    fin = len(datos)
    encontrado = False
    while inicio <= fin and not encontrado:
        mitad = (inicio + fin) // 2
        if mitad < len(datos):
            if datos[mitad] == llave:
                encontrado = True
                break
            else:
                if llave < datos[mitad]:
                    fin = mitad - 1
                else:
                    inicio = mitad + 1
        else:
            break
    if encontrado:
        return mitad
    else:
        return -1

if __name__ == '__main__':
    datos = crearDatos(10)
    print(datos)
    for i in range(11):
        print('La busqueda  de ', (i*10), ' regresó el valor: ',  busquedaBinaria(i*10, datos))

