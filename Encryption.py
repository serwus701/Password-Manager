from cryptography.fernet import Fernet

key = Fernet.generate_key()
fernet = Fernet(key)


def encrypt_text(txt):
    #encoded = fernet.encrypt(txt.encode())
    encoded = txt
    return encoded


def encrypt_list(list):
    return list


def decrypt_text(txt):
    #decoded = fernet.decrypt(txt).decode()
    decoded = txt
    return decoded


def decrypt_list(list):
    return list
