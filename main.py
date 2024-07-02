import csv
import getpass
import cv2
from module.users.emp import Users
from module.users.users_manger import Employees as EMP
from data_analysis.data_analysis import DataAnalysis as DA
from data.assets import AddAssets as Assets
from module.chat.chat import chatgpt_chat
from simple_term_menu import TerminalMenu
from termcolor import colored
from art import *
import colorama
import os



colorama.init()


emp_manager = EMP()
data_analysis = DA()
users = Users()
file_path= "data/devices.csv"
assets = Assets(file_path)

Art = text2art("Mr.IT", font='block', chr_ignore=True)
print(colored(Art, 'blue'))


def clear_console():
    """
    Clears the console screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def menuIT():
    options = [
        "1. View Profile",
        "2. Delete Account",
        "3. View Assets",
        "4. Qrcode Reader",
        "5. Exit"
    ]

    main_menu = TerminalMenu(options, menu_cursor="-> ",
                menu_cursor_style=("bg_red", "fg_yellow"),
                menu_highlight_style=("bg_green", "fg_yellow"),

                cycle_cursor=True,)
    quiting = False

    while not quiting:
        optionsIndex = main_menu.show()
        optionsChoice = options[optionsIndex]
        clear_console()

        if optionsChoice.endswith("Exit"):
            print(colored("Thank you for using Mr.IT System. Stay safe, see you soon! 👋", 'blue', attrs=['bold']))
            quiting = True
        elif optionsChoice.startswith("1"):
            view_profile()
        elif optionsChoice.startswith("2"):
            identifier = input("Enter user ID or name to delete: ")
            delete_account(identifier)
        elif optionsChoice.startswith("3"):
            view_assets()
        elif optionsChoice.startswith("4"):
             print(colored("Scanning......","light_green",attrs=['bold']))
             assets.qrcode_reader()
             if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
             print(colored("Exiting the Qrcode ...", 'red', attrs=['bold']))

def view_profile():

    print(colored("Profile Details:", 'blue', attrs=['bold']))
    file_path = 'data/users.csv'
    user_found = False
    try:
        search_term = input("Enter the Your ID for: ")
        with open(file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row['Employee ID'].lower() == search_term.lower():
                    print(colored(f" Welcome {row['Employee Name']}👋 \n Employee Name: {row['Employee Name']} \n Employee ID: {row['Employee ID']}\n Employee Role: {row['Employee Role']}\n Employee Gender: {row['Employee Gender']}\n\n",'green',attrs=['bold']))
                    user_found = True # FOUND THE USER
                    break  

        if not user_found:  # USER NOT FOUND
            print(colored("Opss User not found.", 'red', attrs=['bold']))

    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
        
def delete_account(identifier):
        """
        Deletes a user from the 'data/users.csv' file based on the provided identifier.

        Args:
            identifier (str): The ID or name of the user to be deleted.

        Returns:
            None
        """
        try:
            with open('data/users.csv', 'r') as file:
                reader = csv.reader(file)
                users = list(reader)
            
            if not users or len(users) == 1:
                print(colored("No ID found. Please check your ID.", 'red', attrs=['bold']))
                return
            
            # Remove header
            header = users.pop(0)

            # Find the user to delete by ID or name
            deleted = False
            for user in users:
                if len(user) == 6 and (user[-1] == identifier):
                    users.remove(user)
                    deleted = True
                    break

            with open('data/users.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(header)
                writer.writerows(users)

            if deleted:
                print(colored(f"User with ID '{identifier}' has been deleted successfully.", 'green', attrs=['bold']))
            else:
                print(colored(f"No user found with ID  '{identifier}'.", 'red', attrs=['bold']))
        except FileNotFoundError:
            print(colored("The file was not found!", 'red', attrs=['bold']))

def view_assets():
    try:
        print(colored("open this File Below:", 'blue', attrs=['bold']))
        pdf_path = os.path.abspath('data/pdf/assets_report.pdf')
        print(colored(pdf_path, 'green', attrs=['bold']))
    except Exception as e:
        print(f"An error occurred while viewing assets: {e}")




def menuAdmin():
    options = [
        "1. Mr.IT chat    🤖",
        "2. Dashboard     📊",
        "3. User Managers 🎩",
        "4. Assets        📝",
        "5. Exit          🚪"
    ]

    main_menu = TerminalMenu(options,
                menu_cursor="-> ",
                menu_cursor_style=("bg_green", "fg_yellow"),
                menu_highlight_style=("bg_green", "fg_yellow"),
                cycle_cursor=True,
                )
    quiting = False

    while not quiting:
        optionsIndex = main_menu.show()
        optionsChoice = options[optionsIndex]
        clear_console()

        if optionsChoice.endswith("exit"):
            print(colored("Thanks for using MR.IT System 🩵\nStay safe, see you soon! 👋", 'blue', attrs=['bold']))
            quiting = True
        elif optionsChoice.startswith("1"):
            print(colored("Welcome to the Mr.IT chat 🤖\n\n", "blue", attrs=['bold']))
            chatgpt_chat()
        elif optionsChoice.startswith("2"):
            data_analysis.dashboard_menu()
        elif optionsChoice.startswith("3"):
             emp_manager.user_manager_menu()
        elif optionsChoice.startswith("4"):
            assets.assets_menu()
             
        elif optionsChoice.startswith("5"):
             quiting = True
        
def main():
    """
    The main function that handles the login and registration process for Mr.IT System.
    """
    try:
        options = [
            "1. Login Press 1 🔑",
            "2. Sign up Press 2 🆕 ",
            "3. Exit 🚪",
        ]

        employees = EMP()
        mainMenu = TerminalMenu(options,title="\n\n<========= Assets Management Menu =========>\n\n",
                menu_cursor="-> ",
                menu_cursor_style=("bg_blue", "fg_yellow"),
                menu_highlight_style=("bg_green", "fg_yellow"),
                cycle_cursor=True,
                )
        quiting = False

        while not quiting:
            optionsIndex = mainMenu.show()
            optionsChoice = options[optionsIndex]
            clear_console()
            # print(colored("\n\n<============ Welcome to Mr.IT Registration Page 🔑🚪 ============>\n", 'blue', attrs=['bold']))
            if optionsChoice.startswith("1"):
                email = input(colored('Enter your email: ', 'green', attrs=['bold'])).lower()
                password = getpass.getpass(colored('Enter your password: ', 'green', attrs=['bold'])).lower()
                user = employees.auth_users(email, password)
                if user:
                    if user['Employee Role'].lower() == 'admin':
                        print(colored("\n\nWelcome Admin 🩵\n\n", 'green', attrs=['bold']))
                        menuAdmin()
                    else:
                        print(colored("\n\nWelcome IT💻\n\n", 'green', attrs=['bold']))
                        menuIT()
                else:
                    print(colored("Invalid username or password, please try again.", 'red', attrs=['bold']))
            elif optionsChoice.startswith("2"):
                users = Users()
                users.reg_new_users()
            elif optionsChoice.startswith("3"):
                print(colored("\nThanks for using Mr.IT System 🩵 \n stay safe, see you soon 👋", 'blue', attrs=['bold']))
                break
            else:
                print(colored("Invalid choice, please try again ", 'red', attrs=['bold']))
    except Exception as e:
        print(f"Oops! Error in main: {str(e)}")

if __name__ == "__main__":
    main()

