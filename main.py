import csv
from data.code.qrcode import generate_qr_code
from data.pdf.pdf import create_qr_code_and_pdf
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
from data.assets import AddAssets


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



def user_manager_menu(self):
        """
        Displays the user manager menu.
        """
        user_menu = [
            "1. Add Assets",
            "2. Display Data in Table",
            "3. Display Data in Graph",
            "4. Display Data in Pie Chart",
            "5. Genrate Pdf File For Assets",
            "6. Exit"
            
        ]
                
        quitting = False

        quitting = False  # Corrected spelling

        while quitting == False:  # More Pythonic way to write `while quitting == False:`
            terminal_menu1 = TerminalMenu(user_menu,clear_screen= True)
            choice_index1 = terminal_menu1.show()

            print(colored("\n===== Data Analysis Dashboard =====", 'blue', attrs=['bold']))
            
            if choice_index1 == 0:
                print(colored("Exiting the user manager menu...", 'red', attrs=['bold']))
                quitting = True  
            elif choice_index1 == 1:
                self.delete_user()
            elif choice_index1 == 2:
                self.get_users()
            elif choice_index1 == 3:
                self.find_user()
            elif choice_index1 == 4:
                self.reg_new_admin()# Properly set quitting to True to exit the loop
            else:
                print(colored("Invalid choice! Please enter a valid option.", 'yellow', attrs=['bold']))
def menuUser():
    options = [
        "1. View Profile",
        "2. Update Profile",
        "3. Delete Account",
        "4. View Assets",
        "5. Request Support",
        "6. Exit"
    ]

    main_menu = TerminalMenu(options)
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
            update_profile()
        elif optionsChoice.startswith("3"):
            delete_account()
        elif optionsChoice.startswith("4"):
            view_assets()
        elif optionsChoice.startswith("5"):
            request_support()

def view_profile():
    print(colored("Profile Details:", 'blue', attrs=['bold']))
    # Implementation to view user profile

def update_profile():
    print(colored("Update Profile:", 'blue', attrs=['bold']))
    # Implementation to update user profile

def delete_account():
    confirmation = input(colored("Are you sure you want to delete your account? (yes/no): ", 'red', attrs=['bold']))
    if confirmation.lower() == 'yes':
        # Implementation to delete user account
        print(colored("Your account has been successfully deleted.", 'green', attrs=['bold']))

def view_assets():
    print(colored("Your Assets:", 'blue', attrs=['bold']))
    # Implementation to view user assets

def request_support():
    print(colored("Requesting Support:", 'blue', attrs=['bold']))
    # Implementation to request support


def menuAdmin():
    options = [
        "1. Mr.IT chat 🤖",
        "2. Dashboard 📊",
        "3. User Managers",
        "4. Assets",
        "5. Exit "
    ]

    main_menu = TerminalMenu(options,title="Assets Management Menu",
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
        mainMenu = TerminalMenu(options,title="Assets Management Menu",
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
            print(colored("\n\nWelcome to Mr.IT Registration Page 🩵\n", 'blue', attrs=['bold']))
            if optionsChoice.startswith("1"):
                email = input(colored('Enter your email: ', 'green', attrs=['bold'])).lower()
                password = input(colored('Enter your password: ', 'green', attrs=['bold'])).lower()
                user = employees.auth_users(email, password)
                if user:
                    if user['Employee Role'].upper() == 'ADMIN':
                        print(colored("Welcome Admin 🩵", 'green', attrs=['bold']))
                        menuAdmin()
                    else:
                        print(colored("Welcome User 🩵", 'green', attrs=['bold']))
                        menuUser()
                else:
                    print(colored("Invalid username or password, please try again.", 'red', attrs=['bold']))
            elif optionsChoice.startswith("2"):
                employees.reg_new_users()
            elif optionsChoice.startswith("3"):
                print(colored("Thanks for using Mr.IT System 🩵 \n stay safe, see you soon 👋", 'blue', attrs=['bold']))
                break
            else:
                print(colored("Invalid choice, please try again ", 'red', attrs=['bold']))
    except Exception as e:
        print(f"Oops! Error in main: {str(e)}")

if __name__ == "__main__":
    main()
