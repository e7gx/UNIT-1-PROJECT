from ast import main
from termcolor import colored
from module.users.users_manger import Employees
import re

class Users(Employees):
    def __init__(self):
        super().__init__()


    def reg_new_users(self):
        while True:
            
            '''
            This method is used to register a new user with only user roles.
            
            The method prompts the user to enter their information, including name, email, password, and role.
            It validates the user's input and adds the user to the system if all conditions are met.
            If the selected role is 'IT', the method prompts for an admin password to authorize the user creation.
            
            Returns:
                None
            
            Raises:
                None            
        
            '''
            # colored("Please enter your information to create an account", 'green', attrs=['bold']))
            # if input('Do you want to SignUp ? (y/n): ').lower() == 'n':
            print(colored("TO Go Back Type Exit 🚪", 'green', attrs=['bold']))
            user_input = input(colored('Do you agree on conditional terms? (yes/no): \n','light_green',attrs=['bold'])).lower()
            if user_input.lower() == 'yes':
                name = input(str('Enter your name: ')).lower()
                email = input('Enter your email: ')
                while not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
                    print(colored('Invalid email format. Please try again.','red', attrs=['bold']))
                    email = input('Enter your email: ')
                email = email.lower()
                password = input(str('Enter your password: ')).lower()
                passwordConfirm = input(str('Confirm your password: ')).lower()
                while password != passwordConfirm or len(password) < 8:
                    
                    if password != passwordConfirm:
                        print(colored('Passwords do not match. Please try again.','red', attrs=['bold']))
                        
                    elif len(password) < 8:
                        print(colored('Passwords are less than 8 characters. Please try again.','red', attrs=['bold']))
                        
                    # print(colored('Passwords do not match or are less than 8 characters. Please try again.','red', attrs=['bold']))
                    password = input(str('Enter your password: ')).lower()
                    passwordConfirm = input(str('Confirm your password: ')).lower()
                gender = input(str('Enter your gender: ')).lower()
            
                
                roles = ['user','IT']
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
                while True:
                    if role.lower() == 'it':
                        it_password = '12345'
                        attempts = 0
                        while attempts < 3:
                            it_password_input = input('Enter the IT password: ')
                            if it_password_input == it_password:
                                self.add_user(name,gender, email, password, passwordConfirm, role)
                                exit()
                            else:
                                attempts += 1
                                print(colored(f'Incorrect IT Password You Only Have 3 attempts  3 / {attempts}','red', attrs=['bold']))
                        else:
                            print('Maximum number of attempts reached. Exiting...')
                            break
                    else:
                        print(colored('You have selected the role of a user.','light_yellow', attrs=['bold']))
                        break
            elif user_input.lower() == 'no':
                print(colored("You must agree on the terms to continue", 'red', attrs=['bold']))
                
            elif user_input.lower() == 'exit':
                    print(colored("Thanks for using Mr.IT System 🩵 \n stay safe, see you soon 👋", 'blue', attrs=['bold']))
                    exit()
            else:
                print(colored("You Must Enter A Valid Choice", 'red', attrs=['bold']))
               
        
        
    def reg_new_admin(self):
        '''
        This method is used to register a new admin/IT/USER only by the admin
        '''
        
        try:
            while True:
                print(colored("TO Go Back Type Exit 🚪", 'green', attrs=['bold']))
                user_input = input(colored('Do you agree on conditional terms📝 ? (yes/no): \n','light_green')).lower()
                if user_input.lower() == 'yes':
                    name = input('Enter your name: ').lower()
                    gender = input(str('Enter your gender: ')).lower()
                    email = input('Enter your email: ').lower()
                    while not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
                        print(colored('Invalid email format. Please try again.','red', attrs=['bold']))
                        email = input('Enter your email: ').lower()
                    password = input(str('Enter your password: ')).lower()
                    passwordConfirm = input(str('Confirm your password: ')).lower()
                    while password != passwordConfirm or len(password) < 8:
                        
                        if password != passwordConfirm:
                            print(colored('Passwords do not match. Please try again.','red', attrs=['bold']))
                            
                        elif len(password) < 8:
                            print(colored('Passwords are less than 8 characters. Please try again.','red', attrs=['bold']))
                        
                    # print(colored('Passwords do not match or are less than 8 characters. Please try again.','red', attrs=['bold']))


                    roles = ['USER', 'IT', 'ADMIN']
                    while True:
                        print('Select your role:')
                        for i, role in enumerate(roles):
                            print(f'{i+1}. {role}')
                        role_choice = input('choice your role: ')
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
                                self.add_user(name,gender, email, password, passwordConfirm, role)
                                break
                            elif admin_password_input.lower() == 'exit':
                                print(colored("Thanks for using Mr.IT System 🩵 \n stay safe, see you soon 👋", 'blue', attrs=['bold']))
                                exit()
                            else:
                                print(colored('Incorrect ADMIN Password.','red', attrs=['bold']))
                        else:
                                print(colored(f'Incorrect IT Password You Only Have 3 attempts  3 / {attempts}','red', attrs=['bold']))


                    elif role.lower() == 'it':
                        it_password = '1234554321'
                        it_password_input = input(colored('Enter the IT Password: ','green', attrs=['bold']))
                        if it_password_input == it_password:
                            self.add_user(name, gender,email, password, passwordConfirm, role)
                            break
                        elif it_password_input.lower() == 'exit':
                            print(colored("Thanks for using Mr.IT System 🩵 \n stay safe, see you soon 👋", 'blue', attrs=['bold']))
                            exit()
                        else:
                            print(colored('Incorrect IT Password\n','red', attrs=['bold']))
                    else:
                        self.add_user(name,gender, email, password, passwordConfirm, role)
                        break
                elif user_input.lower() == 'no':
                    print(colored("You must agree on the terms to continue", 'red', attrs=['bold']))
                    break

                elif user_input.lower() == 'exit'or user_input.lower() == 'exit':
                    exit = exit()
                    exit = input(colored("Thanks for using Mr.IT System 🩵 \n stay safe, see you soon 👋", 'blue', attrs=['bold']))

                else:
                    print(colored("You Must Enter A Valid Choice", 'red', attrs=['bold']))
        except Exception as e:
            print(f"Opss Error in reg_new_admin check it out: {str(e)}")
