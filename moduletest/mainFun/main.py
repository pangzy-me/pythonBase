print('这是主函数：')
from moduletest.mainFun import subMain

subMain.subAddNew(3, 5, 0)
subMain.subAddNew(5, 5, 0)
# import调用时，import之后的全部都要写
import moduletest.carTypes.cars
moduletest.carTypes.cars.Audo('A6')
# 多个包import导入调用
# import mainFun.subMain,carTypes.cars
# 用as起别名时，只需用别名替代即可
import moduletest.mathFunctions.maths as MATH
MATH.add(3,3)
# from..包名..import..函数/变量..
# 调用时，只需直接使用函数及变量即可
from moduletest.mathFunctions.maths import sub,c
sub(5,3)
print('直接导入的c=%d' % c)

