import csv

from termcolor import colored

from data.code.qrcode import generate_qr_code


class AddAssets:
    def __init__(self, file:str):
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