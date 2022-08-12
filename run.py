import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
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