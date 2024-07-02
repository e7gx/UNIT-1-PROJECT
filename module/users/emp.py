import getpass
import re
from termcolor import colored
from module.users.users_manger import Employees
from simple_term_menu import TerminalMenu

class Users(Employees):
    def __init__(self):
        super().__init__()

    def reg_new_users(self):
        '''
        Method to register a new user with user roles.
        Prompts for name, email, password, role, and validates input.
        '''
        while True:
            print(colored("TO Go Back Type Exit 🚪", 'green', attrs=['bold']))
            user_input = input(colored('Do you agree to the terms and conditions? (yes/no): \n','light_green',attrs=['bold'])).lower()
            if user_input == 'yes':
                name = input(colored('Enter your name: ', 'blue')).lower()
                email = input(colored('Enter your email: ', 'blue'))
                while not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
                    print(colored('Invalid email format. Please try again.','red', attrs=['bold']))
                    email = input(colored('Enter your email: ', 'blue'))
                email = email.lower()
                password = getpass.getpass(colored('Enter your password: ', 'blue')).lower()
                passwordConfirm = getpass.getpass(colored('Confirm your password: ', 'blue')).lower()
                while password != passwordConfirm or len(password) < 8:
                    if password != passwordConfirm:
                        print(colored('Passwords do not match. Please try again.','red', attrs=['bold']))
                    elif len(password) < 8:
                        print(colored('Passwords are less than 8 characters. Please try again.','red', attrs=['bold']))
                    password = getpass.getpass('Enter your password: ').lower()
                    passwordConfirm = getpass.getpass('Confirm your password: ').lower()
                gender = input(colored('Enter your gender (male/female): ', 'blue')).lower()
                while gender not in ['male', 'female']:
                    print(colored('Invalid gender. Please try again.','red', attrs=['bold']))
                    gender = input(colored('Enter your gender (male/female): ', 'blue')).lower()
                
                roles = ['it']
                while True:
                    print('Select your role:')
                    for i, role in enumerate(roles):
                        print(f'{i+1}. {role}')
                    role_choice = input('Enter the number corresponding to your role: ')
                    if role_choice.isdigit() and int(role_choice) in range(1, len(roles)+1):
                        role = roles[int(role_choice)-1]
                        break
                    else:
                        print('Invalid choice. Please enter a valid number.')
                if role.lower() == 'it':
                    it_password = '12345'
                    attempts = 0
                    while attempts < 3:
                        it_password_input = input('Enter the IT password: ')
                        if it_password_input == it_password:
                            self.add_user(name, gender, email, password, passwordConfirm, role)
                            exit()
                        else:
                            attempts += 1
                            print(colored(f'Incorrect IT Password. You have {3 - attempts} attempts left.','red', attrs=['bold']))
                    else:
                        print('Maximum number of attempts reached. Exiting...')
                else:
                    print(colored('You have selected the role of a user.','light_yellow', attrs=['bold']))

            elif user_input == 'no':
                print(colored("You must agree to the terms and conditions to continue", 'red', attrs=['bold']))
            elif user_input == 'exit':
                print(colored("Thanks for using Mr.IT System 🩵 \n stay safe, see you soon 👋", 'blue', attrs=['bold']))
                exit()
            else:
                print(colored("You must enter a valid choice", 'red', attrs=['bold']))

    def reg_new_admin(self):
        '''
        Method to register a new admin/IT only by the admin.
        '''
        try:
            while True:
                print(colored("TO Go Back Type Exit 🚪", 'green', attrs=['bold']))
                user_input = input(colored('Do you agree to the terms and conditions? (yes/no): \n','light_green')).lower()
                if user_input == 'yes':
                    name = input('Enter your name: ').lower()
                    gender = input('Enter your gender: ').lower()
                    email = input('Enter your email: ').lower()
                    while not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
                        print(colored('Invalid email format. Please try again.','red', attrs=['bold']))
                        email = input('Enter your email: ').lower()
                   # Password input and validation loop
                    while True:
                        password = getpass.getpass('Enter your password: ').lower()
                        passwordConfirm = getpass.getpass('Confirm your password: ').lower()
                        if password == passwordConfirm and len(password) >= 8:
                            break  # Breaks out of the loop if password matches and is at least 8 characters long
                        else:
                            if password != passwordConfirm:
                                print(colored('Passwords do not match. Please try again.', 'red', attrs=['bold']))
                            if len(password) < 8:
                                print(colored('Password is less than 8 characters. Please try again.', 'red', attrs=['bold']))
                    roles = ['IT', 'ADMIN']
                    while True:
                        print('Select your role:')
                        for i, role in enumerate(roles):
                            print(f'{i+1}. {role}')
                        role_choice = input('Enter the number corresponding to your role: ')
                        if role_choice.isdigit() and int(role_choice) in range(1, len(roles) + 1):
                            role = roles[int(role_choice) - 1]
                            print(f'You have selected {role}')
                            break
                        else:
                            print(colored('Invalid choice. Please enter a valid number.', 'red', attrs=['bold']))

                    if role.lower() == 'admin':
                        admin_password = '1234554321'
                        attempts = 0
                        for _ in range(3):
                            attempts += 1
                            admin_password_input = input(colored(f'Enter the Admin Password (Attempt {attempts}): \n','green', attrs=['bold']))
                            if admin_password_input == admin_password:
                                self.add_user(name, gender, email, password, passwordConfirm, role)
                                break
                            elif admin_password_input.lower() == 'exit':
                                print(colored("Thanks for using Mr.IT System 🩵 \n stay safe, see you soon 👋", 'blue', attrs=['bold']))
                                exit()
                            else:
                                print(colored('Incorrect ADMIN Password.','red', attrs=['bold']))
                        else:
                            print(colored(f'Incorrect IT Password. You have {3 - attempts} attempts left.','red', attrs=['bold']))
                    elif role.lower() == 'it':
                        it_password = '1234554321'
                        it_password_input = input(colored('Enter the IT Password: ','green', attrs=['bold']))
                        if it_password_input == it_password:
                            self.add_user(name, gender, email, password, passwordConfirm, role)
                            break
                        elif it_password_input.lower() == 'exit':
                            print(colored("Thanks for using Mr.IT System 🩵 \n stay safe, see you soon 👋", 'blue', attrs=['bold']))
                            exit()
                        else:
                            print(colored('Incorrect IT Password\n','red', attrs=['bold']))
                    else:
                        self.add_user(name, gender, email, password, passwordConfirm, role)
                        break
                elif user_input == 'no':
                    print(colored("You must agree to the terms and conditions to continue", 'red', attrs=['bold']))
                    break
                elif user_input == 'exit':
                    print(colored("Thanks for using Mr.IT System 🩵 \n stay safe, see you soon 👋", 'blue', attrs=['bold']))
                    exit()
                else:
                    print(colored("You must enter a valid choice", 'red', attrs=['bold']))
        except Exception as e:
            print(f"Error in reg_new_admin: {str(e)}")