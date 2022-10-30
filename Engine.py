from File_Manager import read_data
from Interface import app_login
from Interface import search_bar

app_login_1, app_password, site_names, logins, passwords = read_data()


def map_elements():
    login_credentials = {}
    for key in range(0, len(site_names) - 1):
        login_credentials[site_names[key]] = [logins[key], passwords[key]]
    return login_credentials


def startup():
    user_login_input, user_password_input = app_login()

    if user_login_input == app_login_1 and user_password_input == app_password:
        login_credentials = [logins, passwords]

        print("you're in!")

        for i in map_elements():
            print(i)
