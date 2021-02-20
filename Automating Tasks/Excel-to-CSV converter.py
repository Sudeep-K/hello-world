#! python3

# Excel-to-CSV Converter.py -  a program that reads all the Excel files 
# in the current working directory and outputs them as CSV files.

import os, openpyxl, csv

for filename in os.listdir('.'):
	
	# Skip non-xlsx files, load the workbook object.
	if not filename.endswith('.xlsx'):
		continue

	# open the EXCEL workbook and access the active sheet
	wb = openpyxl.load_workbook(filename)
	sheet = wb.active

	# 'maximum column' and 'maximum row' in our worksheet
	column_maxnum = sheet.max_column
	row_maxnum = sheet.max_row

	# Create the CSV filename from the Excel filename
	file_object = open(filename[:-5] + '.csv', 'w', newline='')
	csv_writer = csv.writer(file_object)

	for row_num in range(1, row_maxnum + 1):		
		# Loop through every row in the sheet.
		row_data = []
		# Loop through each cell in the row.
		for column_num in range(1, column_maxnum + 1):
			
			row_data.append(sheet.cell(row = row_num, column = column_num).value)
		# Append each row's data to csv file
		csv_writer.writerow(row_data)

	file_object.close()