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


def get_tasks_data():
    """
    Get tasks data.
    Run a while loop to add a valid string of data from the user
    via the terminal, which must be 4 strings separated
    by commas. The loop will repeatedly request data, until it is valid.
    """
    while True:
        print("Please add a task to your to do list.\n")
        print("Data should be separated by commas.\n")
        print("Example: Today's Date, Task, Category, Due Date\n")
        print("Example: 28/07/22, Plan project, Studies, 20/08/22\n")

        data_str = input("Add your task here: \n")

        tasks_data = data_str.split(",")

        if validate_data(tasks_data):
            print('Data is Valid!\n')
            break

    return tasks_data


def validate_data(values):
    """
    Inside the try, verifies if data provided are exactly 4 values.
    Raises ValueError if there aren't exactly 4 values.
    """
    try:
        if len(values) != 4:
            raise ValueError(
                f"Exactly 4 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    
    return True


def add_task_worksheet(data):
    """
    Update task worksheet, add new row with the list data provided

    """
    print("Adding task to your worksheet...\n")
    task_worksheet = SHEET.worksheet("database")
    task_worksheet.append_row(data)
    print("Task added successfully\n")


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


def welcome_screen():
    """
    Welcome screen with initial instructions to the user
    """
    data = get_tasks_data()
    add_task_worksheet(data)
    
       
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

