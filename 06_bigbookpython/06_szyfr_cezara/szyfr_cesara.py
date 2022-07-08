try:
    import pyperclip
except:
    pass

SYMBOLS = 'AABCĆDEĘFGHIJKLŁMNOÓPQRSŚTUVWXYZŻŹ1234567890'
translated = ''
# key = 5
mode = input("You are (c)ode or (d)ecode: ").lower()
key = int(input("Enter the key (max 25): "))
message = input("Type Your message: ")
message = message.upper()

for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)
        if mode == 'c':
            num += key
        elif mode == 'd':
            num -= key
        if num < 0:
            num += len(SYMBOLS)
        elif num >= len(SYMBOLS):
            num -= len(SYMBOLS)
        translated += SYMBOLS[num]
    else:
        translated += symbol
print(translated)

try:
    pyperclip.copy(translated)
    print("the text to be {} was copied to the clipboard".format(mode))
except:
    pass

def kojo():
    pass
