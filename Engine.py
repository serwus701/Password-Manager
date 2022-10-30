from File_Manager import read_data
from Interface import *

app_login_1, app_password, site_names, logins, passwords = read_data()


def join_login_credentials():
    login_credentials = []
    for i in range(0, len(site_names)):
        login_credentials.append([site_names[i], logins[i], passwords[i]])
    return login_credentials


def startup():
    user_login_input, user_password_input = app_login()

    if user_login_input == app_login_1 and user_password_input == app_password:

        login_credentials = join_login_credentials()

        while 1:
            user_site_input = search_bar()

            if user_site_input != "qqq":
                for i in login_credentials:
                    if user_site_input in i[0]:
                        print(i)
            else:
                interface()
