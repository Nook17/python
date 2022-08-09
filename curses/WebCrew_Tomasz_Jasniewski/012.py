# D Z I E D Z I C Z E N I E
# dziedziecznie jest w nawiasie po nazwie klasy. Klasa object - to taka klasa bazowa pythona,
# która dostarcza innym obiektom pewnych wspólnych elementów, np. __class__
class A (object) :
  pass

print('=' * 468)

a = object()
print(a.__class__) # nazwa własna klasy obiektu a
print('napis'.__class__) # ha! wszystko jest obiektem !!


print('*' * 80)

class B(object):
  klasowa=None # przypominam, to pole związane z klasą a nie nowymi obiektami
  def __init__(self,x=10):
    self.x=x
    print('Jestem konstruktorem klasy B wywołanym \
przy tworzeniu obiektu klasy ' + str(self.__class__))

class C(B):
  pass

b=B(5)
c=C(2)
d=C()
print(b.klasowa) # gdy obiekt nie ma tego pola, pobiera to pole z klasy B (= B.stała)
b.klasowa=2 # zmienna 'stała' obiektu to nie to samo co B.stała, zatem tu powstanie pole obiektu
print(B.klasowa,b.klasowa) # widać, że pole B.stała nie zmieniło się, a b.stała to nowe pole obiektu
B.klasowa=3 # teraz zmieniam własność całej klasy B
print(b.x, c.x, d.x, B.klasowa, C.klasowa) # dziedziczone x, dziedziczona klasowa z B (w C)

print('*' * 80)

from klasy2 import *
class Koło(Punkt) :
  '''Opis klasy, będzie dostępny pod polem __doc__ dla każdego obiektu oraz dla samej klasy'''
  def __init__(self,x,y,r) :    
    # wywołanie konstruktora z klasy-przodka
    super().__init__(x,y) 
    self.r = r
  def __str__(self) :
    # pobieram __str__ z przodka i dopier dodaję swoją część
    return super().__str__() + ' {r=' + str(self.r) + '}'

k1 = Koło(10,24,120)
print(k1,k1.__class__,k1.__doc__,Koło.__doc__,Koło.mro(),sep='\n')

print('*' * 80, 'KołoŻycia')

# D Z I E D Z I C Z E N I E z kilkoma przodkami
class KołoŻycia(Koło, Organizm) :
  def __init__(self,x,y,r) :    
    Koło.__init__(self,x,y,r)
    Organizm.__init__(self,50,'pięknie żyje')    
  def __str__(self) :
    # super() z Koła czy Organizmu ?
    return Koło.__str__(self) + ' ' + Organizm.__str__(self)

k2 = KołoŻycia(10,24,120)
print(k2)
print(KołoŻycia.mro())
print (hasattr(k2,'opis'))
print(getattr(k2,'zdrowie',1))
print(getattr(k2,'zdrowie2','brak zmiennej, ale coś sobie zwrócę'))


## POLIMORFIZM - funkcje/metody mogą występować pod jedną nazwą a być zdefiniowane
# dla różnych argumentów. Zachowania polimorficzne w przypadku np. C++ musimy
# zaprogramować. PYTHON 3 jest w zasadzie naturalnie polimorficzny.
print('*' * 80, 'POLIMORFIZM')

def f1(arg) :
  print(arg)

# f1 jest polimorficzna "na mocy Python'a". Można jej użyć niemal z dowolnym typem danych.
f1(1)
f1('a')
f1([1,2,3])

### ASERCJE
# Asercja to mechanizm testu czy coś jest tym, co ja myślę że jest :)
# jeżeli myślę, że zmienna x jest równa 10 mogę to sprawdzić - jak sprawdzenie się nie uda,
# program zwróci błąd, a jak się uda nic się nie stanie
x = 10
assert x == 10
# ASERCJE przydają się do obiektów klas, które tworzymy
assert hasattr(k2, 'zdrowie') # sądzę, że k2 ma pole zdrowie. Jak nie ma - błąd

## asercja + try
try:
  assert x==12
except :
  print('mylisz się, x to nie jest 12')





