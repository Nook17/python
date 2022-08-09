class Punkt :
  def __init__(self,x,y) :
    self.x = x
    self.y = y
    self._alfa = None
    self.__beta = 'tajemnica'
    
  def __str__(self) :
    '''
      Ta magiczna funkcja jest wywołana, gdy próbuję bezpośrednio wyświetlić
      obiekt jako obiekt np. poleceniem print(self)
    '''
    template = '''<[x={}, y={}], [{}]>''' #
    return template.format(self.x,self.y,self.__beta)

  # zwykła metoda w klasie 
  def metoda(self) :
    print('Jestem instrukcją metody klasy Punkt, wywołaną na rzecz jakiegoś obiektu')
    
  # poprzedza metodę statyczną, jest to tzw. DEKORATOR (nie podoba mi się to określenie )		
  @staticmethod 
  def metoda_statyczna() :    # nie ma self !!, wywołanie to A.metoda_statyczna_klasy()
    print('Jestem instrukcją metody statycznej klasy')
    return True
  
  # poprzedzenie nazwy metody dwoma __ działa jak dla atrybytów.
  # Nie można używać na zewnątrz klasy, chyba, ze   obiekt._A_metodachroniona() :)
  def __metoda_chroniona(self) : 			
    return True

  # dekorator zgłasza własność, która pobiera chronioną wartość/cechę
  @property
  def alfa(self):
    print('a tu pobieramy sobie alfę')
    return self._alfa
  
  # ustawia własność, która zmienia wartość chronioną
  @alfa.setter
  def alfa(self,v) :
    print('Zanim przypiszę wartość, mogę wywołać czyniącoą to funkę')
    self._alfa = v

  @alfa.deleter
  def alfa(self):
    print('no i sobie pokasujemy, bo co mamy robić?')
    del self._alfa
    
  @property
  def beta(self):
    return self.__beta