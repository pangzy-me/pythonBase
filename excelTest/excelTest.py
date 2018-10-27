# 升级pip版本或者install软件包时，如果报超时错误，加上延时即可 --default-timeout=100
# python -m pip --default-timeout=100 install --upgrade pip

import xlrd
# import xlwt
data = xlrd.open_workbook('excelFile.xlsx')

sheet1 = data.sheet_by_index(0)
# sheet2 = data.sheet_by_name('Sheet1')
# print(sheet1,sheet2)
nrows = sheet1.nrows
ncols = sheet1.ncols

# 获取整行和整列的值（数组）
rowText0 = sheet1.row_values(0)
rowText1 = sheet1.row_values(1)
rowText2 = sheet1.row_values(2)
colText = sheet1.col_values(0)
print(rowText0)
print(rowText1)
print(rowText2)
print(colText)

# 获取单个单元格的数据，方法一：使用单元格索引
cellA1 = sheet1.cell(0,0).value
cellB2 = sheet1.cell(1,1).value
print(cellA1,cellB2)

# 获取单个单元格的数据，方法二：使用行列索引
cell_A1 = sheet1.row(0)[0].value
cell_B2 = sheet1.col(1)[1].value
print(cell_A1,cell_B2)



print('-----------------简单认识sheet页相关操作-----------------')
# nsheets属性是一个整数，返回包含工作簿sheet的数量.与sheet_by_index方法结合起来是获取独立sheet
print(data.nsheets)
for sheet_idx in range(data.nsheets):
    print(data.sheet_by_index(sheet_idx))

# sheet_names方法返回包含工作簿中所有sheet名字,单独的sheet可以通过sheet_by_name方法使用这些名字获取
print(data.sheet_names())
for sheet_name in data.sheet_names():
    print(sheet_name)
    print(data.sheet_by_name(sheet_name))

# sheets方法的结果是迭代获取工作簿中的每个sheet
for sheet in data.sheets():
    print(sheet)


