globalna = 100

def f1():
	print('jestem f1')

def f2():
		print('jestem f2')

__all__ = ["globalna","f1"]  # gdy będzie from klasy import * - zostaną zaimportowane tylko te rzeczy na liście !


print('Zładowano pakiet klasy.  ')
