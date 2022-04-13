class Titan():
	def __init__(self, salud):
		self.salud = salud
		self.correr = False

	def salud_actual(self):
		return self.salud

	def recibir_ataque(self, cantidad):
		self.salud -= 1.5 * cantidad

	def grito(self):
		return "¡Aaaarrrg!"

	def cuantas_casas(self):
		return (self.salud * 8 / 100)

	def destruir_casas(self):
		if (self.cuantas_casas() > 1):
			if ((self.cuantas_casas() % 1) > 0):
				self.salud -= (self.cuantas_casas() // 1) * 12.5
			else:
				self.salud -= (self.cuantas_casas() - 1) * 12.5
		else:
			print("No puede destruir ninguna casa")

	def esta_vivo(self):
		return (self.salud > 0)







class Enterprise():
	def __init__(self):
		self.potencia = 50
		self.coraza = 5

	def potencia_actual(self):
		return self.potencia

	def coraza_actual(self):
		return self.coraza

	def encontrarPilaAtomica(self):
		if self.potencia + 25 <= 100:
			self.potencia += 25
		else:
			self.potencia = 100

	def encontrarEscudo(self):
		if self.coraza + 10 <= 20:
			self.coraza += 10
		else:
			self.coraza = 20

	def recibirAtaque(self, puntos):
		if puntos <= self.coraza:
			self.coraza -= puntos
		else:
			self.potencia -= puntos - self.coraza
			self.coraza = 0

	def fortalezaDefensiva(self):
		return (self.coraza + self.potencia)

	def necesitaFortalecerse(self):
		return (self.coraza == 0 and self.potencia < 20)
		
	def fortalezaOfensiva(self):
		if self.potencia >= 20:
			return ((self.potencia - 20) / 2)
		else:
			return 0
