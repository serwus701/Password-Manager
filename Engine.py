import File_Manager
import Interface
from File_Manager import *
from Interface import *


def join_login_credentials(site_names, logins, passwords):
    login_credentials = []
    for i in range(0, len(site_names)):
        login_credentials.append([site_names[i], logins[i], passwords[i]])
    return login_credentials


def edit_login_credentials(login_credentials):
    while 1:
        match Interface.edit_login_credentials():
            case "1":
                temp_site, temp_login, temp_password = Interface.add_record()
                login_credentials = add_record(temp_site, temp_login, temp_password, login_credentials)
            case "2":
                remove_record(login_credentials)
            case "3":
                edit_record()
            case _:
                break

    return login_credentials


def add_record(site, login, password, login_credentials):
    File_Manager.add_record(site, login, password)

    return login_credentials.append([site, login, password])


def remove_record(login_credentials):
    position_to_delete = Interface.remove_record()
    if position_to_delete != "":
        print(login_credentials[0].index("youtube"))


def edit_record():
    print("edit record")


def print_results(user_search, login_credentials):
    if user_search == "qqq":
        user_search = ""

    for i in login_credentials:
        if user_search in i[0]:
            print(i)


def program_loop(login_credentials):
    user_site_input = search_bar()

    if user_site_input != "qqq":
        print_results(user_site_input, login_credentials)
    else:
        match interface():
            case "1":
                quit()
            case "2":
                print_results("qqq", login_credentials)
            case "3":
                login_credentials = edit_login_credentials(login_credentials)


def startup():
    app_login_1, app_password = read_app_login_credentials()
    site_names, logins, passwords = read_data()
    login_credentials = join_login_credentials(site_names, logins, passwords)
    user_login_input, user_password_input = app_login()

    if user_login_input == app_login_1 and user_password_input == app_password:
        while 1:
            program_loop(login_credentials)
