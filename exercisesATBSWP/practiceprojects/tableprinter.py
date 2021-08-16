import logging
import time

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def print_table(table):
    column_widths = [0] * len(table)
    for x in range(len(column_widths)):
        column_widths[x] = table[x]
        longest = ['']
        for y in range(len(column_widths[x])):
            if len(column_widths[x][y]) > len(longest[0]):
                longest[0] = column_widths[x][y]
        column_widths[x] = len(longest[0])
    print(f'Column_widths: {column_widths}')
    column_widths.sort()
    column_lines = column_widths[-1] * 3
    print("-" * column_lines)
    print("Table: ".center(column_widths[x] * 3))
    print("-" * column_lines)
    for row in zip(*table):
        for x, y in zip(row, column_widths):
            print(end=f"{x.rjust(y+2)}")
        print()
    print("-" * column_lines)


tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bobarosa', 'Frederica', 'David'],
    ['dogs', 'cats', 'tyrannosaurus', 'goose']
]

print_table(tableData)
