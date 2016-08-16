from sys import argv

script, filename = argv

print("We 're gong to erase %r." %filename)
print("If you don't want that, hit CTRL-C(^C).")
print("If you do want that , hit RETURN.")

input("?")
print("Opening the file ...")
target = open(filename,"w")

print("Now I'm going to ask you for three lines ")

lines1 = input("line 1: ")
lines2 = input("line 2: ")
lines3 = input("line 3: ")

print("I'm going to write these to the file ")

target.write(lines1)
target.write("\n")
target.write(lines2)
target.write("\n")
target.write(lines3)
target.write("\n")

print("And finally , we close it")
target.close()
