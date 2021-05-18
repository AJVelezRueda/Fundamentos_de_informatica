"""
Se está pensando en el diseño de un juego que incluye la nave espacial Enterprise. En el juego, esta nave tiene un nivel de potencia de 0 a 100, y un nivel de coraza de 0 a 20. La Enterprise puede:
- encontrarse con una pila atómica, en cuyo caso su potencia aumenta en 25.
- encontrarse con un escudo, en cuyo caso su nivel de coraza aumenta en 10.
- recibir un ataque, en este caso se especifican los puntos de fuerza del ataque recibido. La Enterprise "detiene" el ataque con la coraza, y si la coraza no alcanza, el resto se descuenta de la potencia. Por ejemplo si la Enterprise con 80 de potencia y 12 de coraza recibe un ataque de 20 puntos de fuerza, puede parar solamente 12 con la coraza, los otros 8 se descuentan de la potencia. La nave debe quedar con 72 de potencia y 0 de coraza. Si la Enterprise no tiene nada de coraza al momento de recibir el ataque, entonces todos los puntos de fuerza del ataque se descuentan de la potencia.
La potencia y la coraza tienen que mantenerse en los rangos indicados, por ejemplo, si la Enterprise tien 16 puntos de coraza y se encuentra con un escudo, entonces queda en 20 puntos de coraza, no en 26. Tampoco puede quedar negativa la potencia, a lo sumo queda en 0. La Enterprise nace con 50 de potencia y 5 de coraza. Implementar este modelo de la Enterprise, que tiene que entender los siguientes mensajes:

potencia()
coraza()
encontrarPilaAtomica()
encontrarEscudo()
recibirAtaque(puntos)

Al ejecutar esto:
enterprise = Enterprise()
enterprise.encontrarPilaAtomica()
enterprise.recibirAtaque(14)
enterprise.encontrarEscudo()
la potencia de la Enterprise debe ser 66, y su coraza debe ser 10.

Agregar al modelo de la Enterprise, la capacidad de entender estos mensajes.

fortalezaDefensiva(), que es el máximo nivel de ataque que puede resistir, o sea, coraza más potencia.
necesitaFortalecerse(), tiene que ser true si su coraza es 0 y su potencia es menos de 20.
fortalezaOfensiva(), que corresponde a cuántos puntos de fuerza tendría un ataque de la Enterprise. Se calcula así: si tiene menos de 20 puntos de potencia entonces es 0, si no es (puntos de potencia - 20) / 2.
"""


class Enterprise():
	def __init__(self):
		self.pot = 50
		self.cor = 5

	def potencia(self):
		return self.pot

	def coraza(self):
		return self.cor

	def encontrarPilaAtomica(self):
		if self.pot + 25 <= 100:
			self.pot += 25
		else:
			self.pot = 100

	def encontrarEscudo(self):
		if self.cor + 10 <= 20:
			self.cor += 10
		else:
			self.cor = 20

	def recibirAtaque(self, puntos):
		if puntos <= self.cor:
			self.cor -= puntos
		else:
			self.pot -= puntos - self.cor
			self.cor = 0

	def fortalezaDefensiva(self):
		return (self.cor + self.pot)

	def necesitaFortalecerse(self):
		return (self.cor == 0 and self.pot < 20)

	def fortalezaOfensiva(self):
		if self.pot >= 20:
			return ((self.pot - 20) / 2)
		else:
			return 0