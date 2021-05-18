"""
Un taller de diseño de autos quiere estudiar un nuevo prototipo. Para eso, nos piden hacer un modelo concentrado en las características del motor. El prototipo de motor tiene 5 cambios (de primera a quinta), y soporta hasta 5000 rpm. La velocidad del auto se calcula así: (rpm / 100) * (0.5 + (cambio / 2)). Por ejemplo en tercera a 2000 rpm, la velocidad es 20 * (0.5 + 1.5) = 40. También nos interesa controlar el consumo. Se parte de una base de 0.05 litros por kilómetro. A este valor se le aplican los siguientes ajustes:
- Si el motor está a más de 3000 rpm, entonces se multiplica por (rpm - 2500) / 500. Por ejemplo, a 3500 rpm hay que multiplicar por 2, a 4000 rpm por 3, etc.
- Si el motor está en primera, entonces se multiplica por 3.
- Si el motor está en segunda, entonces se multiplica por 2.
Los efectos por revoluciones y por cambio se acumulan. Por ejemplo, si el motor está en primera y a 5000 rpm, entonces el consumo es 0.05 * 5 * 3 = 0.75 litros/km. El modelo debe entender estos mensajes:

arrancar() , se pone en primera con 500 rpm.
subirCambio()
bajarCambio()
subirRPM(cuantos)
bajarRPM(cuantos)
velocidad()
consumoActualPorKm(), calcula el consumo actual y lo devuelve

Al ejecutar esto:
auto1 = Auto()
auto1.arrancar()
auto1.subirRPM(3500)
auto1.subirCambio()
auto1.subirCambio()
auto1.subirCambio()
auto1.bajarCambio()
la velocidad debería ser 80 y el consumo 0.15 litros/km.
"""


class Auto():
	def __init__(self):
		self.consumo = 0.05
		self.rpm = 0
		self.cambio = None

	def arrancar(self):
		self.cambio = 1
		self.rpm = 500

	def subirCambio(self):
		if self.cambio < 5:
			self.cambio += 1

	def bajarCambio(self):
		if self.cambio > 1:
			self.cambio -= 1
	
	def subirRPM(self, cantidad):
		if self.rpm + cantidad <= 5000:
			self.rpm += cantidad
		else:
			self.rpm = 5000

	def bajarRPM(self, cantidad):
		if self.rpm - cantidad >= 0:
			self.rpm -= cantidad
		else:
			self.rmp = 0
		

	def velocidad(self):
		return ((self.rpm / 100) * (0.5 + (self.cambio / 2)))

	def consumoActualPorKm(self):
		if self.rpm > 3000:
			if self.cambio == 1:
				return (self.consumo * ((self.rpm - 2500) / 500) * 3)
			elif self.cambio == 2:
				return (self.consumo * ((self.rpm - 2500) / 500) * 2)
			elif self.cambio <= 5:
				return (self.consumo * ((self.rpm - 2500) / 500))
		elif self.cambio == 1:
			return (self.consumo * 3)
		elif self.cambio == 2:
			return (self.consumo * 2)
		else:
			return (self.consumo)
	
	def cambioActual(self):
		return (self.cambio)

	def rpmActual(self):
		return (self.rpm)
