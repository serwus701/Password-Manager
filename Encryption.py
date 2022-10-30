KEY = 3


def encrypt_1(txt):
    encrypted = ""
    for i in range(len(txt)):
        if ord(txt[i]) > 122 - KEY:
            encrypted += chr(ord(txt[i]) + KEY - 26)
        else:
            encrypted += chr(ord(txt[i]) + KEY)
    return encrypted


def encrypt_text(txt):
    encrypted = txt
    return encrypted


def encrypt_list(list):
    return list


def decrypt_text(txt):
    decrypted = txt
    return decrypted


def decrypt_list(list):
    return list
