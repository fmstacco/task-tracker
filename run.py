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
from colorama import Fore, Style
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


def welcome_new_user():
    """
    Main menu for the task manager
    """
    while True:
        print(f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}\n\
Hello {username}, Welcome to Carpe Diem Task Manager!\n")
        print("Please choose an option below:\n")
        print("Type '1' to add a new task.")
        print("Type '2' to exit the task manager.\n")

        answer = input("\nEnter your option here: \n")
        if answer == "1":
            add_new_task()
            break
        elif answer == "2":
            print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}\n\
Goodbye {username}. We're looking forward to seeing you again!/n")
            break
        else:
            print(Fore.LIGHTYELLOW_EX + "Please, choose a valid option.\n")


def welcome_user():
    """
    Main menu for the task manager
    """
    while True:
        print(f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}\n\
{username}, please choose an option below\n")
        print("Type '1' to add a new task.")
        print("Type '2' to view your saved tasks.")
        print("Type '3' to delete a task .")
        print("Type '4' to exit the task manager.\n")

        answer = input("\nEnter your option here: \n")
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
            print(f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}\n\
Press the button 'Run Task Tracker' to go back to the system.")
        break


def add_new_task():
    """
     Add a new task to the database.
     Run a while loop to add a valid string of data from the user
     via the terminal, which must be 4 strings separated
     by commas. The loop will repeatedly request data, until it is valid.
    """
    print(f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}\n\
Lets add a task to your to do list.\n")
    print("First lets create a task code: 'todays date + time' \
            \nexample: '17/08/22 3:17pm', type: '1708221517': \n")
    while True:
        task_code = input("\nTask code: \n")
        if task_code == "" or task_code == "  " or len(task_code) < 3:
            print(Fore.LIGHTYELLOW_EX + "Please,\
                  \ntype a task code ex. 'todays date + time''1708221517'.\n")
        else:
            break

    while True:
        todays_date = input("\nToday's date: \n")
        if todays_date == "" or todays_date == "  " or len(todays_date) < 6:
            print(Fore.LIGHTYELLOW_EX +
                  "Please, type the todays date eg. 17/08/22.\n")
        else:
            break

    while True:
        task_description = input("\nNew task: \n")
        if task_description == "" or len(task_description) < 3:
            print(Fore.LIGHTYELLOW_EX + "Please, type a description.\n")
        else:
            break

    while True:
        due_date = input("\nDue Date: \n")
        if due_date == "" or due_date == "  " or len(due_date) < 6:
            print(Fore.LIGHTYELLOW_EX + "Please, type a due date 20/08/22.\n")
        else:
            break

    while True:
        print("\nType the status of your task \
                \n [1] to do \
                \n [2] doing \
                \n [3] done\n")
        status_task = input("Status: \n")
        if status_task == "1" or status_task == "2" or status_task == "3":
                list_details = [
                    username, task_code, todays_date,
                    task_description, due_date, status_task]
                print("Saving your task on the database...\n")
                database = SHEET.worksheet('database')
                database.append_row(list_details)
                print(f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}\n\
Great {username}, Your task was added to Carpe Diem Task Manager.\n")
                print("\nLets see your saved tasks...")
                view_saved_tasks()
                break
        else:
                print(Fore.LIGHTYELLOW_EX + "Please, select a valid option.\n")


def delete_task():
    """
    Allows the user to delete a saved task.
    """
    while True:
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "Please, type the task code you want to delete,\
            \nor type 'm' to return to the main menu:\n")
        code_delete = input("task code: \n")
        if code_delete == 'm' or code_delete == 'M':
            welcome_user()
            break
        elif stored_data.find(code_delete, in_column=2):
            row = stored_data.find(code_delete, in_column=2).row
            print(Fore.LIGHTGREEN_EX + Style.BRIGHT +
                  "\nWe found the task in our database.\n")
            print(Fore.LIGHTYELLOW_EX + Style.BRIGHT +
                  "\nLet's delete it.\n")
            database = SHEET.worksheet('database')
            database.delete_rows(row)
            print(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}\n\
Great {username}, Your task was deleted from Carpe Diem Task Manager.")
            print("\nTaking you to the main menu...")
            welcome_user()
            break
        else:
            print(Fore.LIGHTYELLOW_EX +
                  "\nTask not found, please try again.")


def view_saved_tasks():
    """
    Allows the user to see the saved tasks.
    """
    if stored_data.find(username, in_column=1):
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT +
              "\nThe tasks you currently have saved are:\n")
        df = pd.DataFrame(stored_data.get_all_records())
        user_record = df.loc[df['username'] == username].to_string(index=False)
        print(f"{Fore.LIGHTYELLOW_EX }{Style.BRIGHT}\n{user_record}\n")
        print("\nTaking you to the main menu...")
        welcome_user()


def welcome_returning_user():
    """
       Welcome screen for returning users
    """
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT +
          "\nWelcome back! Please enter your username,")
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT +
          "or type 'n' to create a new username:")
    while True:
        global username
        username = input("\nEnter your username here:\n")

        if username == 'n' or username == 'N':
            new_user()
            break
        elif stored_data.find(username, in_column=1):
            print("\nTaking you to the main menu...")
            welcome_user()
            break
        else:
            print(Fore.LIGHTYELLOW_EX +
                  "\nUsername not found, please try again,\
                    \n or type 'n' to create a new username:")


def new_user():
    """
       This function will register the new user and \
       \nsend the data to the first column of the Database spreadsheet.
    """
    while True:
        print(Fore.LIGHTBLUE_EX+Style.BRIGHT +
              "\nLet's create a username for you!\n")
        print("Usernames must be between 2 and 10 characters,")
        print("and should contain only letters from a to z.\n")

        global username
        username = input("\nEnter your username here: \n")

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


def welcome_screen():
    """
    Welcome screen with initial instructions to the user
    """


print(Fore.LIGHTBLUE_EX + Style.BRIGHT +
      "******************************************************************")
print(Fore.LIGHTBLUE_EX + Style.BRIGHT +
      "               Welcome to Carpe Diem Task Manager                    ")
print(Fore.LIGHTBLUE_EX + Style.BRIGHT +
      "******************************************************************\n")
print("In this system you can better organize yourself")
print("by listing all the tasks you need to do.\n")
print("You will be able to create a username, add tasks,")
print("delete tasks, view saved tasks and also returning to the system.\n")


while True:
    print("To get started, please choose an option below:\n")
    print("[1] Create a new task list")
    print("[2] Access a saved task list\n")

    option = input("\nPlease enter your choice here: \n")

    if option == "1":
        new_user()
        break
    elif option == "2":
        welcome_returning_user()
        break
    else:
        print(Fore.LIGHTYELLOW_EX + "Please, select a valid option.\n")


welcome_screen()
