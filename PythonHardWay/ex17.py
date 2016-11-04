from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from %s to %s "%(from_file, to_file))
#we could do these two on one line too, how?
input = open(from_file)
indata = input.read()

print("The input file is %d bytes long"% len(indata))

print("Does the output file exist? %r"%exists(to_file))
#你应该很快注意到了我们 import 了又一个很好用的命令 exists。
#这个命令将文件名字符串作为参数，如果文件存在的话，它将返回 True，
#否则将返回 False。在本书的下半部分，我们将使用这个函数做很多的事情，
#不过现在你应该学会怎样通过 import 调用它。
print("Ready ,hit RETURN to continue, CTRL-C to abort")
#input()

output = open(to_file,"w")
output.write(indata)

print("Alright,all done")

output.close()
input.close()
