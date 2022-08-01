#!/usr/bin/env python3
import random


def main():
    portfel = 5000
    while True:
        zagranie = bet(portfel)
        lot = lottery()
        chooses = choose()
        if check(lot, chooses):
            portfel += int(zagranie)
            print('Zgadłeś !!! w potfelu posiadasz {}'.format(portfel))
        else:
            portfel -= int(zagranie)
            print('Niestety nie udało się wylosowana liczna to {}'.format(lot))


def bet(portfel):
    while True:
        print('Za ile kasy grasz ? Obecnie posiadasz {}'.format(portfel))
        kasa = input('> ')
        if kasa.isdecimal() and 0 < int(kasa) <= portfel:
            return kasa
        else:
            print('Zła kwota')


def lottery():
    lot = random.randrange(1, 12)
    return lot


def choose():
    while True:
        print('Obstaw czy liczba będzie (p)arzysta czy (n)ieparzysta')
        zgaduje = input('> ').upper()
        if zgaduje == 'P' or zgaduje == 'N':
            return zgaduje
        else:
            print("Wybierz 'p' dla parzystych lub 'n' dla nieparzystych")


def check(lot, chooses):
    if lot % 2 == 0 and chooses == 'P':
        return True
    else:
        return False


if __name__ == '__main__':
    main()