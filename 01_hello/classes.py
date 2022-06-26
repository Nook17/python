#!/usr/bin/env python3

class Car:
    ''' first classes '''
    def __init__(self, moc, zasilanie):
        self.moc = moc
        self.zasilanie = zasilanie

    def disp(self):
        print('Astra')

a = Car(123, 'petrol')
b = Car(150, 'disel')

a.disp()

print(a.moc, a.zasilanie)
print(b.moc, b.zasilanie)

print(a.__dict__)
print(b.__dict__)
print(Car.__doc__)