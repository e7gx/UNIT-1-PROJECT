import re
from termcolor import colored
from module.users.users_manger import Employees
from simple_term_menu import TerminalMenu




class Users(Employees):
    def __init__(self):
        super().__init__()

    def reg_new_users(self):
        '''
        This method is used to register a new user with only user roles.
        
        The method prompts the user to enter their information, including name, email, password, and role.
        It validates the user's input and adds the user to the system if all conditions are met.
        If the selected role is 'IT', the method prompts for an admin password to authorize the user creation.
        '''
        while True:
            print(colored("TO Go Back Type Exit 🚪", 'green', attrs=['bold']))
            user_input = input(colored('Do you agree to the terms and conditions? (yes/no): \n','light_green',attrs=['bold'])).lower()
            if user_input == 'yes':
                name = input('Enter your name: ').lower()
                email = input('Enter your email: ')
                while not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
                    print(colored('Invalid email format. Please try again.','red', attrs=['bold']))
                    email = input('Enter your email: ')
                email = email.lower()
                password = input('Enter your password: ').lower()
                passwordConfirm = input('Confirm your password: ').lower()
                while password != passwordConfirm or len(password) < 8:
                    if password != passwordConfirm:
                        print(colored('Passwords do not match. Please try again.','red', attrs=['bold']))
                    elif len(password) < 8:
                        print(colored('Passwords are less than 8 characters. Please try again.','red', attrs=['bold']))
                    password = input('Enter your password: ').lower()
                    passwordConfirm = input('Confirm your password: ').lower()
                gender = input('Enter your gender: ').lower()
                
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
                                self.add_user(name, gender, email, password, passwordConfirm, role)
                                exit()
                            else:
                                attempts += 1
                                print(colored(f'Incorrect IT Password. You have {3 - attempts} attempts left.','red', attrs=['bold']))
                        else:
                            print('Maximum number of attempts reached. Exiting...')
                            break
                    else:
                        print(colored('You have selected the role of a user.','light_yellow', attrs=['bold']))
                        break
            elif user_input == 'no':
                print(colored("You must agree to the terms and conditions to continue", 'red', attrs=['bold']))
            elif user_input == 'exit':
                print(colored("Thanks for using Mr.IT System 🩵 \n stay safe, see you soon 👋", 'blue', attrs=['bold']))
                exit()
            else:
                print(colored("You must enter a valid choice", 'red', attrs=['bold']))

    def reg_new_admin(self):
        '''
        This method is used to register a new admin/IT/USER only by the admin.
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
                        password = input('Enter your password: ').lower()
                        passwordConfirm = input('Confirm your password: ').lower()
                        if password == passwordConfirm and len(password) >= 8:
                            break  # Breaks out of the loop if password matches and is at least 8 characters long
                        else:
                            if password != passwordConfirm:
                                print(colored('Passwords do not match. Please try again.', 'red', attrs=['bold']))
                            if len(password) < 8:
                                print(colored('Password is less than 8 characters. Please try again.', 'red', attrs=['bold']))
                    roles = ['USER', 'IT', 'ADMIN']
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
            

    # def user_manager_menu(self):
        
    #     user_manager_menu = [
    #             "1. Add User 👨🏻‍💻",
    #             "2. Delete User 🙅🏻‍♂️",
    #             "3. Display All Users 👀",
    #             "4. Find User 🔍",
    #             "5. Exit 🚪"
    #         ]
    
    #     quitting = False  # Corrected spelling

    #     while quitting == False:  # More Pythonic way to write `while quitting == False:`
    #         terminal_menu1 = TerminalMenu(user_manager_menu,clear_screen= True)
    #         choice_index1 = terminal_menu1.show()

    #         print(colored("\n===== Data Analysis Dashboard =====", 'blue', attrs=['bold']))
            
    #         if choice_index1 == 0:
    #             print(colored("Exiting the user manager menu...", 'red', attrs=['bold']))
    #             quitting = True  
    #         elif choice_index1 == 1:
    #             self.delete_user()
    #         elif choice_index1 == 2:
    #             self.get_users()
    #         elif choice_index1 == 3:
    #             self.find_user()
    #         elif choice_index1 == 4:
    #             self.reg_new_admin()# Properly set quitting to True to exit the loop
    #         else:
    #             print(colored("Invalid choice! Please enter a valid option.", 'yellow', attrs=['bold']))