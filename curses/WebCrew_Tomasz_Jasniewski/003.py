#    UWAGA! https://docs.python.org/3/library - spis bibliotek

# BIBLIOTEKI, czyli import gotowych rozwiązań
   # import biblioteka
   # import biblioteka as skrót
   # from biblioteka import funkcja
   # from biblioteka import *
   
import random   # zgłaszam import całej biblioteki z generatorem losowości
# biblioteka.funkcja()  - konkretne wykorzystanie jakiejś funkcji z importowanej biblioteki
print('Losowo od 1 do 10 = ',random.randint(1,10))  

# mogę zamiast przedrostka math.funkcja używać m.funkcja
# ostrożnie, skrót nie powinien być mylący czy głupi
import math as m
print('m.floor(10.6)=',m.floor(10.6)) # floor - część całkowita

0xff # liczba szesnastkowa :) 255
0o14 # liczba ósemkowa :) 
0b1000 # liczba binarna :) 8
x = 31 # dzisiętne 100
print('31=', hex(x),oct(x),bin(x)) # liczba 31 w 3 systemach

    # mogę importować jedną funkcję z biblioteki
# random to też funkcja w bibliotece o tej samej nazwie, a tu ją importuję
from random import random
# teraz mogę korzystać z funkcji random bez prefixu |random.|
print(random(), ' los czegoś ułamkowego od 0 do 1')  

    # jeżeli użyję składni ...
from random import *
# ... będę mógł używać wszystkiego bez prefixu |random.|

# INPUT (pobieranie z klawiatury)
print(" * INPUT i sys")
import sys
    # sep - separator, file=wyjście (ekran/plik)
print('Jaś','Małgosia',sep='| i |', end='\n'+'-'*50+'\n', file=sys.stdout) 
    # pobieranie z klawiatury:         input([opcjonalny tekst wprowadzający])  
name = input('Podaj proszę imię i nazwisko osoby, która ma  nie zdać: ')
print(name)



# CZAS to piniondz jest
print(" * CZAS")
import time
curtime = time.localtime()
print('Time\t\t', curtime.tm_hour, curtime.tm_min, curtime.tm_sec, sep=':')
'''kolejne atrybuty z klasy
tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday
'''
print("Idę spać...")
time.sleep(2) # śpij mi tu X sekund
print('No to się wyspałem...')
