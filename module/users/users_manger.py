import csv
import random as rd
import string
import pandas as pd
from termcolor import colored
from simple_term_menu import TerminalMenu

class Employees:
    def __init__(self):
        self.users = []

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

    def add_user(self, name, gender, email, password, passwordConfirm, role):
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
        self.users.append(user)

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
                print(colored(f"User with ID or name '{identifier}' has been deleted successfully.", 'green', attrs=['bold']))
            else:
                print(colored(f"No user found with ID or name '{identifier}'.", 'red', attrs=['bold']))
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

    def email_exists(self, email):
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

    def auth_users(self, email, password):
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
    
    def find_user(self,userId):
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
                        return row
        except FileNotFoundError:
            print(colored("No users found!", 'red', attrs=['bold'])) 
        return None

    def user_manager_menu(self):
        """
        Displays the user manager menu.
        """
        user_manager_menu = [
            "1. Add User",
            "2. Delete User",
            "3. Display All Users",
            "4. Find User",
            "5. Exit"
        ]
    
        quitting = False

        while not quitting:
            terminal_menu1 = TerminalMenu(user_manager_menu)
            choice_index1 = terminal_menu1.show()

            print(colored("\n===== User Manager Menu =====", 'blue', attrs=['bold']))
            
            if choice_index1 == 4:
                print(colored("Exiting the user manager menu...", 'red', attrs=['bold']))
                quitting = True  
            elif choice_index1 == 0:
                name = input("Enter name: ")
                gender = input("Enter gender: ")
                email = input("Enter email: ")
                password = input("Enter password: ")
                passwordConfirm = input("Confirm password: ")
                role = input("Enter role: ")
                self.add_user(name, gender, email, password, passwordConfirm, role)
            elif choice_index1 == 1:
                identifier = input("Enter user ID or name to delete: ")
                self.delete_user(identifier)
            elif choice_index1 == 2:
                self.get_users()
            elif choice_index1 == 3:
                userId = input("Enter Employee ID: ")
                user = self.find_user(userId)
                if user:
                    print(colored(f"User found: {user}", 'green', attrs=['bold']))
                else:
                    print(colored("User not found.", 'red', attrs=['bold']))
            else:
                print(colored("Invalid choice! Please enter a valid option.", 'yellow', attrs=['bold']))

class Employee:
    def __init__(self, name, gender, email, password, passwordConfirm, role, userId):
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
