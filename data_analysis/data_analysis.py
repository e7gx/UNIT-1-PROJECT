import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from colorama import Fore, Back, Style
from termcolor import colored
from art import *
import colorama
from colorama import Fore

from data.code.qrcode import generate_qr_code

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

    def display_data_in_graph(self):
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
