KEY = 3


def encrypt_1(txt):
    encrypted = ""
    for i in range(len(txt)):
        if ord(txt[i]) > 122 - KEY:
            encrypted += chr(ord(txt[i]) + KEY - 26)
        else:
            encrypted += chr(ord(txt[i]) + KEY)
    return encrypted


def encrypt(txt):
    encrypted = txt
    return encrypted


def decrypt(txt):
    decrypted = txt
    return decrypted
