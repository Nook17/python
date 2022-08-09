#  ĆWICZENIA 001

# 1. Wyświetl parzyste elementy zbioru <1;100>
  # 1.a Stwórz funkcję do tego zadania pobierającą zakres <a;b> jako argumenty.

for parzysta in range(2,101,2) :
  print(parzysta, end=' ')
print("\n","*"*50)

def parzysteZeZbioru(a,b):
  ''' dla zakresu a,b wyłączając b wyświetla liczby parzyste '''
  for parzysta in range(a+1 if a%2 else a,b+1,2) :
    print(parzysta, end=' ')
  print("\n","*"*50)

parzysteZeZbioru(45,101)
parzysteZeZbioru(2,32)
  
  
# 2. Wyświetl 30 elementów ciągu Fibonacciego (iteracyjnie i rekurencyjnie)
  #2.a Wykorzystując bibliotekę time wykaż, że iteracja działa szybciej.
  # ( na własną rękę zerknij na bibliotekę time, zwróć uwagę np. na funkcję time() )

import time
c1 = time.time()
Z = [1,1] #
for i in range(1,29) :  # 1-28 bo 2 pierwsze elementy już są :)
  Z.append(Z[len(Z)-1]+Z[len(Z)-2])
print(Z)

c2 = time.time()
print ('\nCzas wykonania iteracyjnego:',c2-c1)

def Fibonacci(n) :
  return Fibonacci(n-1)+Fibonacci(n-2) if n > 2 else 1

for i in range(1,31):
  print(Fibonacci(i),end=' ')

c3 = time.time()
print ('\nCzas wykonania rekurencyjnego:',c3-c2)

# 3. Narysuj 'kwadrat' zbudowany z losowej małej literki (n znaków w n wierszach) dla
# losowego n>4. Kwadrat ma być w wersji wypełnionej i pustej (tylko krawędzie)

import random
n = random.randint(5,10) # 5-10
print('n=',n)

''' pierwszy sposób na literkę '''
kod = random.randint(97,97+25)  # kod małej literki (angielskiej)
literka = chr(kod)
# print (literka,'=',kod)

''' drugi sposób na literkę '''
literki = list('qazwsxedcrfvtgbyhnujmikolpłśćąźó')
literka = literki[random.randint(0,len(literki)-1)]
print(literka)

''' kwadrat wypełniony '''
for i in range(1,n+1) :
  print(literka * n)
print('*' * 50)

''' kwadrat pusty '''
for i in range(1,n+1) :
  print( literka , literka * (n-2) if i in (1,n) else " " * (n-2) , literka, sep='')

# 4. Stwórz funkcję, która otrzymuje słownik i zwraca jego część złożoną tylko z tych
# par klucz-wartość, w których klucz nie jest liczbą
# słownik - dowolny zbiór z minimum 3 elementami

S = {'klucz1' : 100, 'klucz2' : 200, 1 : 'słoń', 5 : 'kasza', 'klucz3' : 300}

# przy okazji wyjaśniam metodę .items() dla słownika
# S.items() zamienia słownik specjalną klasę dict_items, którą można porównać
# do listy z krotkami (klucz,wartość), gdzie każda krotka odpowiada parze ze słownika
print(S)
print (S.items(),type(S.items()))
# a tak można tę metodę .items() wykorzystać
for k,v in S.items() :
   print(k,':',v)
      

def keyFiltr(s) :
   ''' Zwraca False gdy argument nie jest słownikiem.
   W przeciwnym wypadku wykonuję operację odrzucenia elementów,
   których klucz jest liczbą i zwracam nowy słownik '''
   if not isinstance(s,dict) : return False
   goodKeys = filter(lambda e : not(isinstance(e,int)  or isinstance(e,float)), s)
   print(goodKeys)  # specjalny obiekt filter, iteracja do zbioru 
   newS = dict()
   for goodKey in list(goodKeys):  # korzystam z goodKeys w kontekście listy
      newS[goodKey]=s[goodKey]
   return newS

print('Słownik bez złych kluczy',keyFiltr(S))


# 5. Stwórz funkcję, która w przekazanej liście szuka liczb pierwszych i zwraca listę
# z tymi liczbami pierwszymi
# 5.a Jeżeli elementem listy są inne listy/krotki/słowniki - spróbuj i w nich odszukać
# inne liczby pierwsze !!! Wyświetl znalezione liczby pierwsze jako ZBIÓR (set)

from math import sqrt
def isPrime(x):   
   if not isinstance(x,int) or x<=0 : return False
   for i in range(2,int(sqrt(x))+1) :
      if not x%i : return False
   return True

def f5(L):
   newL = []
   for x in L:
      if isPrime(x) :
         newL.append(x)
   return newL

L = [1,5,7,9,14,'kaszanka',[5,'wiadro'],(123,11,0.9,5.5,[17,23]),{19:43,'a':3,'ślimak':17,2:2}, 13, 29]

print('Lista z liczbami pierwszymi f5',f5(L))

def f5a(L) :
   newL = []
   for x in L:
      if (isinstance(x,tuple)):
         newL += f5a(list(x))
      elif (isinstance(x,list)):
         newL += f5a(x)
      elif (isinstance(x,dict)):
         newL += f5a(x.items())
      elif isPrime(x) :
         newL.append(x)
   return newL

print('Lista z liczbami pierwszymi f5a',f5a(L))
print('Zbiór z liczbami pierwszymi f5a',set(f5a(L)))
