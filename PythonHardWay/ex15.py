from sys import argv
#导入模块
script, filename = argv
#设置系数
txt = open(filename,"r")
#打开文件
print("Here 's your file %r :" %(filename))
print(txt.read())
#输出文件内容
print("Type the filename again:")
file_again = input("> ")
txt_again = open(file_again)
print(txt_again.read())
#再次输出而文件内容
