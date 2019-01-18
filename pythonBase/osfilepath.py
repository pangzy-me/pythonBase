import os

# 取当前文件的路径
a = os.path.realpath(__file__)
print(a)
# 取当前文件路径的目录
adir = os.path.dirname(a)         # 取当前文件的目录路径，方法一
print(adir)
# b = os.path.split(a)[0]         # 取当前文件的目录路径，方法二
# print(b)

# 两步合成一步，取当前文件路径的目录
curDir = os.path.dirname(os.path.realpath(__file__))
print(curDir)

# 设置配置文件路径
configFile = 'config.ini'
configPath = os.path.join(curDir, configFile)
print(configPath)

# 设置多层级目录
filename2 = 'config2.ini'
d = os.path.join(adir, "new_dir", "new_dir_dir", filename2)
print(d)

print(d[:3])    # 切片，取盘符路径
print(d[3:])    # 切片，取除盘符之外的路径

