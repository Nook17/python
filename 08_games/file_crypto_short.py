#!/usr/bin/env python3
# ---------------------- Crypto Files ----------------------
#
# WWW - https://hashdork.com/pl/file-encryption-decryption-using-python/
#
# ----------------------------------------------------------
from cryptography.fernet import Fernet

key = b'Xy8u2GtHOaHlULVywaL6xBeAb48oiG1UAYxybLdNQ24='
score = b"{'Nook': 17, 'Kojo': 1, 'Kama': 11, 'Amon': 0}"


def main():
    global key
    global score
    saveScore(score, key)
    openScore(key)


def saveScore(scores, keys):
    f = Fernet(keys)

    encrypted = f.encrypt(scores)

    with open('score_crypto2', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


def openScore(keys):
    f = Fernet(keys)
    with open('score_crypto2', 'rb') as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = f.decrypt(encrypted)

    data = decrypted.decode('utf8')
    print(data)


if __name__ == '__main__':
    main()