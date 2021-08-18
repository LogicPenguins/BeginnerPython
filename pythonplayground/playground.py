import openpyxl

wb = openpyxl.Workbook()

sheet = wb['Sheet']

c5 = sheet['C5']


sheet['C5'] = 'Hello'

print(sheet['A1:F1'])


wb.save('Lol.xlsx')

368