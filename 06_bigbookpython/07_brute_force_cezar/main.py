from os import system, name
import sys, bext

SYMBOLS_PL = 'AABCĆDEĘFGHIJKLŁMNOÓPQRSŚTUVWXYZŻŹ1234567890'     # 44
SYMBOLS_EN_NUM = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'         # 36
SYMBOLS_EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'                       # 26
translated = {}


def main():
    clear()
    keyRange = ''
    bext.fg('yellow')   # black, red, green, yellow, blue, purple, cyan, white
    print('''
 ------------------------------------------------
|         Please select your alphabet            |
 ------------------------------------------------
''')
    bext.fg('green')
    print("1", end='')
    bext.fg('yellow')
    print(" - AABCĆDEĘFGHIJKLŁMNOÓPQRSŚTUVWXYZŻŹ1234567890")
    bext.fg('green')
    print("2", end='')
    bext.fg('yellow')
    print(" - ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
    bext.fg('green')
    print("3", end='')
    bext.fg('yellow')
    print(" - ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    bext.fg('green')
    print("q", end='')
    bext.fg('yellow')
    print(" - quit\n")

    bext.fg('reset')
    alphabet = input('> ')
    if alphabet == '1':
        keyRange = 44
    elif alphabet == '2':
        keyRange = 36
    elif alphabet == '3':
        keyRange = 26
    elif alphabet == 'q':
        endProgram()
    else:
        main()

    print('Type Your message: ')
    bext.fg('red')
    message = input('> ')
    message = message.upper()
    translated = translate(message, keyRange)
    printResult(translated, keyRange)


def translate(message, keyRange):
    for key in range(keyRange):
        word = ''
        for symbol in message:
            if symbol in SYMBOLS_PL:
                num = SYMBOLS_PL.find(symbol)
                num -= key
                if num < 0:
                    num += len(SYMBOLS_PL)
                elif num >= len(SYMBOLS_PL):
                    num -= len(SYMBOLS_PL)
                word += SYMBOLS_PL[num]
            else:
                word += symbol
            translated[key] = word
    return translated


def printResult(translated, keyRange):
    bext.fg('cyan')
    for key in range(keyRange):
        print('key #{}: {}'.format(key, translated[key]))
    bext.fg('green')
    print("\nc", end='')
    bext.fg('yellow')
    print(" - continue")
    bext.fg('green')
    print("q", end='')
    bext.fg('yellow')
    print(" - quit\n")
    bext.fg('reset')
    choice = input('> ')
    if choice == 'c':
        main()
    else:
        endProgram()

def clear():
   if name == 'nt':
        _ = system('cls')   # for windows
   else:
        _ = system('clear') # for mac and linux (here, os.name is 'posix')


def endProgram():
    bext.fg('purple')
    sys.exit('\n\tHave a nice day ...\n')


if __name__ == '__main__':
    main()

# ---- Another way to clear screen ----
# from subprocess import call
# def clear():
    # check and make call for specific operating system
    # _ = call('clear' if os.name == 'posix' else 'cls')