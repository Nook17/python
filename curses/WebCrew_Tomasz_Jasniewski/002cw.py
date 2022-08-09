#  ĆWICZENIA 002 (po lekcji 9)

# 1
# Pobieraj od użytkownika listę słów tak długo, aż wprowadzi on słowo : 'end'
# Słowa mogą być wprowadzane pojedyńczo lub poprzez wpisanie wielu słów po spacji.
# Pobrane słowa zapisz do pliku words.pickle za pomocą 'piklowania' (lekcja 9)
# Napisz funkcję, która 'ładuje' te słowa z pliku i czyni z nich posortowaną listę słów.

# 2
# Napisz program, który pobiera od użytkownika 3 punkty na płaszczyźnie
# (2 liczby X i Y typu float jako jeden punkt )
# Sprawdzaj, czy liczby są poprawne (obsłuż wyjątki na wypadek nieudanej konwersji) i pobieraj
# je tak długo, aż zostaną podane prawidłowe dane (prawidłowe liczby)
# Stwórz funkcję, która sprawdza pobrane punkty pod kątem występowania na jednej prostej.
# (zwraca True lub False)

# 3
# Pobieraj od użytkownika linię tekstu tak długo, aż wprowadzi słowo 'end'
# po pobraniu zdania/linii dodaj do słownika parę:
# znacznik-czasu : podana w kolejnym kroku pętli treść linii tekstu
# stwórz mechanizm wyświetlania tylko tych danych ze słownika, których wartość
# zawiera słowo 'python' bez względu na wielkość liter

# 4*  Niezależnie, czy zrobiłeś zadanie samodzielnie czy na podstawie propozycji poniżej
# spróbuj je zoptymalizować, skrócić, skondensować... Być może użyjesz
# wyrażenia warunkowego zamiast instrukcji warunkowej, może poprawisz algorytm
# a może poszukasz w necie funkcji (z biblioteki wspomagającej obsługę napisów)
# przyśpieszających działania na danych ?
# Popracuj samodzielnie. Stawiaj sobie cel i próbuj go osiągnąć. Nawet odkrycie, że to za trudne
# jest formą edukacji. Obniż wtedy poziom celu i próbuj ponownie. Nie poddawaj się nigdy!
# A jak nie dajesz rady samodzielnie, weź kolegę/koleżankę i poucz się razem.


# rozwiązanie 1
'''
L = []
while True:
  string = input('?: ').strip()
  if len(string)==0 : print('sam Enter? Wpisz coś!'); continue  
  if string == 'end' : break
  if (' ' in string) :
    # ponieważ nie znamy jeszcze fajnych funkcji tekstowych, a wiemy tylko, że napis to lista
    # znaków, spróbujemy to wykorzystać
    # w jednej z przyszłych lekcji poznamy sporo funkcji związanych z napisami, spróbuj
    # potem zrobić to zadanie raz jeszcze ;)
    letters = list(string) # napis rzutowany na listę znaków
    word = ''
    for letter in letters :      
      if letter!=' ' :
        word = word + letter
      else :
        L.append(word)
        word=''
        
    if len(word) : L.append(word)
  else :
    L.append(string)
print(L)

import pickle
with open('words.pickle','wb') as fd :
  pickle.dump(L,fd)

def loadList() :
  with open('words.pickle','rb') as fd :
    return sorted(pickle.load(fd))

print(loadList())
'''


'''
# rozwiązanie 2
points3 = [{},{},{}]
print(points3, type(points3))
for p in range(0,len(points3)) :    
    for xy in ['x','y'] :
        while True:
            try:
                info = 'Podaj liczbę: punkt {}, współrzędna {}   :'
                s = input(info.format(p,xy))
                f = float(s)
                points3[p][xy] = f
                break;
            except:
                print('Wprowadź właściwy format liczby')        

print(points3)

def onTheSameLine(p) :
    # Z dwóch różnych punktów mam prostą, sprawdzam, czy trzeci na niej leży (czy spełnia
    # wzór funkcji liniowej)    
    if p[0]==p[1] or p[0]==p[2] or p[1]==p[2] : return True    
    return (p[2]['y'] - p[0]['y'])*(p[1]['x']-p[0]['x']) - (p[1]['y']-p[0]['y'])*(p[2]['x']-p[0]['x']) == 0
    

print(onTheSameLine(points3))
'''

'''
# rozwiązanie 3
import time
D = dict()
while True:
    s = input('Wpisz zdanie: ')
    if s == 'end' : break
    D[time.time()] = s
    time.sleep(0.2)
    
for k,v in D.items() :
    print('key=', k , 'value=', v)

keys = list(filter(lambda k : 'python' in D.get(k).lower(), D))
newD = dict()
for k in keys :
    newD[k] = D[k]
print(newD)
'''


# PRZY OKAZJI, może się przyda konstrukcja generująca (taki miks FOR i IF)
a=[1,2,3]
b=[1,3,5,7,10]
g = list(x for x in b if x not in a)  # generuje listę jakby kolejnyc x'ów (wewnętrzna pętla for)
print(g)

# a tu przefiltrowanie przykładowego słownika z zadania # 3
D = { 1:'python', 2:'mam Pythona', 3:'śmietanka z mięsem i cebulą na czereśniach'}
g = ((k,v) for k,v in D.items() if 'python' in v.lower())
print(dict(g))

    

