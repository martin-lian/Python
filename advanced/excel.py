# import xlrd

# location=("C:\\Users\\BHC\\Desktop\\data.xlsx")

# wb =xlrd.open_workbook(location)

# sheets=wb.sheet_by_index(0)

# print(sheets.cell_value(1,1))

# import pandas as pd
# pd.read_excel('C:\\Users\\BHC\\Desktop\\data.xlsx', engine='openpyxl')

# print(excel(1,1))

import pandas as pd
df = pd.read_excel('C:\\Users\\BHC\\Desktop\\data.xlsx', engine='openpyxl')
