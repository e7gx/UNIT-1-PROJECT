import csv
from data.code.qrcode import generate_qr_code
from data.pdf.pdf import create_qr_code_and_pdf
from module.users.emp import Users
from module.users.users_manger import Employees as EMP
from data_analysis.data_analysis import DataAnalysis as DA
from data.data import AddAssets as Assets
from module.chat.chat import chatgpt_chat
from termcolor import colored
from art import *
import colorama

colorama.init()


emp_manager = EMP()
data_analysis = DA()
users = Users()
assets = Assets('data/devices.csv')

tprint("Mr.IT", font="block")


def menuUser():
    """
    Displays the menu options for the user and performs the corresponding actions based on user input.
    """
    while True:
        print("\nMenu:")
        print("1. Add Assets")
        print("2. Display Data in Table")
        print("3. Display Data in Graph")
        print("4. Add User")
        print("5. Exit\n")
        
        user_input = input("Please choose from the menu (1-5): ").strip()

        if user_input == '1':
            assets.add_assets()
        elif user_input == '2':
            data_analysis.display_data_in_table()
        elif user_input == '3' or 'display data in graph' in user_input.lower():
            data_analysis.display_data_in_graph()
        elif user_input == '4' or 'add user' in user_input.lower():
            users.reg_new_users()
        elif user_input == '5' or user_input.lower() == 'exit':
            print(colored("Thanks for using MR.IT System 🩵\nStay safe, see you soon! 👋", 'blue', attrs=['bold']))
            break
        else:
            print("Invalid choice, please try again.")


def menuAdmin():
    """
    Displays the menu options for the admin and performs the corresponding actions based on admin input.
    """
    try:
        while True:
            print(colored("\n<-----------------💻Mr.IT SERVICES💻----------------->\n", 'green', attrs=['bold']))
            print(colored("1. Add Assets\n", 'yellow', attrs=['bold']))
            print(colored("2. Delete User\n", 'red', attrs=['bold']))
            print(colored("3. Display Data in Table\n", 'blue', attrs=['bold']))
            print(colored('4. Display the data in Pie Chart\n', 'magenta', attrs=['bold']))
            print(colored('5. Display Data in Graph\n', 'green', attrs=['bold']))
            print(colored('6. Add User\n', 'cyan', attrs=['bold']))
            print(colored('7. Display All Users\n', 'magenta', attrs=['bold']))
            print(colored('8. Mr.IT chat 🤖\n', 'green', attrs=['bold']))
            print(colored('9. Display QrCode\n', 'green', attrs=['bold']))
            print(colored('10. Generate A PDF File\n', 'blue', attrs=['bold']))
            print(colored('11. Exit\n\n', 'red', attrs=['bold']))
            
            user_input = input(colored("Please choose from the menu [1-11]: ", 'yellow', attrs=['bold'])).strip()
            if user_input == '1':
                assets.add_assets()
                
            elif user_input == '2':
                identifier = input("Enter the user name or user ID to delete: ")
                emp_manager.delete_user(identifier)
                
            elif user_input == '3':
                data_analysis.display_data_in_table()
                
            elif user_input == '4' or 'display data in Pie' in user_input.lower():
                data_analysis.display_data_in_pie()

            elif user_input == '5' or 'display data in graph' in user_input.lower():
                data_analysis.display_data_in_graph()

            elif user_input == '6' or 'display all users' in user_input.lower():
                users.reg_new_admin()

            elif user_input == '7':
                emp_manager.get_users()
     
            elif user_input == '8':
                print(colored("Welcome to the Mr.IT chat 🤖\n\n","blue", attrs=['bold']))
                chatgpt_chat()
                
            elif user_input == '9':
                generate_qr_code()
            
            elif user_input == '10':
                create_qr_code_and_pdf()

                
            elif user_input == '11'  or user_input.lower() == 'exit' :
                print(colored("Thanks For Using Mr.IT System 🩵 \n Stay Safe, See You Soon 👋", 'blue', attrs=['bold'])) 
                break
    except Exception as e:
        print(f"Oops! Error in menuAdmin: {str(e)}")
        
        
def main():
    """
    The main function that handles the login and registration process for Mr.IT System.
    """
    try:
        employees = EMP()
        
        while True:
            print(colored("\n\nWelcome to Mr.IT Registration Page 🩵\n", 'blue', attrs=['bold']))
            login_sign_up = input(colored("For Login Press 1 🔑 \t\t\t For Sign up Press 2 🆕  \n\n", 'green', attrs=['bold'])).lower()
            if login_sign_up == '1':
                email = input('Enter your email: ')
                password = input('Enter your password: ')
                user = employees.find_user(email, password)
                if user:
                    if user['Employee Role'].upper() == 'ADMIN':
                        print(colored("Welcome Admin 🩵", 'green', attrs=['bold']))
                        menuAdmin()
                    else:
                        print(colored("Welcome User 🩵", 'green', attrs=['bold']))
                        menuUser()
                else:
                    print(colored("Invalid username or password, please try again.", 'red', attrs=['bold']))
            elif login_sign_up == '2':
                employees.reg_new_users()
            elif login_sign_up == 'exit':
                print(colored("Thanks for using Mr.IT System 🩵 \n stay safe, see you soon 👋", 'blue', attrs=['bold']))
                break
            else:
                print(colored("Invalid choice, please try again ", 'red', attrs=['bold']))
    except Exception as e:
        print(f"Oops! Error in main: {str(e)}")

if __name__ == "__main__":
    main()
