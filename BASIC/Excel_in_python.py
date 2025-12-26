# Working with Excel files in Python using openpyxl
from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active
sheet.title = "Sample Sheet"
# sheet['A1'] = "Index"
textdata = [["Name","City"],['Mayank',"New York"],["John","Los Angeles"],["Alice","Chicago"]]
for row in textdata:
    sheet.append(row)   
workbook.save("sample_excel.xlsx")  


for i in range(1, 11):
    for j in range(1,5):
        sheet.cell(row=i, column=j, value=f"Row {i}, Col {j}")

workbook.save("sample_excel.xlsx")


# Reading from an Excel file
