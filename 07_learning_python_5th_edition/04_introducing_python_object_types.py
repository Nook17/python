#!/usr/bin/env python3
def main():
    # immutability()
    # typeSpecificMethods()
    # gettingHelp()
    # unicodeStrings()
    # sequenceOperations()
    # typeSpecificOperations()
    # nesting()
    # comprehensions()
    mappingOperations()


# ------------ LISTS ------------
def immutability():
    s = 'Spam'
    l = list(s)
    print(l)
    l[1] = 'r'
    p = ''.join(l)
    print(p)
    print('-----------------')
    b = bytearray(b'mini')
    b.extend(b'maraton')
    print(b)
    c = b.decode()
    print(c)


def typeSpecificMethods():
    s = 'Podczas rundy we Włoszech najlepszymi kierowcami okazali się Alvaro Bautista i Toprak Razgatlioglu'
    print(s.find('we'))
    d = s.replace('we', 'na')
    print(d)
    print('-----------------')
    c = 'aaaa,sssss,eeee,dddd,ww,ggg,ttt'
    k = c.split(',')
    print(k)
    print('-----------------')
    p = '   Arek     '
    print(p)
    c = p.lstrip()
    print(c)
    print('-----------------')
    print('{:,.2f}'.format(2655432.4325))
    print('%.2f | %+05d' % (3.14159, 42))


def gettingHelp():
    s = 'nook'
    print(dir(s))       # zmienną s można zamienić na str, list i dict
    print(help(str.replace))


def unicodeStrings():
    # ASCII -> https://www.ascii-code.com/
    a = '\x9B\x4E\x4E\x6B\x6F\x68\x86\xBD\xF8'
    print(a)
    b = 'sp\xc4\u00c4\U000000c4m'   # x - HEX    u i U - UNICODE short & long
    print(b)


# ------------ LISTS ------------
def sequenceOperations():
    a = ['123', 'arek', '23.4']
    print(len(a))
    print(a[:-1])
    print(a + [11, 22, 33])
    print(a * 3)


def typeSpecificOperations():
    a = ['123', 'arek', '23.4']
    a.append('Nook')
    print(a)
    a.pop(1)
    print(a)
    b = ['ddd', 'www', 'sss', 'aaa']
    b.sort()
    print(b)
    b.reverse()
    print(b)


def nesting():
    a = [[2, 4, 9], [5, 2, 8], [9, 1, 2]]
    print(a[1][2])

def comprehensions():
    a = [[2, 4, 9],
         [6, 2, 8],
         [9, 1, 2]]
    col2 = [row[1] for row in a]    # pobranie drugiej kolumny z macierzy
    print(col2)
    col2parzysta = [r[1] for r in a if r[1] % 2 == 0]   # jak wyżej, ale tylko dla parzystych elementów
    print(col2parzysta)
    diagonal = [a[i][i] for i in [0, 1, 2]]    # pobranie przekątnej z macierzy
    print(diagonal)
    print('-----------------')
    b = 'spam'
    doubles = [i * 2 for i in b]    # powtórzenie znaków
    print(doubles)
    print('-----------------')
    c = list(range(5))
    d = list(range(-6, 7, 2))
    print('{}\n{}'.format(c, d))
    e = [[x ** 2, x ** 3] for x in range(5)]
    f = [[x, x / 2, x * 2] for x in range(-8, 8, 2) if x > 0]
    print('{}\n{}'.format(e, f))
    print('-----------------')
    g = (sum(row) for row in a) # sumowanie liczb w wierszach macierzy a
    for i in range(3):
        print(next(g))
        i += 1
    h = list(map(sum, a))       # jak wyżej, ale za pomocą funkcji map
    print(h)
    print('-----------------')


# ------------ DICTIONARIES ------------
def mappingOperations():
    a = {'food': 'spam', 'quantity': 4, 'color': 'red'}
    print(a['food'])
    b = {}
    b['name'] = 'Arek'
    b['age'] = 42
    b['job'] = 'soldier'
    print(b)
    c = dict(name = 'Michael', job = 'police', age = 10)
    print(c)
    d = dict(zip(['job', 'name', 'age'], ['fireman', 'Kojo', 12]))
    print(d)



if __name__ == '__main__':
    main()
