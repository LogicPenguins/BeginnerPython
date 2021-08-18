#! python3
# samplechart.py - A very simplistic program to make a bar graph in an excel spreadsheet

from pathlib import Path
import openpyxl
import os

# Clears terminal for each time program is run for a less messy terminal
os.system('cls')

# Makes workbook object and sets sheet var to the active sheet in the workbook
wb = openpyxl.Workbook()
sheet = wb.active

# Assigns a number for each cell from A1 to A11
for i in range(1, 11):
    sheet[f'A{i}'] = i


ref_obj = openpyxl.chart.Reference(sheet, min_col=1, min_row=1, max_col = 1, max_row=10)

series_obj = openpyxl.chart.Series(ref_obj, title='First Series')

chart_obj = openpyxl.chart.BarChart()
chart_obj.title = 'My Chart'
chart_obj.append(series_obj)

sheet.add_chart(chart_obj, 'C5')

wb.save(f'{Path.home()}\\small-projects-python\\Excel_Mini_Projs\\xlsx_files\\sampleChart.xlsx')