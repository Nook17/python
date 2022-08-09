# PODSTAWOWE KOLEKCJE
# https://docs.python.org/3.7/library/collections.html
'''
tuple (krotka)
list (lista)
set (zbiór)
dict (słownik)
'''
    # krotka, czyli zbiór, którego wartości nie można zmienić (wartości mogą być różne)
kroteczka = ( 'v',5,'string' )
print(kroteczka[0],kroteczka[1],type(kroteczka), type(kroteczka[2]))
    # kroteczka[0] = 6  # takie przypisanie to byłby błąd
tuple1 = tuple(range(0,100,5)) # range(generuje zbiór od 0 do 99 włącznie, krok co 5)
print(tuple1,type(tuple1))

    # lista czyli zbiór możliwy do zmiany (taka krotka, tylko można zmieniać)
lista = [ '1',2,'A' ]
print(lista[0])
lista[0]='koniowół'
print(lista[0])
print('lista:',lista, type(lista))

lista2 = [ ]  # pusta lista
lista2.append(123)  # dodaj do listy
lista2.append(1)
lista2.append(10)
print(lista2)
print(max(lista2), min(lista2))
print('1:2',lista2[1:3]) # od 1 do 3 (bez 3)
lista2.insert(0,100)
lista2.reverse()
print('reverse',lista2)
lista2.pop() # zabierz z końca
print('pop',lista2)
del lista2[0]
print('del',lista2)

lista2.clear() # ciekawe, co się stanie?
print(lista2,' : lista2')

# lista2[0] = 1 #  - błąd !

lista2.insert(0,20)
print( len(lista2) ) # ile elementów
lista3 = list(range(1,100))
lista4 = lista3[1:25:3] + lista2 # złączenie list
print(lista4)
print(lista4.count(20)) # wartość 20 w lista4 wystąpiło 2 razy
lista5 = [ 5 ] * 10
print(lista5) 

lista6 = [ [ 5 ] ] * 5
print(lista6) 







