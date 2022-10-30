from Encryption import *


def read_app_login_credentials():
    file = open("app_login_credentials.txt", "r")
    app_login = file.readline().split("\n")[0]
    app_password = file.readline().split("\n")[0]

    return decrypt_text(app_login), decrypt_text(app_password)


def read_data():
    site_names = []
    logins = []
    passwords = []

    file = open("login_credentials.txt", "r")

    for read in file:
        login_and_password = read.split(" ", 2)

        site_names.append(login_and_password[0])
        logins.append(login_and_password[1])
        passwords.append(login_and_password[2].split("\n")[0])

    file.close()

    return decrypt_list(site_names), decrypt_list(logins), decrypt_list(passwords)


def add_record(site, login, password):
    file = open("login_credentials.txt", "a")
    file.write("\n" + encrypt_text(site) + " " + encrypt_text(login) + " " + encrypt_text(password))


def remove_record(login_credentials):
    file = open("login_credentials.txt", "w")

    for each_site_credential in login_credentials:
        file.write(each_site_credential[0] + " " + each_site_credential[1] + " " + each_site_credential[2] + "\n")
