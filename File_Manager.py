from Encryption import decrypt


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

    return decrypt(app_login), decrypt(app_password), decrypt(site_names), decrypt(logins), decrypt(passwords)
