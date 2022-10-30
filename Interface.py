def app_login():
    # login = input("Insert login:\n")
    # password = input("Insert password:\n")

    login = "your_login"
    password = "your_password"

    return login, password


def search_bar():
    return input("Insert site name: (press qqq to enter interface)\n")


def interface():
    return input("any to [back]\n1 to [exit]\n2 to [print all]\n3 to [edit login credentials]\n")


def edit_login_credentials():
    print("Login credentials:")
    return input("any to [back]\n1 to [add]\n2 to [delete]\n3 to [edit]\n")


def add_record():
    site = input("Insert site name\n")
    login = input("Insert login\n")
    password = input("Insert password\n")

    return site, login, password
