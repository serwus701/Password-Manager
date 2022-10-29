from File_Manager import read_data
from Interface import app_login

app_login_1, app_password, logins, passwords = read_data()


def map_elements(position):
    return passwords[position]


def startup():
    user_login_input, user_password_input = app_login()

    print("Hello?")
    print(app_login_1)
    print(app_password)
    if user_login_input == app_login_1 and user_password_input == app_password:
        login_credentials = map(logins, passwords)

        print("you're in!")
        print(login_credentials)
