#!/usr/bin/env python3
# ---------------------- Crypto Files ----------------------
#
# WWW - https://hashdork.com/pl/file-encryption-decryption-using-python/
#
# ----------------------------------------------------------
from cryptography.fernet import Fernet


def main():
    key = loadKeyFile()
    print(type(key))
    print(key)
    # fileEncryption(key)
    # fileDecryption(key)


# ***** create key *****
def createKey():
    key = Fernet.generate_key()
    with open('nook.key', 'wb') as myKey:
        myKey.write(key)


# ***** load key file *****
def loadKeyFile():
    with open('nook.key', 'rb') as myKey:
        key = myKey.read()
    return key


# ***** File Encryption *****
def fileEncryption(key):
    f = Fernet(key)
    with open('score.txt', 'rb') as original_file:
        original = original_file.read()

    encrypted = f.encrypt(original)

    with open('score_crypto', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


# ***** File Decryption *****
def fileDecryption(key):
    f = Fernet(key)
    with open('score_crypto', 'rb') as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = f.decrypt(encrypted)

    with open('score2.txt', 'wb') as decrypted_file:
        decrypted_file.write(decrypted)


if __name__ == '__main__':
    main()