from Encryption import *


def read_data():
    site_names = []
    logins = []
    passwords = []

    file = open("login_credentials.txt", "r")
    app_login = file.readline().split("\n")[0]
    app_password = file.readline().split("\n")[0]

    for _ in file:
        login_and_password = file.readline().split(" ", 2)

        site_names += login_and_password[0]
        logins += login_and_password[1]
        passwords += login_and_password[2]

    file.close()

    return decrypt_text(app_login), decrypt_text(app_password), decrypt_list(site_names), decrypt_list(logins), decrypt_list(passwords)
