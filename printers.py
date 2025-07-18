from termcolor import colored

def print_menu():
    print("1. Kirish")
    print("2. Ro'yxatdan o'tish")


def print_satus(text, status):
    types = {
        'error': 'red',
        'success': 'green'
    }
    colored_text = colored(text, types[status])
    print(colored_text)