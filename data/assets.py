import csv
import datetime
import string
import cv2
from termcolor import colored
from art import *
import colorama
from data.code.qrcode_reader import check_device_in_csv, draw_polygon, get_qr_data
from data.pdf.pdf import create_qr_code_and_pdf
from simple_term_menu import TerminalMenu
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
                    while True:
                        purchase_date = input(f'{i+1}. Enter Purchase Date (YYYY-MM-DD): ')
                        try:
                            datetime.datetime.strptime(purchase_date, '%Y-%m-%d')
                            break
                        except ValueError:
                            print(colored("Invalid date format. Please enter the date in the format YYYY-MM-DD.", 'red', attrs=['bold']))
                    warranty_info = input(f'{i+1}. Enter Warranty Information: ')
                    while True:
                        try:
                            warranty_info = int(warranty_info)
                            break
                        except ValueError:
                            print("Invalid input. Please enter a number.")
                            warranty_info = input(f'{i+1}. Enter Warranty Information: ')
                    assigned_to = input(f'{i+1}. Enter Assigned To: ')
                    assigned_to = str(assigned_to)
                    location = input(f'{i+1}. Enter Location: ')
                    cost = input(f'{i+1}. Enter Cost: $')
                    depreciation = input(f'{i+1}. Enter Depreciation: $ ')

                    writer.writerow([asset_id, asset_type, brand, model, serial_number, operating_system, processor, ram, storage, purchase_date, warranty_info, assigned_to, location, cost, depreciation])
                    print("\n")
                    print(colored("All records inserted successfully!", 'green', attrs=['bold']))

        except Exception as e:
            print(f"An error in add_assets() function class AddAssets: {str(e)}")

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
            search_term = input("Enter the asset name or ID to search for: ")
            with open(file_path, mode='r') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    if row['Asset ID'].lower() == search_term.lower():
                        print(f"Asset Found: {row}")
                        asset_found = True
                        break 
                
                if not asset_found:
                    print("Asset not found.")
        
        except FileNotFoundError:
            print(f"The file {file_path} does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def qrcode_reader(self):
        """
        Reads QR codes from the video stream captured by the camera.

        This method opens the camera, captures frames, and processes them to detect QR codes.
        It continuously reads frames from the webcam until a QR code containing a device ID is found in a CSV file.
        If a device ID is found, it prints a success message, writes the device has been found, and stops the process.
        If a device ID is not found, it prints a failure message and continues to read frames.
        The processed frames are displayed in a window named "QR Code Scanner".

        Returns:
            None
        """
        cap = cv2.VideoCapture(0)
        try:
            while True:
                ret, frame = cap.read()
                if not ret:
                    print("Failed to grab frame")
                    break
                qr_objects = get_qr_data(frame)
                if qr_objects:
                    qr_data = qr_objects[0].data.decode('utf-8')
                    print(qr_data)
                    if check_device_in_csv(qr_data):
                        print(colored("Device ID found in CSV file.", "green"))
                        with open('data/devices.csv', mode='a', newline='') as file:
                            file.write(f"Device with ID '{qr_data}' has been found.\n")
                        break
                frame = draw_polygon(frame, qr_objects)
                cv2.imshow("QR Code Scanner", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        finally:
            cap.release()
            cv2.destroyAllWindows()

    def assets_menu(self):
        data_menu = [
            "1. Add Assets",
            "2. Delete Asset",
            "3. Search For Asset",
            "4. Edit Assets",
            "5. Generate Pdf File For Assets",
            "6. QRCode Reader",
            "7. Exit",
        ]
        quitting = False

        while not quitting:
            print(colored("\n<===== Assets Menu =====>\n", 'blue', attrs=['bold']))
            terminal_menu = TerminalMenu(
                data_menu,
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
                    print(colored("Scanning......","light_green",attrs=['bold']))
                    self.qrcode_reader()
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                    print(colored("Exiting the Assets ...", 'red', attrs=['bold']))
            elif choice_index == 6:
                print(colored("Exiting the Assets ...", 'red', attrs=['bold']))
                quitting = True
            else:
                print(colored("Invalid choice! Please enter a valid option.", 'yellow', attrs=['bold']))