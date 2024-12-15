# Importing necessary libraries to read the PDF and CSV files
import pandas as pd
import fitz  # PyMuPDF for reading the PDF

# Reading the CSV file
people_df = pd.read_csv('people.csv')

# Reading the PDF file
pdf_document = fitz.open('EDA Internship 2.0 Week 2.pdf')
pdf_text = ''

# Extracting text from the PDF
for page in pdf_document:
    pdf_text += page.get_text()

# Displaying the first few rows of the CSV and the extracted PDF text
print("CSV Data Head:")
print(people_df.head())

print("\
Extracted PDF Text:")
print(pdf_text[:1000])  # Displaying the first 1000 characters of the PDF text for context

# Solving the second tasks from the PDF document

# Task 6: Import CSV 'people.csv' and set specific columns as index
# Setting 'User Id' as the index as per the instructions
people_df.set_index('User Id', inplace=True)

# Displaying the updated DataFrame
print("Updated DataFrame with 'User Id' as index:")
print(people_df.head())
