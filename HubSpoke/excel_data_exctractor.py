import xlrd
from pathlib import Path
import json
from matplotlib import colors as mcolors 

import xlsxwriter

class ExcelData():

	dir_name = Path(__file__).resolve().parent	
	json_file_name = 'data.json'
	sku_file_name = 'sku_data.json'
	sku_file_name2 = 'sku_data_filtered.json'
	sku_retailer_file_name = 'sku_retailer_data.json'
	sku_retailer_file_name2 = 'sku_retailer_data_filtered.json'

	colors = mcolors.CSS4_COLORS

	def __init__(self,file_name):
		self.file_name = file_name
		self.file_path = self.dir_name / self.file_name
		self.generate_excel_file()


	def short_color(self,color):
		if color == 'Gold':
			return 'GLD'
		return f"{color[0]}{color[1]}{color[-1]}".upper()

	def get_excel_data(self):			
		book = xlrd.open_workbook(self.file_path)
		sh = book.sheet_by_index(0)
		data = []
		for row in range(3,sh.nrows):
			obj = {}
			for col in range(0,sh.ncols):
				obj.setdefault(sh.cell_value(rowx=2, colx=col).lower(),
					           sh.cell_value(rowx=row, colx=col))
			data.append(obj)
		return data

	def get_sku_data(self,color_filter=False):
		genereted_data = []
		for obj in self.get_excel_data():
			if color_filter:
				func = lambda x:x.lower() in self.colors
				color = ' '.join(filter(func,obj.get('remark','').split(' ')))
			else:
				color = obj.get('remark',' ')

			filtered_item = filter(lambda x:x,[obj['brand'],obj['model'],color])
			item = '-'.join(filtered_item)
			genereted_data.append(item)
		return genereted_data


	def get_sku_retailer_data(self,color_filter=False):
		genereted_data = []

		for obj in self.get_excel_data():

			if color_filter:
				def filter_and_format(item):
					if item:
						if item.lower() in self.colors:
							return self.short_color(item)
					return ''


			else:
				def filter_and_format(item):
					if item:
						if item.lower() in self.colors:
							return self.short_color(item)
					return item


			color = ' '.join(map(filter_and_format,obj.get('remark','').split(' '))).strip()

			filtered_item = filter(lambda x:x,[obj['brand'],obj['model'],color])
			item = '-'.join(filtered_item)
			genereted_data.append(item)
		return genereted_data


	def generate_excel_file(self):
		workbook = xlsxwriter.Workbook('data.xlsx')
		worksheet = workbook.add_worksheet()

		# Widen the first column to make the text clearer.
		worksheet.set_column('A:A', 50)
		worksheet.set_column('B:B', 50)
		worksheet.set_column('C:C', 11)
		worksheet.set_column('E:E', 15)
		worksheet.set_column('F:F', 23)
		worksheet.set_column('G:G', 43)

		# Add a bold format to use to highlight cells.
		bold = workbook.add_format({'bold': True})

		# Write some simple text.
		worksheet.write('A1', 'retailer_sku',bold)
		worksheet.write('B1', 'vendor_sku',bold)
		worksheet.write('C1', 'quantity',bold)
		worksheet.write('D1', 'cost',bold)
		worksheet.write('E1', 'leadtime',bold)
		worksheet.write('F1', 'vendor_name',bold)
		worksheet.write('G1', 'purchase_name',bold)		

		data = self.get_excel_data()
		sku_data = self.get_sku_data(color_filter=True)
		sku_retailer_data = self.get_sku_retailer_data(color_filter=True)
		index = 0

		for item in data:

			worksheet.write(index + 2, 0, sku_retailer_data[index])
			worksheet.write(index + 2, 1, sku_data[index])
			worksheet.write(index + 2, 2, 1000)
			worksheet.write(index + 2, 3, item['hkd'])
			worksheet.write(index + 2, 4, 2)
			worksheet.write(index + 2, 5, "Dunamis")
			worksheet.write(index + 2, 6, item['model'])
			index += 1

		# Text with formatting.
		# worksheet.write('A2', 'World', bold)

		# # Write some numbers, with row/column notation.
		# worksheet.write(2, 0, 123)
		# worksheet.write(3, 0, 123.456)

		# # Insert an image.
		# worksheet.insert_image('B5', 'logo.png')

		workbook.close()
		


excel_data = ExcelData('price.xls')
 
