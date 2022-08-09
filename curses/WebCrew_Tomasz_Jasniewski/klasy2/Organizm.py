class Organizm :
	'''Organizm to klasa określana przez zdrowie i opis'''
	def __init__(self,zdrowie,opis):
		self.zdrowie = zdrowie
		self.opis = opis
	def __str__(self) :
		'''
			opis obiektu Organizm
		'''
		template = '''Organizm: zdrowie={}, opis={}'''
		return template.format(self.zdrowie,self.opis)