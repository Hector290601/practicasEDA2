#-*-coding:utf-8-*-
import random

longitud = 10

def crearListaDeDatosAleatorios():
    datos = []
    for i in range(longitud):
        datos.append(random.randint(0, (longitud*10)))
    return datos

def busquedaLineal(llave, lista):
    for i in range(len(lista)):
        if lista[i] == llave:
            return i
    return -1

if __name__ == '__main__':
    datos = crearListaDeDatosAleatorios()
    print(datos)
    print(busquedaLineal(10, datos))
