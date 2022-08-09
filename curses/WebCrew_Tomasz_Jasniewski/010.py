# KLASY i OBIEKTY
print('*'*468)

class Organizm :
  # poniższe pola są powiązane z klasą a nie obiektem, taka cecha klasy
  zdrowie = 100
  opis = 'To żyje!'
  
# użycie statycznych pól/własności klasy  (nie potrzeba obiektu by odwołać się do własności)
print(Organizm.opis, ' i ma ',str(Organizm.zdrowie) + '% zdrowia.')
# ale i obiekt posiada te pola
o1 = Organizm()
print(o1.opis,o1.zdrowie) # To żyje! 100
o2 = Organizm()
o2.zdrowie = 200 # to nie jest zdrowie klasy, tylko zdrowie obiektu :-P
print(o1.zdrowie, o2.zdrowie, Organizm.zdrowie) # 100 200 100

Organizm.zdrowie = 300 # i zmienione :)
print(o1.zdrowie, o2.zdrowie, Organizm.zdrowie) # 300 200 300 :-O
 


class Książka :  
  def __init__ (self, tytuł, autor, rok='2019') :   # konstruktor 
    '''
      Podaj argumenty: tytuł, autora i ewentualnie rok wydania
    '''
    print('Uruchomiono konstruktor klasy Książka')
    self.tytuł = tytuł
    self.autor = autor
    self.rok = rok
    self.__priv = 1 # ta zmienna jest prywatna, do użytku tylko wewnątrz klasy
    # ponieważ Python pozostawia dużo swobody jak to języki interpretowalne
    # można wykorzystać __priv poza klasą za pomocą :
    #     obiekt._Książka__priv
  def __del__(self) : # destruktor
    print('*** kaBUUUUM !!! ***')

book = Książka('Wiedźmaks', 'Fandrzej')
print (book.autor, book.rok)
try:
  print(book.__priv) # błąd, zatem wypluje wyjątek, który przechwycę
except Exception as e:
  print('Nie udało się wywołać book.__priv, ponieważ: ',e)
  
print (book._Książka__priv) # poprawnie, choć przestraszniająco
del book



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
    template = '''<punkt[x={}, y={}], [*{}*]>''' #
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
    print('Zanim przypiszę wartość, mogę wywołać ... cokolwiek innego! ')
    self._alfa = v

  @alfa.deleter
  def alfa(self):
    print('no i sobie pokasujemy, bo co mamy robić?')
    del self._alfa
    
  @property
  def beta(self):
    pass
    return self.__beta

p1 = Punkt(x=1,y=5)
p2 = Punkt(5,120)
print(p1)
p1.metoda()
Punkt.metoda_statyczna()
try:
  p1.metoda_chroniona()  # nie można wywołać metody chronionej wprost
except:
    print('Tylko to: ', p1._Punkt__metoda_chroniona()) # co najwyżej tak można

p1.wartość = 12*100 # tworzę własność w locie
print(p1.wartość)

try:
  p1.alfa(10)
except:
  print('''alfa jest getterem, setterem, deleterem - ale nie metodą -
        nie da się jej wywołać jako metody, gdyż to taka metoda co udaje własność/cechę obiektu''')

print(p2._alfa) # po prostu dobiorę się do własności _alfa
print(p2.alfa) # tu też dobiorę się do _alfa, ale poprzez @property (geter)
p2._alfa = 100 # przypisałem wartość bezpośrednio do _alfa
print(p2._alfa)
p2.alfa = 10 # przypisałem wartość do _alfa, ale wywołałem też funkcję ustawiającą !
print(p2._alfa)

del p2.alfa # wywołam deleter, czyli funkcję w momencue kasowania pola alfa

### settery, gettery, deletery - są po to, by kontrolować sytuację podczas zmian jakichś-tam
### własności. Np. gdy postać w grze,a ściślej jej zdrowie przyjmie wartość 0, możemy
### uruchomić setter, który odpali funkcje towarzyszące śmierci gracza/postaci.

print(p2.beta) #getter do własności chronionej działa (samo .__beta nie da się pobrać)

