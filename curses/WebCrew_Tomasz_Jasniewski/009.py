# PLIKI
# https://docs.python.org/3/library/os.html
# https://docs.python.org/3/library/os.path.html
# operacje na typie str:  https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

# referencja_do_obiektu_plikowego = open(ścieżka,'w')  # - zapis

fd = open('dane.txt','w',encoding="utf-8") # otwieram do zapisu (czyszczę przy otwarciu)
fd.write('Pierwsza linia tekstu w pliku śćźńąłó.\n')
fd.write('Druga linia tekstu w pliku.\n')
fd.write('Trzecia linia tekstu w pliku.\n')
fd.close() # zamykam plik


import os # operacje na plikach/katalogach itp.

def myReadFile(path) :
  ''' czyta i pokazuje zawartość pliku '''
  # test na obecność pliku
  if os.path.isfile(path) :    
    fdread = open(path,'r',encoding="utf-8") # otwieram do odczytu, skoro jet
    #  używam lambdy i map by oczyścić linie ze znaków białych .strip() z początku i końca tekstu
    lines = list(map(lambda line : line.strip() , fdread)) # :-D a mówią, że Python PROSTY
    # ta linia wyżej jest zbliżona logiką do kodu niżej
    #!    lines=[]
    #!    for line in fdread :
    #!        lines.append(line.strip())  
    print(*lines,sep='@') # a tu tylko rozpakowałem lines i wyświetliłem oddzielone znakiem @
    fdread.close()
  else:
      print('Plik ',path,' nie istnieje!')

myReadFile('dane.txt')    

# wszystko czytam na raz do jednej zmiennej tekstowej
if os.path.isfile('dane.txt') :
  fdread = open('dane.txt','r',encoding="utf-8") 
  fdtotal = fdread.read() # czytanie całego pliku na raz
  print(fdtotal) # pokaż to wszystko na raz
  fdread.seek(0) # zamiast ponownie zamykać i otwierać plik po przeczytaniu ...
  lines=fdread.readlines() # czytam wszystko do listy linii
  print(lines)
  fdread.close()

# Informacja. Sposobów i technik odczytu pliku/danych jest znacznie więcej! 

# Teoria: powinniśmy zamykać plik kiedy z niego skorzystaliśmy. Może to się jednak nie udać
# gdy wyskoczy wyjątek. Dlatego powinno się korzystać z ..
'''KONSTRUKCJA with - specjalny protokół pobierania i zwalniania zasobów.
      with wyrażenie as nazwa :
        grupa instrukcji
  W przypadku plików with otwiera zasób plikowy i pilnuje by uruchomiono
  protokoły "zwalaniania zasobu" co w przypadku pliku oznacza jego zamknięcie,
  nawet, jeżeli programista wprost o to nie zadba. Oto przykład wykorzystania with
  do otwierania plików:
'''
try:
  L = ['A','B','\nC']
  with open('dane.txt','a',encoding="utf-8") as fd:   # fd - zasób plikowy otwarty przez with
    for elem in L:
      # błąd - nie ma fs. ale ponieważ plik otworzono z with, zadba ono by plik został zamknięty
      fd.write(elem)  
except:
  print('Zanim przekazano tu wyjątek, kontrukcja with wymusiła operacje zamknięcia zasobu.')
  #fd.read()
  

# ZADANIE : tak przerób myReadFile aby wykorzystywał kontruktor with !!!
myReadFile('dane.txt')    

# A NA KONIEC zabawy z plikami - ciakwy mechanizm PIKLOWANIA z wykorzystaniem
# plików. Piklowanie to sprytne pakowanie obiektów do pliku !!

import pickle # tak, pickle importujemy

lista = [10,20,'trzydzieści',[1,2,'trzy']]
with open('plik.pickle','wb')  as outPut : # 'wb' - zapis binarny !
  pickle.dump(lista,outPut) # wgranie do pliku listy ;) MEGA! Może to być dowolny obiekt!
  outPut.close()
	
with open('plik.pickle','rb') as inPut:
  unpickle = pickle.load(inPut)
print(unpickle,type(unpickle))

# PROBLEM: jeżeli zmieniliśmy obiekt (klasę) to wczytanie może się nie udać :
# chodzi o sytuację, gdy zapisany obiekt klasy i obecna klasa (pola,metody) różnią się 

