# od znaku # do końca linii rozpoczyna się komentarz

# LITERAŁY
# każdy LITERAŁ ma jakiś typ. Podstawowe typy to: int, float, str, bool
# WSZYSTKO w Python to OBIEKT jakiejś klasy. Zatem typy podstawowe to też klasy
print(" * LITERAŁY")
2 # int
-3.5 # float
'tekst' # str
"tekst" # str
# Uwaga! Wpisz w konsolę
# import sys     a następnie np. sys.int_info lub sys.float_info
# by otrzymać informację o zakresie itp.

# W Pythonie przyjęto zasadę iż w jednej linii jest jedna instrukcja, dlatego nie musimy
# kończyć instrukcji znakami końca, jak np. średnikiem w PHP
# linia:  print(1)  print(2)   byłaby zatem rozpoznana jako błędna (dwie instrukcje w linii)
# ALE dla miłośników wielu instrukcji w jednej linii można je oddzielić średnikiem ;)
print(1)
print(2)


   # ponieważ wszystko jest obiektem, mogę wywołać metody
   # klasy na obiekcie, gdyż LITERAŁY to też obiekty, reprezentanci swojej klasy
   # przykładowo na tekście mogę uruchomić metody upper() i lower()
print('Śliweczki Parszywki'.lower())   
print('WEBJASIEK Tomasz Jaśniewski'.upper())


# WYŚWIETLANIE / print(...)
print(" * PRINT")
print(2, -3.5, 'tekst1', "tekst2")
print('-*-' * 10) # 10 razy napis '-*-'
print(2+2.5, 'tekst1' + 'tekst2')
   # działania podobne do C/C++ itp. dodatkowo jest operacja ** czy //
   # (// to cz. całkowita z dzielenia oraz ** to potęgowanie)
print(5/2, 2**4, 5%2, 5//2)
print('''
Pierwsze zdanie wieloliniowego tekstu.
Linie wyświetlają \t\tsię ...
      ... z zachowaniem formatu tekstu.
... ''')




# ZMIENNE   
print(" * ZMIENNE")
x = 0
y = 10
x = x*y + 5
nazwaSugerujeZnaczenie = 'Nie zapominaj by nazywać zmienne sugestywnie'
print (x,y,nazwaSugerujeZnaczenie)
   # ZMIENNE to referencje do obiektów.
   # https://en.wikipedia.org/wiki/Reference_(computer_science)
a=30
b=30
c=a
print ("a, b i co to", a, b, c)
c=100
print ("a, b i c to", a, b, c)		
    # typy bool, float, int, string są NIEMUTOWALNE
    # (obiekty klasy niemutowalnej nie mogą być modyfikowane, zawsze tworzone są nowe, 
    # zatem przypisanie do c wartości 100 tworzy nowy obiekt 100 klasy int)
   
	 
	# PRAWDA i FAŁSZ   
x=True    
y=False
   # Zmienne x i y były już używane i mają swój typ! W C++ nie możnaby było tak zrobić.
   # x i y przyjmują nową wartość i nowy typ bez problemu
z= 'ABC' < 'DEF'  # logiczna prawda
print (x, y, z)
# KONWERSJE do typów podstawowych
liczba = int("18") + 12
liczba_zm_prz = float('12.567')
czy = bool(17-15)
val = str(10)
print(liczba,liczba_zm_prz,czy,val)
# type() - pokazuje, co to za klasa
print(type(liczba), type(liczba_zm_prz), type(czy), type(val), sep='\n') 




