import csv
import matplotlib.pyplot as plt
import pandas as pd
from termcolor import colored
from art import *
import colorama
from  data.code.qrcode import generate_qr_code
from data.pdf.pdf import create_qr_code_and_pdf
from simple_term_menu import TerminalMenu
colorama.init()




class DataAnalysis:
    def __init__(self):
        self.file = 'data/devices.csv'
    def add_assets(self):
        try:
            with open(self.file, 'r') as f:
                first_char = f.read(1)
                if not first_char:
                    header_needed = True
                else:
                    header_needed = False
        except FileNotFoundError:
            header_needed = True

        # Open the file in append mode or create it if it doesn't exist
        with open(self.file, 'a', newline='') as file:
            writer = csv.writer(file)
            # Write the header row if needed
            if header_needed:
                writer.writerow(['Asset ID', 'Asset Type', 'Brand', 'Model', 'Serial Number', 'Operating System', 'Processor', 'RAM', 'Storage', 'Purchase Date', 'Warranty Information', 'Assigned To', 'Location', 'Cost', 'Depreciation'])
            
            n = int(input('How many assets do you want to insert 🤔: '))
            for i in range(n):
                print()
                asset_id = input(f'{i+1}. Enter Asset ID: ')
                asset_type = input(f'{i+1}. Enter Asset Type: ')
                brand = input(f'{i+1}. Enter Brand: ')
                model = input(f'{i+1}. Enter Model: ')
                serial_number = input(f'{i+1}. Enter Serial Number: ')
                operating_system = input(f'{i+1}. Enter Operating System: ')
                processor = input(f'{i+1}. Enter Processor: ')
                ram = input(f'{i+1}. Enter RAM: ')
                storage = input(f'{i+1}. Enter Storage: ')
                purchase_date = input(f'{i+1}. Enter Purchase Date (YYYY-MM-DD): ')
                warranty_info = input(f'{i+1}. Enter Warranty Information: ')
                assigned_to = input(f'{i+1}. Enter Assigned To: ')
                location = input(f'{i+1}. Enter Location: ')
                cost = input(f'{i+1}. Enter Cost: $')
                depreciation = input(f'{i+1}. Enter Depreciation: ')

                writer.writerow([asset_id, asset_type, brand, model, serial_number, operating_system, processor, ram, storage, purchase_date, warranty_info, assigned_to, location, cost, depreciation])
                print()
                print(colored("All records inserted successfully!", 'green', attrs=['bold']))
                generate_qr_code()

    def display_data_in_table(self):
        with open(self.file, 'r') as file:
            reader = csv.reader(file)
            df = pd.DataFrame(reader)
            print(colored(df, 'green', attrs=['bold']))


    def export_to_excel(self):
        try:
            with open(self.file, 'r') as excelfile:
                df = pd.read_csv(excelfile)
                excelfile = f'data/Exported/assets_{pd.Timestamp.now().strftime("%Y-%m-%d")}.csv'
                df.to_excel('data/Exported/assets.xlsx', index=False)
                print(colored("Data exported to 'data/Exported/assets.xlsx' successfully!", 'green', attrs=['bold']))
        except FileNotFoundError:
            print(colored("The file does not exist. Please add some data first.", 'red', attrs=['bold']))
            
    def export_to_csv(self):
        try:
            with open(self.file, 'r') as csvfile:
                df = pd.read_csv(csvfile)
                csv_file = f'data/Exported/assets_{pd.Timestamp.now().strftime("%Y-%m-%d_%H-%M-%S")}.csv'
                df.to_csv(csv_file, index=False)
                print(colored(f"Data exported to '{csv_file}' successfully!", 'green', attrs=['bold']))
        except FileNotFoundError:
            print(colored("The file does not exist. Please add some data first.", 'red', attrs=['bold']))

    def display_data_in_graph(self):
        """
        Displays a bar graph showing the number of assets per brand in the company.

        Reads data from a CSV file and counts the number of assets for each brand.
        Then, plots the data using matplotlib.

        Args:
            self (object): The current instance of the class.

        Returns:
            None
        """
        brand_count = {}

        with open(self.file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            next(plots, None)  # Skip the header row
            for row in plots:
                brand = row[2]  # Adjusted to the correct index for 'Brand'
                if brand in brand_count:
                    brand_count[brand] += 1
                else:
                    brand_count[brand] = 1

        # Prepare data for plotting
        brands = list(brand_count.keys())
        counts = list(brand_count.values())

        # Plotting
        plt.figure(figsize=(10, 6))  # Optional: Adjust figure size
        plt.bar(brands, counts, color='b', width=0.72, label="Number of Assets per Brand")
        plt.xlabel('Brands')
        plt.ylabel('Number of Assets')
        plt.title('Number of Assets per Brand In The Company')
        plt.xticks(rotation=45)  # Rotate brand names for better readability
        plt.legend()
        plt.tight_layout()  # Adjust layout to not cut off labels
        plt.show()


    def display_data_in_pie(self):
        brand_count = {}

        with open(self.file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            next(plots, None)  # Skip the header row
            for row in plots:
                brand = row[2]  # Adjusted to the correct index for 'Brand'
                if brand in brand_count:
                    brand_count[brand] += 1
                else:
                    brand_count[brand] = 1

        # Prepare data for plotting
        brands = list(brand_count.keys())
        counts = list(brand_count.values())

        # Plotting
        plt.figure(figsize=(10, 6))  # Optional: Adjust figure size
        plt.pie(counts, labels=brands, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
        plt.title('Distribution of Assets by Brand')
        plt.show()
        
    def display_users_gender(self):
        file = 'data/users.csv'
        gender_count = {}

        with open(file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            next(plots, None)  # Skip the header row
            for row in plots:
                gender = row[1]  # Adjusted to the correct index for 'Brand'
                if gender in gender_count:
                    gender_count[gender] += 1
                else:
                    gender_count[gender] = 1

        # Prepare data for plotting
        gender = list(gender_count.keys())
        counts = list(gender_count.values())

        # Plotting
        plt.figure(figsize=(10, 6))  # Optional: Adjust figure size
        plt.pie(counts, labels=gender, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
        plt.title('Distribution of males and Felames')
        plt.show()
        
        
    def display_users_role(self):
        file = 'data/users.csv'
        role_count = {}

        with open(file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            next(plots, None)  # Skip the header row
            for row in plots:
                role = row[4]  # Adjusted to the correct index for 'Brand'
                if role in role_count:
                    role_count[role] += 1
                else:
                    role_count[role] = 1

        # Prepare data for plotting
        brands = list(role_count.keys())
        counts = list(role_count.values())

        # Plotting
        plt.figure(figsize=(10, 6))  # Optional: Adjust figure size
        plt.pie(counts, labels=brands, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
        plt.title('Distribution of males and Felames')
        plt.show()
        
        
    def dashboard_menu(self):
        data_menu = [
            "1. Display Assets Table ",
            "2. Display Assets Graph  ",
            "3. Display Assets Pie Chart",
            "4. Display Gender Pie Chart",
            "5. Display Users Role Pie Chart",
            "6. Genrate Pdf File For Assets ",
            "7. Export Data to CSV",
            "8. Export Data to Excel",
            "9. Exit",
        ]
        quiting = False
        while quiting == False :
    
            print(colored("\n===== Data Analysis Dashboard =====", 'blue', attrs=['bold']))
            terminal_menu = TerminalMenu(data_menu,menu_cursor="-> ",
                menu_cursor_style=("bg_red", "fg_yellow"),
                menu_highlight_style=("bg_green", "fg_yellow"),
                cycle_cursor=True,)
            choice_index = terminal_menu.show()
            if choice_index == 0:
                self.display_data_in_table()
            elif choice_index == 1:
                self.display_data_in_graph()
            elif choice_index == 2:
                self.display_data_in_pie()
            elif choice_index == 3:
                self.display_users_gender()
            elif choice_index == 4:
                self.display_users_role()
            elif choice_index == 5:
                create_qr_code_and_pdf()
            elif choice_index == 6:
                self.export_to_csv()
            elif choice_index == 7:
                self.export_to_excel()
            elif choice_index == 8:
                 print(colored("Exiting the Data Analysis Dashboard...", 'red', attrs=['bold']))
                 break

            else:
                print(colored("Invalid choice! Please enter a valid option.", 'yellow', attrs=['bold']))
