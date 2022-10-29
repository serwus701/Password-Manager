from File_Manager import read_data
from Interface import app_login

app_login_1, app_password, site_names, logins, passwords = read_data()


def map_elements(site_name):
    position = site_names.index(site_name)
    return [logins[position], passwords[position]]


def startup():
    user_login_input, user_password_input = app_login()

    if user_login_input == app_login_1 and user_password_input == app_password:
        login_credentials = [logins, passwords]

        print("you're in!")

        credentials_map = map(site_names, login_credentials)

        print(credentials_map)
