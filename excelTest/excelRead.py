# python 3.x版本输出不换行格式如下
# print(x, end='')    end='' 可使输出不换行
print('----------循环读取Excel内所有数据----------')
import xlrd
data = xlrd.open_workbook('excelFile.xlsx')

sheets = data.sheet_names()
print(sheets)

for i in range(len(sheets)):
    print('第' + str(i+1) + '个sheet页：' + sheets[i] + '>>>>>>>>')
    sheet = data.sheet_by_index(i)
    nrow = sheet.nrows
    ncol = sheet.ncols
    # print(nrow,ncol)
    for row in range(0,nrow):
        ## 方法一：简单读取sheet中所有数据，不注重展示格式
        #  print(sheet.row_values(row))
        for col in range(0,ncol):
            cellContent = sheet.cell(rowx=row, colx=col).value
            ## 方法二：简单对齐
            # print(str(cellContent).ljust(15),end='')

            ## 方法三：严格对齐(仅适用于仅中文、英文，若中英文混合的还是会出现不对齐情况)
            name = str(cellContent)
            print('{name:<{len}}\t'.format(name=name,len=30-len(name.encode('ANSI'))+len(name)),end='')
        print()
