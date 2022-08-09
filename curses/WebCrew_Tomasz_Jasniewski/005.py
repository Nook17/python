# PODSTAWOWE KOLEKCJE
# https://docs.python.org/3.7/library/collections.html
'''
tuple (krotka)
list (lista)
set (zbiór)
dict (słownik)
'''
   
    # zbiór - wartości nie będą się nigdy powtarzać, nawet jak dodam zdublowane
zbiór = { 1, 2, 2, 3 }
print('zbiór=',zbiór, type(zbiór))
zbiór2 = { }  # pusty ... zbiór? Nie! Słownik.
print('zbiór2', zbiór2, type(zbiór2))

zbiór3 = set() # to samo co {}
print(zbiór3,type(zbiór3))
zbiór3.add(1)
zbiór3.add(3)
zbiór3.add(100)
zbiór3.add(0)
zbiór3.add(100)
print('zbiór3', zbiór3, type(zbiór3))
zbiór3.remove(100) # usuwa ale musi być
zbiór3.discard(3) # usuwa o ile jest (jak nie ma to nic się nie dzieje)
print('zbiór3.pop()',zbiór3.pop())
print('zbiór3', zbiór3, type(zbiór3))
zbiór3.clear()

    # ciekawostką jest że argument dla set( ) może być czymś
    # "iteracyjnym" np krotka, lista albo ... tekst jako ciąg znaków
set1 = set([5,4,1,2,3,3,3]) # 3 nie będzie powtórzone
print ('set1:',set1)
set2 = set('literki') # literki są jako zbiór ! ani alfabetycznie ani się nie powtórzą
print ('set2:',set2)
set3 = sorted(set2)
print ('set3 as sorted: set2',set3)
set4 = set([3,4,5,6,7,8])
print(set1.difference(set4)) # wynikiem podzbiór z set1, którego nie ma w set4
print(set1.union(set4)) # zbiór z obu zbiorów, dalej nie ma dubli
print(set1.intersection(set4)) # część wspólna
print(set1.isdisjoint(set4)) # zwraca TRUE gdy nie ma wspólnych elementów
print(set1.issubset(set4)) # TRUE gdy set1 zawiera się w set4 (cały)
print(set1.issuperset(set4)) # TRUE gdy każdy element set4 jest w set1
set5 = set4.copy()
print("set5",set5)


    # słownik (ma dowolne klucze, dla jednego klucza jedna wartość)
słownik = { 'a' : 1, 'banan' : 'ciarki', 123 : 120, 120: 'Rabarbar' }
print('słownik:',słownik, type(słownik))
print(słownik['a'], słownik['banan'], słownik[123], słownik[120] ,sep='  *  ')
print(type(słownik['a']), type(słownik['banan']), type(słownik[123]), type(słownik[120]) ,sep='  *  ')
del słownik['a']  # ciekawe, co robi del ?
print (słownik)

di = dict()
di['rycerz']='Rodryg Podkowa'
di['dama']='Gertruda von Wieża Zamkowa'
di[102]='Rudy'

di2 = di.copy()
print("di2:",di2)
di2.clear()
print(di2)

print(len(di))
print(di['dama'])
print('rycerz' in di)
print('pies' not in di)
print('kot' in di)
print(di[102])
print(di.get(102))
print(di.get(103,'nie za bardzo'))
print(di.items()) # zwraca specjalną klasę dict_items (dokładniej o tym w ćwiczeniach nr 1, po poznaniu pętli)
print(di.keys()) # klucze
print(di.values()) # wartości
print(di.popitem()) # od 3.7 gwarancja LIFO    - usuwa ostatni dodany i zwraca  
print(di.update(dama='Królowa Śniegu'))
print(di)      




