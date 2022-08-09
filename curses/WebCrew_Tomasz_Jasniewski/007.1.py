# yield czyli YIELD czyli bardzo ciekawy sposób na opuszczanie funkcji :)
# yield w funkcjiach wychodzi z funkcji jak return, ale ponowne wywołanie funkcji
# kontunuuje jej działa za ostatnim yield'em ! Punkt dla pythona !
# yield nie jest rekurencją! yield nie jest zmienną statyczną pamiętaną pomiędzy wowołaniami!
def yieldPresentation(a) :        
        yield a
        a+=1 # argument a przy kolejnym uruchomieniu funkcji zachowa zmienioną wartość
        yield a
        a+=a
        yield a
        a*=a
        yield a

# klasyczna rekurencja (przykład na samym dole) to wywołanie funkcji przez samą siebie (w skrócie)
# konstrukcja z yield to nie jest mechanika rekurencji: funkcja nie wywołuje się,
# nie ma warunku stopu rekurencji - po prostu wykonuje się od pierwszego do ostatniego
# yield, gdzie każdy yield zwraca coś, co utworzy w przyszłości zbiór

for i in yieldPresentation(5) :
        print(i, end='\t');

print('\n\n', list(yieldPresentation(5))) 


v1= yieldPresentation(5) # v1 to nie jest pierwszy zwrócony yield !!
print (v1) # v1 to specjalny obiekt, który reprezentuje to, co zwracają wszystkie yield'y !
v2 = yieldPresentation(5) # v2 to nie jest drugie yield, to jest dokładnie to, co v1
print (v2) # zatem v2 jest już obiektem przechowującym wszystkie yield'y dla tej funkcji

# funkcja next() pozwala pobrać kolejne rozwiązania
print(next(v1), next(v1), next(v1), next(v1))
print(next(v2), next(v2), next(v2), next(v2))

# kiedy rzutujemy nasz obiekt (tzw. generator) na listę, wszystkie zwrócone yield'y utworzą listę
v3 = yieldPresentation(2)
print(list(v3))

# nic nie stoi na przeszkodzie rzutować trochę inaczej ...
v4 = yieldPresentation(3)
print(tuple(v4))

# ZATEM wywołanie funkcji z yield nie zwraca pierwszego wyniku,
# ale zostaje uruchomiona niewidoczna iteracja, tak długo, aż odpalą się wszystkie yield'y
# a zwracany wynik to specjalny zbiorowy obiekt, GENERATOR, z którego to można
# utworzyć np. listę lub krotkę (elementy muszą być indeksowane od 0, dlatego lista/krotka)

# a co, gdy pobiorę za dużo ?
try:
        print(next(v1))  # zostanie zwrócony wyjątek StopIteration - z obiektu v1 nie da się już nic pobrać
except:
        pass



# przykład wykorzystania yield (mniej eleganckie niż rekurencyjny fibonacci, ale szybsze
def fibo(n) :
        print('START fibo')
        a1 = 0
        a2 = 1
        yield a1 # 0
        yield a2 # 1
        if n<1 or isinstance(n,float) : n = int(1)
        while n>a1+a2:
                suma = a1+a2
                yield suma # suma wcześniejszych dwóch
                # przesuwam się na dwa ostatnie, tak by a1, i a2 były ostatnimi elementami
                a1 = a2 
                a2 = suma 

print(list(fibo(999999999999)))

'''
def f(a):
        if a>0:
                print(a)
                f(a-1)
f(10)
'''


