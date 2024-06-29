from fpdf import FPDF
import pyqrcode
import pandas as pd
import os
import png
from termcolor import colored

class PDF(FPDF):
    """
    Custom PDF class that extends FPDF for generating IT assets report.
    """
    def header(self):
        """
        Header method to add logo and title to each page.
        """
        # Add logo
        self.image('data/logo.png', 10, 8, 33)
        self.set_font('Arial', 'B', 12)
        # Move to the right
        self.cell(80)
        # Title below the logo
        self.cell(30, 10, 'IT Assets Report', 0, 1, 'C')

    def footer(self):
        """
        Footer method to add page number at the bottom of each page.
        """
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')

def add_qr_code_at_top_right(pdf, data):
    """
    Adds a QR code at the top right of the page with asset information.

    :param pdf: The PDF instance.
    :param data: A dictionary containing asset information.
    """
    # Generate QR code with asset information
    qr_data = f"{data['Asset ID']} {data['Asset Type']} {data['Brand']} {data['Model']} {data['Serial Number']} {data['Operating System']} {data['Processor']} {data['RAM']} {data['Storage']} {data['Purchase Date']} {data['Warranty Information']} {data['Assigned To']} {data['Location']} {data['Cost']} {data['Depreciation']} " 
    # Replace invalid characters in qr_data with underscores
    qr_data = qr_data.replace('/', '_').replace(':', '_').replace('*', '_').replace('?', '_').replace('"', '_').replace('<', '_').replace('>', '_').replace('|', '_')
    qr = pyqrcode.create(qr_data)
    qr_image_path = f"{qr_data}.png"
    qr.png(qr_image_path, scale=2)
    
    # Position QR code at the top right of the page
    qr_x = pdf.w - 30  # 20 units from the right of the page
    qr_y = 8  # 8 units from the top of the page
    pdf.image(qr_image_path, x=qr_x, y=qr_y, w=20)
    
    # Add "Scan me!!" text below QR code
    pdf.set_xy(qr_x, qr_y + 20)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(20, 10, 'Scan me!!', 0, 2, 'C')
    
    # Remove QR code image file after adding to PDF
    os.remove(qr_image_path)

def add_data_in_center_as_table(pdf, data):
    """
    Adds asset information in the center of the page as a table.

    :param pdf: The PDF instance.
    :param data: A dictionary containing asset information.
    """
    # Calculate the starting position for the table
    start_x = 20
    start_y = 60  # Adjusted to leave space for the title
    width = pdf.w - 2 * start_x
    height = 10
    
    # Set font for the table
    pdf.set_font('Arial', size=10)
    
    # Set colors for table header
    pdf.set_fill_color(0, 128, 0)  # Green background
    pdf.set_text_color(255)  # White text
    pdf.set_font('Arial', 'B', 10)  # Bold font for header
    pdf.set_draw_color(0)  # Black border for cells
    # Table header
    col_width = width / 2  # Split the width for 2 columns
    pdf.set_xy(start_x, start_y)
    pdf.cell(col_width, height, "Attribute", border=1, fill=True, align='C')
    pdf.cell(col_width, height, "Value", border=1, fill=True, align='C')
    pdf.ln(height)
    
    # Reset colors for table body
    pdf.set_fill_color(255)  # White background for body
    pdf.set_text_color(0, 128, 0)  # Green text for body
    
    # Table body with asset information
    for key, value in data.items():
        pdf.set_x(start_x)
        pdf.cell(col_width, height, key, border=1, align='C')
        pdf.cell(col_width, height, str(value), border=1, align='C')
        pdf.ln(height)

def create_qr_code_and_pdf():
    """
    Main function to create a PDF report with QR codes and asset information.
    """
    # Read data from CSV
    df = pd.read_csv('data/devices.csv')
    pdf = PDF()

    # Iterate through each row in the DataFrame and add to PDF
    for index, values in df.iterrows():
        pdf.add_page()
        
        # Add QR code at the top right of the page
        add_qr_code_at_top_right(pdf, values)
        
        # Add data in the center as a table
        add_data_in_center_as_table(pdf, values)
    
    # Save the PDF
    pdf.output('data/pdf/assets_report.pdf')
    print(colored("PDF report generated successfully!✅", 'green', attrs=['bold']))

if __name__ == "__main__":
    create_qr_code_and_pdf()