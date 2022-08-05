#!/usr/bin/env python3
# ---------------------- Crypto Files ----------------------
#
# WWW - https://hashdork.com/pl/file-encryption-decryption-using-python/
#
# ----------------------------------------------------------
from cryptography.fernet import Fernet
import json

key = b'Xy8u2GtHOaHlULVywaL6xBeAb48oiG1UAYxybLdNQ24='
# score = b"{'Nook': 17, 'Kojo': 1, 'Kama': 11, 'Amon': 0}"
s = {'Nook': 256, 'Kojo': 274, 'Kama': 22, 'Amon': 0}
score = json.dumps(s).encode('utf-8')


def main():
    global key
    global score
    saveScore(score, key)
    openScore(key)


def saveScore(scores, keys):
    f = Fernet(keys)

    encrypted = f.encrypt(scores)

    with open('score', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


def openScore(keys):
    f = Fernet(keys)
    with open('score', 'rb') as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = f.decrypt(encrypted)

    d = decrypted.decode('utf8')
    data = eval(d)
    print(data)
    # print(type(data))
    # print(data['Nook'])


if __name__ == '__main__':
    main()