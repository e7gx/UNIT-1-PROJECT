import csv
import random as rd
import re
import string
import pandas as pd
from termcolor import colored
from simple_term_menu import TerminalMenu
import getpass
import getpass

class Employees:
    class UserManager:
        def __init__(self):
            self.users = []

    def __init__(self):
        self.user_manager = self.UserManager()


    def get_users(self):
        """
        Retrieves and displays the list of users from the 'data/users.csv' file.
        """
        try:
            with open('data/users.csv', 'r') as file:
                reader = csv.reader(file)
                df = pd.DataFrame(reader)
                print(colored(df, 'green', attrs=['bold'])) 
        except FileNotFoundError:
            print(colored("No users found!", 'red', attrs=['bold'])) 

    def add_user(self, name:str, gender:str, email:str, password:str, passwordConfirm:str, role:str):
        """
        Adds a new user to the 'data/users.csv' file.

        Args:
            name (str): The name of the employee.
            gender (str): The gender of the employee.
            email (str): The email of the employee.
            password (str): The password of the employee.
            passwordConfirm (str): The confirmation password of the employee.
            role (str): The role of the employee.

        Returns:
            None
        """
        if self.email_exists(email):
            print(colored("This email already exists. Please use a different email.", 'red', attrs=['bold']))
            return

        userId = "".join(rd.choices(string.digits, k=10))  # Generate a 10-digit user ID 
        user = Employee(name, gender, email, password, passwordConfirm, role, userId)
        self.user_manager.users.append(user)

        # Check if the file exists and is not empty to avoid appending the header row again
        header_needed = not self.check_if_file_exists()
        # Open the file in append mode or create it if it doesn't exist
        with open('data/users.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            # Write the header row if needed
            if header_needed:
                writer.writerow(['Employee Name', 'Employee Gender', 'Employee Email', 'Employee Password', 'Employee Role', 'Employee ID'])
            
            writer.writerow([name, gender, email, password, role, userId])
        print(colored(f"Welcome To Mr.IT System {name}", 'green', attrs=['bold']))
        print(colored(f"The User {name} has been added successfully with the ID {userId} And his role is {role}\n and all records inserted successfully!", 'green', attrs=['bold']))

    def delete_user(self, identifier):
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
                print(colored("No users found!", 'red', attrs=['bold']))
                return
            
            # Remove header
            header = users.pop(0)

            # Find the user to delete by ID or name
            deleted = False
            for user in users:
                if len(user) == 6 and (user[0] == identifier or user[-1] == identifier):
                    users.remove(user)
                    deleted = True
                    break

            # Rewrite the file with the updated users
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

    def check_if_file_exists(self):
        """
        Checks if the 'data/users.csv' file exists and is not empty.

        Returns:
            bool: True if the file exists and is not empty, False otherwise.
        """
        try:
            with open('data/users.csv', 'r') as f:
                first_char = f.read(1)
                return bool(first_char)
        except FileNotFoundError:
            return False





    def email_exists(self, email:str):
        """
        Checks if an email already exists in the 'data/users.csv' file.

        Args:
            email (str): The email to check.

        Returns:
            bool: True if the email exists, False otherwise.
        """
        
        
        try:
            with open('data/users.csv', 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['Employee Email'].lower() == email.lower():
                        return True
        except FileNotFoundError:
            return False
        return False



    def auth_users(self, email:str, password:str):
        """
        Finds a user in the 'data/users.csv' file by email and password.

        Args:
            email (str): The email of the employee.
            password (str): The password of the employee.

        Returns:
            dict: The user data if found, None otherwise.
        """
        try:
            with open('data/users.csv', 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['Employee Email'].lower() == email.lower() and row['Employee Password'] == password:
                        return row
        except FileNotFoundError:
            print(colored("No users found!", 'red', attrs=['bold'])) 
        return None
    
    
    
    
    def find_user(self,userId:int):
        """
        Finds a user in the 'data/users.csv' file by email and userId.

        Args:
            email (str): The email of the employee.
            userId (str): The ID of the employee.

        Returns:
            dict: The user data if found, None otherwise.
        """
        try:
            with open('data/users.csv', 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['Employee ID'] == userId:
                       print(colored(f"{row['Employee Name']} information:\n Employee Name: {row['Employee Name']} \n Employee Email: {row['Employee Email']} \n Employee ID: {row['Employee ID']}\n Employee Role: {row['Employee Role']}\n Employee Gender: {row['Employee Gender']}",'light_green', attrs=['bold']))
                       break
        except FileNotFoundError:
            print(colored("No users found!", 'red', attrs=['bold'])) 
        return None
    
    
    
    
    
    def reg_new_admin(self):
        '''
        Method to register a new admin/IT/USER only by the admin.
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
                            break  # Breaks the loop if password matches and is at least 8 characters long
                        else:
                            if password != passwordConfirm:
                                print(colored('Passwords do not match. Please try again.', 'red', attrs=['bold']))
                            if len(password) < 8:
                                print(colored('Password is less than 8 characters. Please try again.', 'red', attrs=['bold']))
                    roles = ['it', 'admin']
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
                            admin_password_input = getpass.getpass(colored(f'Enter the Admin Password (Attempt {attempts}): \n','green', attrs=['bold']))
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
                        it_password_input = getpass.getpass(colored('Enter the IT Password: ','green', attrs=['bold']))
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
                    break
                else:
                    print(colored("You must enter a valid choice", 'red', attrs=['bold']))
        except Exception as e:
            print(f"Error in reg_new_admin: {str(e)}")
            
            
    def user_manager_menu(self):
        """
        Displays the user manager menu.
        """
        user_manager_menu = [
            "1. Add User            📇",
            "2. Delete User         👋",
            "3. Display All Users   📊",
            "4. Find User           🔍",
            "5. Exit                🚪"
        ]
    
        quitting = False

        while not quitting:
            terminal_menu1 = TerminalMenu(user_manager_menu,menu_cursor="-> ",
                menu_cursor_style=("bg_red", "fg_yellow"),
                menu_highlight_style=("bg_green", "fg_yellow"),

                cycle_cursor=True,)
            choice_index1 = terminal_menu1.show()

            print(colored("\n<=========== User Manager Menu ===========>", 'blue', attrs=['bold']))
            
            if choice_index1 == 4:
                print(colored("Exiting the user manager menu...", 'red', attrs=['bold']))
                quitting = True  
            elif choice_index1 == 0:
                self.reg_new_admin()
            elif choice_index1 == 1:
                identifier = input(colored("Enter user ID or name to delete: ", 'red', attrs=['bold']))
                self.delete_user(identifier)
            elif choice_index1 == 2:
                self.get_users()
            elif choice_index1 == 3:
                userId = input(colored("Enter Employee ID: ", 'blue', attrs=['bold']))
                user = self.find_user(userId)
                if user:
                    print(colored(f"User found: {user}", 'green', attrs=['bold']))
                else:
                    print(colored("User not found.", 'red', attrs=['bold']))
            else:
                print(colored("Invalid choice! Please enter a valid option.", 'yellow', attrs=['bold']))

class Employee:
    """
    Represents an employee in the system.

    Attributes:
        name (str): The name of the employee.
        gender (str): The gender of the employee.
        email (str): The email address of the employee.
        password (str): The password of the employee.
        passwordConfirm (str): The confirmation password of the employee.
        role (str): The role of the employee.
        userId (int): The unique identifier of the employee.
    """

    def __init__(self, name:str, gender:str, email:str, password:str, passwordConfirm:str, role:str, userId:int):
        self.name = name
        self.gender = gender
        self.email = email
        self.password = password
        self.passwordConfirm = passwordConfirm
        self.role = role
        self.userId = userId

if __name__ == "__main__":
    employee_manager = Employees()
    employee_manager.user_manager_menu()
