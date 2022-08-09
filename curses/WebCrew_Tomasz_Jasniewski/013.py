# Funkcje tekstowe i operacje z nimi związane

findIndex = 'to jest tekst o tosterze'.find('to')
print(findIndex) # 0 (znalezione pod numerem literki 0)

print('to jest tekst o tosterze totalnym'.find('to',findIndex+1)) # 16 (szuka za pozycją)
print('to jest tekst o tosterze'.find('to',1,15)) # -1 w wyniku to brak (szuka pomiędzy)
# .index działa jak find, ale zwraca wyjątek gdy nie znajdzie
# print('to jest tekst o tosterze'.index('to',1,15)) # -1 w wyniku to brak
print('to jest tekst o tosterze'.rfind('to')) # 16 (od końca)
# .rindex jak rfind z zachowanie reguły zgłaszania wyjątku

print('RABARBAR jest fajny'.capitalize())
print('śLIMAKOŃ'.capitalize())
print('pa1pa2pa3pa4pa5rapet papy'.count('pa')) # pa wystąpiło 6 razy
print('pa1pa2pa3pa4pa5rapet papy'.count('pa',3,10)) # pa w zakresie wystąpiło 2 razy

# różne testy czegoś, a to czy tekst to liczba jakiegoś typu, albo czy nie.
# czy coś jest rozpoznawalnym słowem kluczowym języka python czy nie (isidentifier)
print('aA'.isalpha(), '1.5'.isdecimal(), '1'.isdigit(), '1a'.isnumeric(), 'def'.isidentifier(), '  \t'.isspace(),\
      'low'.islower(), 'UP'.isupper(), 'Title Is Fine'.istitle())


teksty = ['a','b','c',"dramat"]
print(' ... '.join(teksty)) # łączy teksty ciągiem ' ... '

print('TRAKTOR'.center(50,'='))
print('TRAKTOR'.ljust(50,'*'))
print('TRAKTOR'.rjust(50,'*'))

print('abcdecfg'.partition('c')) # dzieli na 3 części przed 'c', samo 'c', po 'c' ;)
#rpartition - odwrotny porządek
print('krowa krowie nie równa'.replace('kro','mo'))

print('1,2,3,4,5'.split(',')) # lista po podziale tekstu
print('1,2,3,4,5'.split(',',2)) # lista po podziale tekstu (ograniczona ilością podziałów)
print('   1   2  A       B'.split()) # bez argumentów stosuje pewien algorytm podziału
print('1\n2\t\n3\n\n4'.splitlines())
print('1\n2\t\n3\n\n4'.splitlines(True))

print("-51".zfill(30)) # zero-fill

# translate
print('pacynka'.translate( {97:121, 107:65} )) # a->y, k->A


vars=[1,2,3,'a','b','c']
print('tekst formatowany: {} {}'.format(5,vars[0]))
print('tekst formatowany: {1} {2} {0} {1}'.format(vars[0],vars[1],vars[5]))
print('{a} {c} {b}'.format(a=1, b=2, c=3))
print('{a[0]} {a[1]}'.format(a=[1,2]))

print('{:<30}'.format('napis'))
print('{:>30}'.format('napis'))
print('{:^30}'.format('napis'))
print('{:_^30}'.format('napis'))

print('{:+} {:+f}'.format(2.5, -2.5))
print('{:>f} {:>f}'.format(2.5, -2.5))

print('{0:d} {0:x} {0:o} {0:b}'.format(99)) # 99 w 4 systemach pozycyjnych liczbowych
print('{0:#d} {0:#x} {0:#o} {0:#b}'.format(99)) # 99 w 4 systemach pozycyjnych liczbowych
print('{0:08X}'.format(2557)) # duże

print('{:,}'.format(5555555555)) # separator tysięcy
print('{:.3}'.format(1.2345)) # ile liczb po przecinku
print('{:.5%}'.format(44.671/100)) # ile liczb po przecinku jako %
print('{:.0%}'.format(44/100)) # ile liczb po przecinku jako %

from datetime import datetime
print('{:%Y-%m-%d %H:%M:%S}'.format(datetime(2020, 5, 1, 20, 30, 45)))

for x,y in zip('^><',['_','+','#']):  
  print('{0:{y}{x}30}'.format( 'TEKST', x=x, y=y ))



# https://docs.python.org/3/library/string.html  - tu znajdziecie znacznie więcej  !
import string
# stałe
print (string.digits, string.hexdigits)
# ascii_letters, ascii_lowercase, ascii_uppercase, printable, whitespace itp.

# Template
from string import Template
s = Template('$a to nie $b')
print(s.substitute(a='siano', b='kapusta'))

d=dict(a='szynka', b='kalafior')
print(Template('$a to nie $b').substitute(d))

d=dict(a='szynka', c='kalafior')
print(Template('$a to nie $b $c $d').safe_substitute(d)) # gdy nie ma $b - wyświetli $b ;)


