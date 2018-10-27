print('----------向Excel中写入相关数据----------')
## 方法内，即括号内，使用ctrl+p可以查看所需使用的参数
import xlwt

file = xlwt.Workbook()
# sheet = file.add_sheet('新加第一个sheet页')
## 若实现对同一个单元格重复写入，可使用如下方法
sheet = file.add_sheet('新加第一个sheet页',cell_overwrite_ok=True)

style = xlwt.XFStyle()
font = xlwt.Font()
font.name='Time New Roman'
font.bold=True
font.height=300
font.colour_index=0x35
style.font=font

## table.write(行,列,value)
sheet.write(0,0,'username1')
sheet.write(0,0,'username2')
sheet.write(0,1,'password',style)
file.save('excelFileWrite.xls')

'''
写入内容，使用style
style = xlwt.XFStyle() #初始化样式
font = xlwt.Font() #为样式创建字体
font.name = 'Times New Roman'
font.bold = True
style.font = font #为样式设置字体
table.write(0, 0, 'some bold Times text', style) # 使用样式
'''
