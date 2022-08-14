from os import system
from colorama import init, Fore, Back, Style
from getpass import getpass
import stdiomask
from time import sleep
init(autoreset=True)


CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('task-tracker')


def show_menu():
    """
    Show the options menu to the user
    """
    print(Fore.GREEN + 
    """
    *********************************************************************
                        Welcome to your Task Manager
    *********************************************************************        
Choose an Option:
[1] Sign up
[2] Log in
[3] Exit (or type Enter) 
""")
    try:
        opcao = int(input('Digite sua opção: '))
        return(opcao)
    except ValueError:
        print()


show_menu()


def signup():
    print("Please enter the username:")
    username = input("Username:  ")
    print("Please enter a password:")
    password = stdiomask.getpass(prompt="Password:  ", mask='*')


signup()

def add_user(data):
   """
    Add user to users worksheet
   """
print("Signing you up...\n")
users_worksheet = SHEET.worksheet('users')
users_worksheet.append_row(data)
print("Your login was created successfully.\n")

data = signup()