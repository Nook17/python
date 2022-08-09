# FUNKCJE !!
#       def funkcja(argumenty) :
#               '''dokumentacja'''
#               kod

# nie ma argumentów, nic nie zwraca, nic nie robi - a jest funkcją :)
def nic( ):
        pass


nic()
nic()

        # wartości domyślne dla argumentu/ów
def ileCzego(arg1, arg2='default') :
        arg1 = int(arg1)        
        print((' '+arg2) * arg1)
        nic()

ileCzego(3)
ileCzego(12.8,'*-')

#       zmienna = funkcja  (nazwa funkcji)
#       zmienna()  - możliwe wywołanie, coś jak alias do funkcji
f = ileCzego
f(5,'-')

# eval
v='ileCzego'
x=10
tpl='#'
print(v+'('+str(x)+",tpl)")
# eval traktuje napis jak instrukcję pythona i tak ją wywołuje/wykonuje
eval(v+'('+str(x)+",tpl)")  # fragment tpl zostaje zamieniony na wartość zmiennej tpl !
# uwaga! eval to niebezpieczna instrukcja !!
#polecenie = input('Podaj polecenie:   ')
#eval(str(polecenie))

        # return
def multi(arg1) :
        return arg1 * 5        

        # sam return zwraca NONE (wartość pusta, nic)
print(multi(2) * multi(3)) # (2*5) * (3*5)= 10 * 15 = 150


# globalna zmienna w funkcji
var = 1
var3 = 10
def changeGlobal() :
        var2 = 100 # żyje lokalnie, nie istnieje poza funkcją
        global var # var to jest te var globalne
        var = 2
        var3 = 2 # var3 też jest lokalne - żyje tylko w funkcji 

changeGlobal()
print('var=',var,'var3=',var3)


# komentarz
def funkcja() :
        '''
        opis funkcji, pojawi się w podpowiedziach co bardziej sensownych IDE
        '''
        pass # instrukcja wypełniacz, pusta, nic nie robi

# zwracanie zbiorów (list, krotek itp.)
def collectionReturn() :
        return (1,2,'3')        

a,b,c = collectionReturn() # wywołanie można tak przypisać ;)
print(a,b,c,type(c))

def collectionReturn() :        # przy okazji redefinicja funkcji (w innych ograniczenia)
        return {'a':1,'b':20,'c':300}
print(collectionReturn()['c']) # ha!

		
# funkcja o dowolnej liczbie argumentów ? proszę !
def multiArgs(*args) :
        suma = 0
        for arg in args :       # arg to wszystkie argumenty, które podano - jeden po drugim
                print(arg)
                if (isinstance(arg,int) or isinstance(arg,float)):  suma += arg;
        return suma

print('multiArgs(1,2,3)=',multiArgs(1,2,3))

nums = (1,2,3,4,5,0.5,'rabarbar') # kroteczka, posłuży jako kolejne argumenty
s = multiArgs(*nums)  # *nums - jakby rozpakowanie krotki, zbioru
print ('suma=',s)

# LAMBDA, czyli funkcje anonimowe (nie posiadają nazwy, ale mogą mieć referencję)
# nazwa = lambda argumenty : wyrażenie do obliczenia
f = lambda arg : arg+1  # f staje się referencją do funkcji, która zwiększa argument o jeden
print('lambda f(5)=',f(5))

g = lambda x,y,z : (x+y)*z  # lambda może mieć wiele argumentów
print('g(1,2,3)',g(1,2,3)) # 9

# lambda może być łączona np. z wyrażeniem warunkowym
h = lambda arg1 : 'jestem dodatnia' if arg1>0 else 'nie jestem dodatnia'
print(h(5),h(-5), sep=' | ')
		

# lambdy są częstym argumentem dla takich sprytnych funkcji jak map
# funkcja map uruchamia podaną funkcję dla każdego elementu zbioru
        # map (funkcja, zbiór) - każdy element zbioru odpalony zostanie przetworzony prze f-ę
# tu jako funkcję podałem właśnie lambdę.
L = [1,2,3,4] # lista-zbiór
newL = map(lambda x: x+1, L)  # newL to zwrócony przez map specjalny iterator ...
# i ten iterator trzeba rzutować na np. listę lub inny zbiór/kolekcję
print (list(newL))  # 2,3,4,5
# samo newL to specjalny obiekt zwracany przez map, to nie jest jeszcze kolekcja
print(newL)

# podobnie lambdy poddane są jako argument dla funkcji filter. Ta z kolei wybiera
# część elementów ze zbioru
L = list(range(1,11))
newL = filter(lambda x: x%2==0, L)
print(list(newL)) # będą tylko parzyste :)

# i ponownie lambda jako przydatna do funkcji reduce, która podaną ilość elementów
# zastępuje jednym wg podanej mechaniki. Nowy element jest parowany z następnymi
# aż do uzyskania jednego elementu
from functools import reduce
suma = reduce( lambda x,y : x+y, L) 
print(suma) # suma wszystkich z L

# yield czyli YIELD czyli bardzo ciekawy sposób na opuszczanie funkcji :)
# yield w funkcjiach wychodzi z funkcji jak return, ale ponowne wywołanie funkcji
# kontunuuje jej działa za ostatnim yield'em ! Punkt dla pythona !
# yield nie jest rekurencją! yield nie jest zmienną statyczną pamiętaną pomiędzy wowołaniami!
def yieldPresentation() :
        print('przed a')
        yield 'a'
        
        print('przed 1')
        yield 1

        print('przed 2.5')
        yield 2.5

        print('przed krotką 1,2,3')
        yield (1,2,3)

for i in yieldPresentation() :
        if (isinstance(i,tuple)) :
                for temp in i :
                        print('\t',temp)
                print( '\t: ilość elementów=',len(i))
        else : print(i);

# taki kontekst wymusza użycie funkcji aż zwróci wszystkie swoje yield'y - wynik wkładam do listy
print(list(yieldPresentation())) 







