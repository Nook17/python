# WYJĄTKI, czyli co robić, gdy coś poszło nie tak a python zwraca 'wyjątkowy' błąd
# https://docs.python.org/3/library/exceptions.html
# zgłoszenie wyjątku to znaczy w praktyce przerwanie programu i zgłoszenie komunikatu
# chyba, że przechwycimy taki wyjątek i obsłużymy, czyli zaprogramujemy inne zachowanie

# próba zmiany tekstu na int musi zakończyć się zgłoszeniem wyjątku ValueError:
# fine_number = int('tekst ten nijak nie przypomina liczby typu int') 

# try rozpoczyna wykonywanie kodu który chcemy obsłużyć na wypadek wyjątku/ów
# gdy wystąpi wyjątek - po jego obsłużeniu program 'idzie dalej', podczas gdy
# bez tego zatrzyma się zgłaszając wyjątek
try:
  #fine_number = int('tekst ten nijak nie przypomina liczby typu int') # próba zmiany na int
  #fine_number = int(['tekst ten nijak nie przypomina liczby typu int']) # próba zmiany na int
  fine_number = int('5') # próba zmiany na int
except ValueError: # ValueError to wyjątek błędnej wartości - tu się zadzieje
  print('Wprowadzony tekst nie jest liczbą. Ustawiam wartość domyślną = 0.')
  fine_number = 0
except TypeError: # gdy oczekiwano innego typu
  print('Argument dla rzutowania int() powinien być napisem')
  fine_number = 0
finally :
  print('ta sekcja wykona się zawsze')
  fine_number += 1

print(fine_number)

'''
try:
  pobieranie = input('Przerwij wprowadzanie wartości CTRL+C :    ')  
except KeyboardInterrupt : # wyjątek Ctrl+C
  pobieranie = 'Gandalf: You Shall not Pass !!'

print(pobieranie)
'''
try:
  5/0
except :
  print('po prostu błąd - nie interesuje mnie jaki')

# wyjątki mogę zgłaszać samodzielnie, czyli samemu je wywołać
# funkcja dziel zwróci wyjątek (raise) gdy będzie miała podzielić przez 0
# (problem jest sztuczny, ale chodzi o mechanizm zgłaszania wyjątku)

def dziel(a,b) :
  if b == 0 :
    raise Exception('Uwaga! Drugi argument dzielenia nie może być zerem.')
    print(1)  # ta linia nigdy nie zostanie wykonana, wyjątek próbuje przerwać program...
    #... ale blok try (niżej) przechwyci ten wyjątek i nie przerwie programu.
  else:
    return a/b

#dziel(5,0) # bez bloku try takie dzielenie zgłosi wyjątek a ten przerwie program

try :
  wartość = dziel(5,0)
  print(wartość) # jeżeli wystąpił wyjątek - wartość nie zostanie wyświetlona
except Exception as e:
  print(e)
  
