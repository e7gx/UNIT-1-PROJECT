import csv
from termcolor import colored

class AddAssets:
    def __init__(self, file:str):
        self.file = file

    def add_assets(self):
        header_needed = not self.file_exists()

        try:
            with open(self.file, 'a', newline='') as file:
                writer = csv.writer(file)
                if header_needed:
                    writer.writerow(['Asset ID', 'Asset Type', 'Brand', 'Model', 'Serial Number', 'Operating System', 'Processor', 'RAM', 'Storage', 'Purchase Date', 'Warranty Information', 'Assigned To', 'Location', 'Cost', 'Depreciation'])
                
                assets_number = int(input('How many assets do you want to insert 🤔: '))
                for i in range(assets_number):
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

        except Exception as e:
            print(f"An error in add_assets funcation class AddAssets : {str(e)}")

    def file_exists(self):
        try:
            with open(self.file, 'r') as f:
                first_char = f.read(1)
                return bool(first_char)
        except FileNotFoundError:
            return False
