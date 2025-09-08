import openpyxl

# Create a new Workbook
wb = openpyxl.Workbook()
ws = wb.active

# Rename the sheet to 'LoginTestData'
ws.title = "LoginTestData"

# Define the header row
header = ["Test ID", "Username", "Password", "Date", "Time of Test", "Name of Tester", "Test Result"]
ws.append(header)

# Add 5 test username-password combinations with blank date, time, and results
test_data = [
    ["1", "Admin", "admin123", "", "", "Tester1", ""],
    ["2", "invalidUser", "admin123", "", "", "Tester1", ""],
    ["3", "Admin", "wrongPass", "", "", "Tester1", ""],
    ["4", "user1", "password1", "", "", "Tester1", ""],
    ["5", "Admin", "admin123", "", "", "Tester1", ""]
]

for row in test_data:
    ws.append(row)

# Save the workbook to file
wb.save("login_test_data.xlsx")

print("Excel file 'login_test_data.xlsx' created successfully.")
