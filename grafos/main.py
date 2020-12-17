# -*- coding: utf-8 -*-
import random

class Nodo:
	to = 0
	costo = 0
	sig = None

class Grafo:
	edges = []
	grado = []
	numNodos = 0
	numEdges = 0
	dirigido = False

def iniciarGrafo(grafoVar):
	i = 0
	while i <= grafoVar.numNodos:
		grafoVar.grado.append(0)
		grafoVar.edges.append(None)
		i += 1

def insertarArista(grafoVar, a, b, costo, dirigida):
	item = Nodo()
	item.costo = costo
	item.to = b
	item.sig = grafoVar.edges[a - 1]
	grafoVar.edges[a] = item
	grafoVar.grado[a] += 1
	if dirigida == False and b != a:
		insertarArista(grafoVar, b, a, costo, True)

def crearGrafo(grafoVar, costo, datos = None):
	i = 0
	if datos == None:
		while i < grafoVar.numEdges:
			u = int(input('U: '))
			v = int(input('V: '))
			if costo == True:
				cost = input('Costo: ')
			else:
				cost = 1
			insertarArista(grafoVar, u, v, cost, grafoVar.dirigido)
			i += 1
	else:
		while i < grafoVar.numEdges:
			u = datos[random.randint(0, (len(datos) - 1))]
			v = datos[random.randint(0, (len(datos) - 1))]
			if costo == True:
				cost = random.randint(0, 10)
			else:
				cost = 1
			insertarArista(grafoVar, u, v, cost, grafoVar.dirigido)
			i += 1

def imprimirGrafo(grafoVar):
	i = 1
	item = None
	string = ""
	while i <= grafoVar.numNodos:
		string += str(i) + "\t"
		item = grafoVar.edges[i]
		while item != None:
			string += str(item.to) + "%" + str(item.costo) + "\t"
			item = item.sig
		string += "\n"
		i += 1
	return string

def test():
	dirigido = int(input('Es dirigido? 1)Sí, 2)No: '))
	cost = int(input('Las aristas tienen peso? 1)Sí, 2)No: '))
	grafoVar.numNodos = int(input('Número de nodos: '))
	grafoVar.numEdges = int(input('Número de aristas: '))
	grafoVar.dirigido = True if dirigido == 1 else False
	cost = True if cost == 1 else False
	iniciarGrafo(grafoVar)
	crearGrafo(grafoVar, cost)
	print(imprimirGrafo(grafoVar))

def conDatos(datos):
	tamanio = len(datos)
	grafoVar.numNodos = tamanio
	grafoVar.dirigido = bool(random.getrandbits(1))
	grafoVar.numEdges = random.randint(0, tamanio)
	costo = bool(random.getrandbits(1))
	iniciarGrafo(grafoVar)
	crearGrafo(grafoVar, costo, datos)
	print(imprimirGrafo(grafoVar))
	return grafoVar

grafoVar = Grafo()

if __name__ == '__main__':
	#test()
	conDatos([1, 2, 3, 5, 6, 7, 8, 9, 10])

