
from getpass import getpass
from printers import print_menu, print_satus
from utils import (
    is_valid_username, is_same_password, 
    is_valid_password, laod_users, 
    add_user, make_password,
    is_username, get_user,
)


def main() -> None:
    print_menu()

    op = input("> ")

    if op == '1':
        username = input("username: ")
        password = getpass("password: ")

        user = get_user(username, password)
        if user:
            print_satus("muvaffaqiyatli kirdingiz.", 'success')
        else:
            print_satus("user topilmadi", 'error')

    elif op == '2':
        username = input("username: ")
        password = getpass("password: ")
        confirm_password = getpass("confirm password: ")

        if is_username(username):
            print_satus("bu username tanlangan.", "error")
        elif not is_valid_username(username):
            print_satus("username faqat harflardan iborat bolsin.", 'error')
        elif not is_valid_password(password):
            print_satus("pasrol kamida 8 ta belgigan iborat bolsin.", 'error')
        elif not is_same_password(password, confirm_password):
            print_satus("parol mos emas.", 'error')
        else:
            add_user(username, make_password(password))
            print_satus("ro'yxatdan otdingiz.", 'success')
    else:
        print("xato tanlov")

main()