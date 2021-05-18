class MedioDeTransporte:
	def __init__(self, combustible = 100):
		self.combustible = combustible
	
	def cargar_combustible(self, cantidad):
		self.combustible += cantidad

	def combustibleActual(self):
		return self.combustible
	
	def entran(self, numero):
		return (numero <= self.maxPersonas())

class Auto(MedioDeTransporte):
	def maxPersonas(self):
		self.max_personas = 5
		return(self.max_personas)

	def recorrer(self, km):
		self.combustible -= km / 2

class Moto(MedioDeTransporte):
	def maxPersonas(self):
		self.max_personas = 2
		return self.max_personas

	def recorrer(self, km):
		self.combustible -= km / 2


moto1 = Moto(200)
moto2 = Moto()
auto1 = Auto(300)
auto2 = Auto()

print(moto1.entran(3))
print(moto1.entran(2))
print(auto1.entran(2))
print(auto1.entran(6))
print(moto1.combustibleActual(), moto2.combustibleActual(), auto1.combustibleActual(), auto2.combustibleActual())