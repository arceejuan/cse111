# In test_statement_of_account.py
import os
import pytest
import csv
from statement_of_account import generate_statement_of_account, read_payment_data

@pytest.fixture
def payment_data_file(tmp_path):
    # Create a temporary CSV file with dummy payment data
    file_path = tmp_path / "payments.csv"
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['A', 'B', 'C', 'D'])  # Header
        writer.writerow(['1', '2', '3', '4'])   # Sample data row
    return file_path

@pytest.fixture
def statement_date():
    # Use a fixed statement date for testing
    return "February 17, 2024"

def test_read_payment_data(payment_data_file):
    # Test whether payment data is read correctly from the CSV file
    data = read_payment_data(str(payment_data_file))
    assert len(data) == 1, f"Expected 1 row, but got {len(data)} rows."
    assert data[0] == ['1', '2', '3', '4'], f"Unexpected data: {data}"

def test_generate_statement_of_account(payment_data_file, statement_date, tmp_path):
    # Test the generation of the statement of account PDF
    client_name = "Test Client"
    output_directory = tmp_path

    output_pdf = generate_statement_of_account(client_name, str(payment_data_file), statement_date, output_directory)

    assert output_pdf is not None, "Output PDF file path is None."
    assert os.path.exists(output_pdf), f"Output PDF file {output_pdf} does not exist."

    # Check the content of the generated PDF
    with open(output_pdf, 'rb') as pdf_file:
        # Your additional checks/assertions on the PDF content can be performed here
        pass

def test_invalid_payment_data_file():
    # Test when the payment data file does not exist
    client_name = "Test Client"
    invalid_payment_data_file = "nonexistent_file.csv"
    statement_date = "February 17, 2024"
    output_directory = os.getcwd()

    output_pdf = generate_statement_of_account(client_name, invalid_payment_data_file, statement_date, output_directory)

    assert output_pdf is None, "Expected None for non-existent file."

if __name__ == "__main__":
    pytest.main()
