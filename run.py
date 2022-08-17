import gspread
from google.oauth2.service_account import Credentials
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
        print("\nWe are glad to have you here!\n")
        print("Lets create a username for you!\n")
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
            welcome_user()
            break
        else:
            print(Fore.LIGHTYELLOW_EX +
                  "\nThe username you have entered is not valid, \
please try again.\n")


def welcome_user():
    """
    Main menu for the task manager
    """
    while True:
        print(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}\n\
Hello {username}, Welcome to Carpe Diem Task Manager!\n")
        print("Please choose an option below:\n")
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
Many thanks for using the Carpe Diem Task Manager. We're looking forward to seeing you again, {username}.")
            break
        else:
            print(Fore.LIGHTYELLOW_EX + "Please, choose a valid option.\n")


def add_new_task():
    """
     Add a new task to the database.
     Run a while loop to add a valid string of data from the user
     via the terminal, which must be 4 strings separated
     by commas. The loop will repeatedly request data, until it is valid.
    """

    while True:
        print(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}\n\
Hello {username}, Please add a task to your to do list.\n")
      
        todays_date = input("Today's date: \n")
        task = input("New task: \n")
        category = input("Category: \n")
        due_date = input("Due Date: \n")
        
        list_details = [username, todays_date, task, category, due_date]
        print("Saving your details...\n")
        database = SHEET.worksheet('database')
        database.append_row(list_details)
        print(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}\n\
Great {username}, Your task was added to Carpe Diem Task Manager.\n")
        print("\nTaking you to the main menu...")
        welcome_user()
        break


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

