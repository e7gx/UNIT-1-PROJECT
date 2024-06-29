import os
import pyqrcode
import pandas as pd

def generate_qr_code():
    df = pd.read_csv('data/devices.csv')

    # Create the "qrcode_assets" folder if it doesn't exist
    if not os.path.exists('qrcode_assets'):
        os.makedirs('qrcode_assets')

    for index, values in df.iterrows():
        asset_id = values["Asset ID"]
        asset_type = values["Asset Type"]
        brand = values["Brand"]
        model = values["Model"]
        serial_number = values["Serial Number"]
        operating_system = values["Operating System"]
        processor = values["Processor"]
        ram = values["RAM"]
        storage = values["Storage"]
        purchase_date = values["Purchase Date"]
        warranty_information = values["Warranty Information"]
        assigned_to = values["Assigned To"]
        location = values["Location"]
        cost = values["Cost"]
        depreciation = values["Depreciation"]
        
        data = f''' 
        Asset_id: {asset_id} \n 
        Asset_type: {asset_type} \n
        Brand: {brand} \n
        Model: {model} \n
        Serial Number: {serial_number} \n
        Operating System: {operating_system} \n
        Processor: {processor} \n
        RAM: {ram} \n
        Storage: {storage} \n
        Purchase Date: {purchase_date} \n
        Warranty Information: {warranty_information} \n
        Assigned To: {assigned_to} \n
        Location: {location} \n
        Cost: {cost} \n
        Depreciation: {depreciation} \n
        '''
        
        image = pyqrcode.create(data)
        image.png(f'data/qrcode_assets/{asset_id}_{asset_type}.png', scale=5)
        # print(image.terminal(quiet_zone=9))
