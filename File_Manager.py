from Encryption import decrypt


def read_data():
    site_name = []
    logins = []
    passwords = []

    file = open("login_credentials.txt", "r")
    app_login = file.readline()
    app_password = file.readline()

    for _ in file:
        login_and_password = file.readline().split(" ", 1)

        site_name += login_and_password[0]
        logins += login_and_password[1]
        passwords += login_and_password[2]

    file.close()

    return decrypt(app_login), decrypt(app_password), decrypt(logins), decrypt(passwords)
