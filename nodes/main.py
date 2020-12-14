# -*- coding:utf-8 -*-

class primerNodo:
	genero = ''
	anio = 0
	distribuidor = ''
	plataformas = ['']
	nombre = ''
	def __init__(self, stringNombre, stringGenero, intAnio, stringDistribuidor, listPlaformas = ['Pc']):
		self.genero = stringGenero
		self.anio = intAnio
		self.distribuidor = stringDistribuidor
		self.nombre = stringNombre
		self.plataformas = listPlaformas
	def __str__(self):
		datosDelJuego = ''
		#datosDelJuego += 'El juego ' + self.nombre + ' es de género ' + self.genero + ' salió en el año  ' + self.anio + ' disponible para: ' + str(self.plataformas) + ' y le pertenece a ' + self.distribuidor + '\n'
		datosDelJuego += 'El juego ' + self.nombre + ' es de género ' + self.genero + ' salió en el año  ' + self.anio + ' disponible para: '
		# El juego Smash bros es de género Pela salió en el año 1997 disponible para: ['N64', 'NSitch'] y le pertenece a Nintendo
		# El juego Smash bros es de género Pela salió en el año 1997 disponible para: N64, NSitch, y le pertenece a Nintendo
		# El juego Smash bros es de género Pela salió en el año 1997 disponible para: N64, NSitch, le pertenece a Nintendo
		# El juego Smash bros es de género Pela salió en el año 1997 disponible para: N64, NSitch y le pertenece a Nintendo
		cadena = ''
		longitud = len(self.plataformas)
		for i in range(0, longitud, 1):
			if i + 1< longitud:
				cadena += self.plataformas[i] + ', '
			else:
				cadena += self.plataformas[i]
		datosDelJuego += cadena + ' y le pertenece a ' + self.distribuidor + '\n'
		return datosDelJuego

if __name__ == '__main__':
	#videojuego = primerNodo('Smash Bros', 'Pelea', '1997', 'Nintendo', ['N64', 'NSwitch'])
	#videojuego = primerNodo('Fortnite', 'Shooter', '2018', 'Epic games', ['Xbox', 'Play', 'PC', 'Android', 'iOs'])
	videojuego = primerNodo('Fortnite', 'Shooter', '2018', 'Epic games')
	print(primerNodo)
	print(videojuego)

