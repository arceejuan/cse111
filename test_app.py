import tkinter as tk
from tkinter import filedialog, messagebox
import os
import csv
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors

# Define the function to extract the directory path from a file path
def get_directory_from_filepath(filepath):
    return os.path.dirname(os.path.abspath(filepath))

def read_payment_data(payment_data_file):
    """
    Read payment data from a CSV file starting from row 7.

    Parameters:
        payment_data_file (str): The file path of the CSV file containing payment data.

    Returns:
        list: A list containing payment data.
    """
    data = []
    with open(payment_data_file, 'r', newline='') as file:
        csv_reader = csv.reader(file)
        for _ in range(6):  # Skip the first 6 rows
            next(csv_reader, None)
        for row in csv_reader:
            # Read columns A-F
            row = [cell.strip() for cell in row[:6]]
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
    header_style_1 = ParagraphStyle(name='HeaderStyle1', fontName='Courier', fontSize=12, leading=14)
    header_paragraph_1 = Paragraph(header_text_1, header_style_1)
    elements.append(header_paragraph_1)

    header_text_2 = "Purok 4, Nalum, Baliok, Davao City"
    header_style_2 = ParagraphStyle(name='HeaderStyle2', fontName='Courier', fontSize=12, leading=14)
    header_paragraph_2 = Paragraph(header_text_2, header_style_2)
    elements.append(header_paragraph_2)

    header_text_3 = f"Statement Date: {statement_date}"
    header_style_3 = ParagraphStyle(name='HeaderStyle3', fontName='Courier', fontSize=12, leading=14)
    header_paragraph_3 = Paragraph(header_text_3, header_style_3)
    elements.append(header_paragraph_3)

    header_text_4 = f"\nClient Name: {client_name}"
    header_style_4 = ParagraphStyle(name='HeaderStyle4', fontName='Courier', fontSize=12, leading=14)
    header_paragraph_4 = Paragraph(header_text_4, header_style_4)
    elements.append(header_paragraph_4)

    # Add an empty paragraph for spacing before the table
    elements.append(Paragraph("", header_style_3))

    # Add centered "STATEMENT OF ACCOUNT" text
    statement_text = "\n STATEMENT OF ACCOUNT \n"
    statement_style = ParagraphStyle(name='StatementStyle', fontName='Courier', fontSize=16, leading=18, alignment=1)
    statement_paragraph = Paragraph(statement_text, statement_style)
    elements.append(statement_paragraph)


    # Create table data including headers
    table_data = [['MONTH', 'PAYMENT DATE', 'OR #', 'AMOUNT', 'PENALTY', 'BALANCE']] + data

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
        messagebox.showerror("Error", f"File '{payment_data_file}' not found.")
        return None
    
    data = read_payment_data(payment_data_file)
    
    if output_directory is None:
        # Extract the directory path from the CSV file path
        output_directory = get_directory_from_filepath(payment_data_file)
    
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    # Include client name in the PDF file name
    output_pdf = os.path.join(output_directory, f"statement_of_account_{client_name}.pdf")
    
    create_statement_of_account_pdf(client_name, statement_date, data, output_pdf)
    
    messagebox.showinfo("Success", f"Statement of Account PDF generated for {client_name}.\nSaved as '{output_pdf}'.")
    return output_pdf

def browse_file():
    filename = filedialog.askopenfilename(initialdir="/", title="Select CSV File", filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
    file_entry.delete(0, tk.END)
    file_entry.insert(0, filename)

def generate_pdf():
    client_name = client_name_entry.get()
    statement_date = statement_date_entry.get()
    payment_data_file = file_entry.get()

    if not client_name or not statement_date or not payment_data_file:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    output_pdf = generate_statement_of_account(client_name, payment_data_file, statement_date)
    if output_pdf:
        messagebox.showinfo("Success", f"Statement of Account PDF generated for {client_name}.\nSaved as '{output_pdf}'.")

# Create the main window
window = tk.Tk()
window.title("Statement of Account Generator")

# Create GUI elements
tk.Label(window, text="Client Name:").grid(row=0, column=0, padx=10, pady=5)
client_name_entry = tk.Entry(window)
client_name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(window, text="Statement Date:").grid(row=1, column=0, padx=10, pady=5)
statement_date_entry = tk.Entry(window)
statement_date_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(window, text="Payment Data File:").grid(row=2, column=0, padx=10, pady=5)
file_entry = tk.Entry(window)
file_entry.grid(row=2, column=1, padx=10, pady=5)
browse_button = tk.Button(window, text="Browse", command=browse_file)
browse_button.grid(row=2, column=2, padx=10, pady=5)

generate_button = tk.Button(window, text="Generate PDF", command=generate_pdf)
generate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Start the GUI event loop
window.mainloop()
