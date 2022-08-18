# Carpe Diem Task Manager
# By Fabiana Martins de Souza Tacco
# https://github.com/fmstacco/

"""This code was developed having as a main inspiration the following \
\nrepository: https://github.com/frankiesanjana/mortgage-calculator.\
\nI borrowed some of the code from this repository to help create the task\
\nmanager.I have also customized some of the code to achieve the project goals.
"""

# imports

import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('task-tracker')
stored_data = SHEET.worksheet('database')


def new_user():
    """
       This function will register the new user and send the data to the first column of the Database spreadsheet.
    """
    while True:
        print("\nLet's create a username for you!\n")
        print("Usernames must be between 2 and 10 characters,")
        print("and should contain only letters from a to z.\n")

        global username
        username = input("Enter your username here:\n")

        if stored_data.find(username, in_column=1):
            print(Fore.LIGHTYELLOW_EX +
                  "\nSorry, that username has already been taken.")
            print(Fore.LIGHTYELLOW_EX +
                  "Please choose an alternative username.\n")
        elif username.isalpha() and len(username) > 1 and len(username) < 11:
            welcome_new_user()
            break
        else:
            print(Fore.LIGHTYELLOW_EX +
                  "\nThe username you have entered is not valid, \
please try again.\n")


def welcome_new_user():
    """
    Main menu for the task manager
    """
    while True:
        print(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}\n\
Hello {username}, Welcome to Carpe Diem Task Manager!\n")
        print("Please choose an option below:\n")
        print("Type '1' to add a new task.")
        print("Type '2' to exit the task manager.\n")

        answer = input("Enter your option here:\n")
        if answer == "1":
            add_new_task()
            break
        elif answer == "2":
            print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}\n\
Goodbye {username}. We're looking forward to seeing you again!")
            break
        else:
            print(Fore.LIGHTYELLOW_EX + "Please, choose a valid option.\n")        


def welcome_user():
    """
    Main menu for the task manager
    """
    while True:
        print(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}\n\
{username}, please choose an option below\n")
        print("Type '1' to add a new task.")
        print("Type '2' to view your saved tasks.")
        print("Type '3' to delete a task .")
        print("Type '4' to exit the task manager.\n")

        answer = input("Enter your option here:\n")
        if answer == "1":
            add_new_task()
            
            break
        elif answer == "2":
            view_saved_tasks()
            break
        elif answer == "3":
            delete_task()
            break
        elif answer == "4":
            print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}\n\
Goodbye {username}. We're looking forward to seeing you again!.")
            break


def add_new_task():
    """
     Add a new task to the database.
     Run a while loop to add a valid string of data from the user
     via the terminal, which must be 4 strings separated
     by commas. The loop will repeatedly request data, until it is valid.
    """

    while True:
        print(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}\n\
Lets add a task to your to do list.\n")
      
        print("First lets create a task task code: 'todays date + time' \
            \nexample: '17/08/22 3:17pm', type: '1708221517': \n")
        task_code = input("Task code: \n")
        
        if task_code == "":
            print(Fore.LIGHTYELLOW_EX + "Please, type a task code.\n")

        todays_date = input("\nToday's date: \n")
        task = input("\nNew task: \n")
        due_date = input("\nDue Date: \n")
        print("\nType the status of your task \
            \n [1] to do \
            \n [2] doing \
            \n [3] done\n")
        status = input("Status: \n") 
        
        list_details = [username, task_code, todays_date, task, due_date, status]
        print("Saving your task on the database...\n")
        database = SHEET.worksheet('database')
        database.append_row(list_details)
        print(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}\n\
Great {username}, Your task was added to Carpe Diem Task Manager.\n")
        print("\nLets see your saved tasks...")
        view_saved_tasks()
        break


def view_saved_tasks():
    """
    Allows the user to see the saved tasks.
    """
    if stored_data.find(username, in_column=1):
        print(Fore.LIGHTGREEN_EX + Style.BRIGHT +
              "\nThe tasks you currently have saved are:\n")
        df = pd.DataFrame(stored_data.get_all_records())
        user_record = df.loc[df['username'] == username].to_string(index=False)
        print(f"{Fore.LIGHTCYAN_EX }{Style.BRIGHT}\n{user_record}\n")
        print("\nTaking you to the main menu...")    
        welcome_user()

def welcome_screen():
    """
    Welcome screen with initial instructions to the user
    """


print(Fore.LIGHTGREEN_EX + Style.BRIGHT + 
"****************************************************************************")
print(Fore.LIGHTGREEN_EX + Style.BRIGHT +
        "               Welcome to Carpe Diem Task Manager                    ")
print(Fore.LIGHTGREEN_EX + Style.BRIGHT +
        "****************************************************************************\n") 
print("In this system you can better organize yourself")
print("by listing all the tasks you need to do.\n")

while True:
    print("To get started, please choose an option below:\n")
    print("[1] Create a new task list")
    print("[2] Access a saved task list\n")

    type = input("Please enter your choice here: \n")

    if type == "1":
        new_user()
        break
    elif type == "2":
        returning_user()
        break
    else:
        print(Fore.LIGHTYELLOW_EX + "Please, select a valid option.\n")

welcome_screen()

