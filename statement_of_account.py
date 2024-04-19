import csv
import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors

def read_payment_data(payment_data_file):
    """
    Read payment data from a CSV file.
    
    Parameters:
        payment_data_file (str): The file path of the CSV file containing payment data.
        
    Returns:
        list: A list containing payment data.
    """
    data = []
    with open(payment_data_file, 'r', newline='') as file:
        csv_reader = csv.reader(file)
        next(csv_reader, None)  # Skip header
        for row in csv_reader:
            row = [cell.strip() for cell in row[:4] if cell.strip()]  # Only consider non-empty cells
            if row:
                data.append(row)
    return data

def create_statement_of_account_pdf(client_name, statement_date, data, output_pdf):
    """
    Create a statement of account PDF for a given client using payment data.
    
    Parameters:
        client_name (str): The name of the client.
        statement_date (str): The statement date.
        data (list): A list containing payment data.
        output_pdf (str): The file path for the output PDF file.
        
    Returns:
        None
    """
    doc = SimpleDocTemplate(output_pdf, pagesize=letter)
    elements = []

    header_text_1 = "AJIA Real Estate Marketing"
    header_style_1 = ParagraphStyle(name='HeaderStyle1', fontName='Times-Roman', fontSize=12, leading=14)
    header_paragraph_1 = Paragraph(header_text_1, header_style_1)
    elements.append(header_paragraph_1)

    header_text_2 = "Purok 4, Nalum, Baliok, Davao City"
    header_style_2 = ParagraphStyle(name='HeaderStyle2', fontName='Times-Roman', fontSize=12, leading=14)
    header_paragraph_2 = Paragraph(header_text_2, header_style_2)
    elements.append(header_paragraph_2)

    header_text_3 = f"Statement Date: {statement_date}"
    header_style_3 = ParagraphStyle(name='HeaderStyle3', fontName='Times-Roman', fontSize=12, leading=14)
    header_paragraph_3 = Paragraph(header_text_3, header_style_3)
    elements.append(header_paragraph_3)

    table_data = [['Column A', 'Column B', 'Column C', 'Column D']] + data

    table_style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
                              ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                              ('GRID', (0, 0), (-1, -1), 1, colors.black)])
    
    table = Table(table_data)
    table.setStyle(table_style)
    elements.append(table)

    doc.build(elements)

def generate_statement_of_account(client_name, payment_data_file, statement_date, output_directory=None):
    """
    Generate a statement of account PDF for a given client using payment data from a CSV file.
    
    Parameters:
        client_name (str): The name of the client.
        payment_data_file (str): The file path of the CSV file containing payment data.
        statement_date (str): The statement date.
        output_directory (str, optional): The directory where the PDF file will be saved. Defaults to None.
        
    Returns:
        str: The file path where the generated PDF is saved.
    """
    if not os.path.exists(payment_data_file):
        print(f"Error: File '{payment_data_file}' not found.")
        return None
    
    data = read_payment_data(payment_data_file)
    
    if output_directory is None:
        output_directory = os.getcwd()  # Use the current working directory
    
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    output_pdf = os.path.join(output_directory, "statement_of_account.pdf")
    
    create_statement_of_account_pdf(client_name, statement_date, data, output_pdf)
    
    print(f"Statement of Account PDF generated for {client_name}. Saved as '{output_pdf}'.")
    return output_pdf

def get_statement_date():
    """
    Prompt the user to input the statement date.
    
    Returns:
        str: The statement date provided by the user.
    """
    return input("Enter the statement date (e.g., February 15, 2024): ")

def test_generate_statement_of_account():
    """
    Test function for generate_statement_of_account.
    """
    client_name = "Test Client"
    payment_data_file = "payments.csv"
    statement_date = get_statement_date()
    output_directory = r"D:\Dont Delete\Desktop\Statement of Accounts"  # Used raw string to avoid escape sequences
    
    output_pdf = generate_statement_of_account(client_name, payment_data_file, statement_date, output_directory)
    
    assert output_pdf is not None and os.path.exists(output_pdf), "PDF file was not generated successfully."

test_generate_statement_of_account()
