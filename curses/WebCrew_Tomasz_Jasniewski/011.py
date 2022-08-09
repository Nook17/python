# MODUŁY
# czyli dane z innego pliku .py, np. z pliku modul.py 
''' 
modul.py:
#############################
print('plik modul.py')
info = 'to jest plik modułowy'
def f1():
	return 100
	
class A:
	def __init__(self):
		print(True or False)
		pass
############################# 
'''	

'''
import modul
print(modul.f1())
print(modul.info + '!')
obiekt = modul.A()
'''

'''
# modulsy/modul.py
from modulsy.modul import *
print(info+'!')
f1()
obiekt = A()
'''


# PAKIETY
  # posiadam katalog <klasy>
  # w katalogu <klasy> jest plik __init__.py  (uruchamiany gdy jest import katalogu <klasy>
  # w katalogu <klasy> są pliki np. Punkt.py z definicją klasy Punkt itd.

''' __init__.py
--------------------------------------------------------------------------------------------------------
globalna = 100
def f1():
	print('jestem f1')
def f2():
	print('jestem f2')

# gdy będzie from klasy import * - zostaną zaimportowane tylko te rzeczy na liście !		
__all__ = ["globalna","f1"] 
print('Zładowano pakiet klasy.  ')
'''
'''
import klasy.Punkt # import klasy/Punkt.py - to jest prefix

# wprawdzie ładuję Punkt, ale przy okazji uruchamiam __init__.py z katalogu klasy ...
# ... i dzięki temu widzę elementy z pliku __init__.py
print(klasy.globalna)
klasy.f1()
klasy.f2()

# z klasy.Punkt (prefix) weź klasę Punkt i utwórz obiekt p0 tej klasy
p0 = klasy.Punkt.Punkt(0,0)
print(p0)

# referencja do klasy Punkt, w katalogu klasy z pliku Punkt
Pkt = klasy.Punkt.Punkt  
p1 = Pkt(1,2) # Pkt reprezentuje klasę Punkt
print(p1)
'''


'''
from klasy import *
print(globalna)
f1()
# f2() # niezdefiniowana, bo nie dostarczona w __all__ z pliku __init__.py !!!

from klasy import Punkt
Pkt = Punkt.Punkt
p0 = Pkt(3,5)
print(p0)


from klasy.Punkt import *
p1=Punkt(0,200)
print(p1)


# Dzięki plikowi __init__.py, który z katalogu czyni pakiety, 
# mam większą kontrolę nad importem.
'''




''' __init__.py z klasy2
---------------------------------------------------
from klasy2.Punkt import Punkt
from klasy2.Organizm import Organizm
'''

from klasy2 import *
p0 = Punkt(1,25)
print(p0)

org = Organizm(5,'śluz i parzydełka')
print(org)

# Uwaga! W katalogu z pakietem mogą być pod-katalogi jako podpakiety!



