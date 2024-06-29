import random as rd
import string
import pandas as pd
import csv
from termcolor import colored

class Employees:
    def __init__(self):
        self.users = []

    def get_users(self):
        try:
            with open('data/users.csv', 'r') as file:
                reader = csv.reader(file)
                df = pd.DataFrame(reader)
                print(colored(df, 'green', attrs=['bold'])) 
        except FileNotFoundError:
            print(colored("No users found!", 'red', attrs=['bold'])) 

    def add_user(self, name, gender, email, password, passwordConfirm, role):
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
        try:
            with open('data/users.csv', 'r') as f:
                first_char = f.read(1)
                return bool(first_char)
        except FileNotFoundError:
            print(colored("The file was not found!", 'red', attrs=['bold'])) 
            return False

class Employee:
    def __init__(self, name, gender, email, password, passwordConfirm, role, userId):
        self.name = name
        self.gender = gender
        self.email = email
        self.password = password
        self.passwordConfirm = passwordConfirm
        self.role = role
        self.userId = userId
