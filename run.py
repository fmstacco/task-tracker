import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('task-tracker')


def get_tasks_data():
    """
    Get tasks data.
    Run a while loop to add a valid string of data from the user
    via the terminal, which must be 4 strings separated
    by commas. The loop will repeatedly request data, until it is valid.
    """
    while True:
        print("Please add a task to your to do list.")
        print("Data should be separated by commas.")
        print("Example: Today's Date, Task, Category, Due Date")
        print("Example: 28/07/22, Plan project portfolio 3, Studies, 20/08/22")

        data_str = input("Add your task here:\n")

        tasks_data = data_str.split(",")

        if validate_data(tasks_data):
            print('Data is Valid!')
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
    task_worksheet = SHEET.worksheet("tasks")
    task_worksheet.append_row(data)
    print("Task added successfully\n")
  

def main():
    """
    Run all program functions
    """

data = get_tasks_data()
add_task_worksheet(data)