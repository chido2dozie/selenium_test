import openpyxl


# Load excel sheet
workbook = openpyxl.load_workbook("/Users/chidozieamefule/Downloads/Copy of Credentials.xlsx")

sheet = workbook['Credentials']

# Valid login details
valid_username = sheet['A2'].value
valid_password = sheet['B2'].value

# Invalid login details
invalid_username = sheet['A3'].value
invalid_password = sheet['B3'].value

