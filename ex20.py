from sys import argv
#脚本参数
script, input_file = argv
#定义函数
def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count,f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file: \n")
#打开文件
print_all (current_file)

print("Now let's rewind kind of like a tape.")
#用seek()来重定向,方便下面输出
rewind(current_file)

print("Let's print three line:")
#用readline(),读取文本的每一行,通过current_line的叠加
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
