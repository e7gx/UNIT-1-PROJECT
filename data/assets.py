import csv
import string
import tempfile
from termcolor import colored
from art import *
import colorama
from data.pdf.pdf import create_qr_code_and_pdf
from simple_term_menu import TerminalMenu
import shutil
import random as rd

colorama.init()

class AddAssets:
    def __init__(self, file: str):
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
                    asset_id = "".join(rd.choices(string.digits, k=10))
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
            print(f"An error in add_assets function class AddAssets: {str(e)}")

    def delete_asset(self, asset_id):
        """
        Deletes an asset from the CSV file based on the provided asset ID.

        Args:
            asset_id (str): The ID of the asset to be deleted.

        Returns:
            None
        """
        try:
            with open(self.file, 'r') as file:
                reader = csv.reader(file)
                assets = list(reader)

            if not assets or len(assets) == 1:
                print(colored("No assets found!", 'red', attrs=['bold']))
                return
            
            # Remove header
            header = assets.pop(0)

            # Find the asset to delete by ID
            deleted = False
            for asset in assets:
                if asset and asset[0] == asset_id:
                    assets.remove(asset)
                    deleted = True
                    break

            # Rewrite the file with the updated assets
            with open(self.file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(header)
                writer.writerows(assets)

            if deleted:
                print(colored(f"Asset with ID '{asset_id}' has been deleted successfully.", 'green', attrs=['bold']))
            else:
                print(colored(f"No asset found with ID '{asset_id}'.", 'red', attrs=['bold']))
        except FileNotFoundError:
            print(colored("The file was not found!", 'red', attrs=['bold']))
        except Exception as e:
            print(f"An error occurred while deleting the asset: {str(e)}")

    def file_exists(self):
        try:
            with open(self.file, 'r') as f:
                first_char = f.read(1)
                return bool(first_char)
        except FileNotFoundError:
            return False
        
        

    def search_for_asset(search_term):
        file_path = 'data/devices.csv'
        asset_found = False
        
        try:
                # Example usage
            search_term = input("Enter the asset name or ID to search for: ")
            with open(file_path, mode='r') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    # Assuming you're searching for an asset by its name or ID in the 'asset_name' column
                    if row['Asset ID'].lower() == search_term.lower():
                        print(f"Asset Found: {row}")
                        asset_found = True
                        break  # Exit the loop after finding the asset
                
                if not asset_found:
                    print("Asset not found.")
        
        except FileNotFoundError:
            print(f"The file {file_path} does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")
            
    # def edit_asset(asset_id, new_name, new_description):
    #     temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
    #     assets_file_path = 'data/devices.csv'
    #     asset_found = False

    #     with open(assets_file_path, mode='r') as file, temp_file:
    #         reader = csv.DictReader(file)
    #         writer = csv.DictWriter(temp_file, fieldnames=reader.fieldnames)
    #         writer.writeheader()

    #         for row in reader:
    #             if row['Asset ID'] == asset_id:
    #                 print(f"Editing asset: {row['Asset ID']}")
    #                 row['Asset ID'] = new_name
    #                 row['Depreciation'] = new_description
    #                 asset_found = True
    #             writer.writerow(row)

    #     if asset_found:
    #         shutil.move(temp_file.name, assets_file_path)
    #         print("Asset updated successfully.")
    #     else:
    #         print("Asset not found.")
    #     temp_file.close()

    # # Example usage
    # asset_id = input("Enter the asset ID to edit: ")
    # new_name = input("Enter the new name for the asset: ")
    # new_description = input("Enter the new description for the asset: ")
    # edit_asset(asset_id, new_name, new_description)    

                
    def assets_menu(self):
        data_menu = [
            "1. Add Assets",
            "2. Delete Asset",
            "3. Search For Asset",
            "4. Edit Assets",
            "5. Generate Pdf File For Assets",
            "6. Exit",
        ]
        quitting = False

        while not quitting:
            print(colored("\n===== Data Analysis Dashboard =====", 'blue', attrs=['bold']))
            terminal_menu = TerminalMenu(
                data_menu,
                title="Assets Management Menu",
                menu_cursor="-> ",
                menu_cursor_style=("bg_red", "fg_yellow"),
                menu_highlight_style=("bg_green", "fg_yellow"),
                cycle_cursor=True,
            )

            choice_index = terminal_menu.show()

            if choice_index == 0:
                self.add_assets()
            elif choice_index == 1:
                asset_id = input("Enter the Asset ID to delete: ")
                self.delete_asset(asset_id)
            elif choice_index == 2:
                self.search_for_asset()
            elif choice_index == 3:
                print("soon ....... ")
                # self.edit_asset()
            elif choice_index == 4:
                create_qr_code_and_pdf()
            elif choice_index == 5:
                print(colored("Exiting the Assets ...", 'red', attrs=['bold']))
                quitting = True
            else:
                print(colored("Invalid choice! Please enter a valid option.", 'yellow', attrs=['bold']))