i = 0
numbers = []
while i < 6:
    print("At the top i is %d"% i)
    numbers.append(i)

    i = i + 1
    print("Numbers now:",numbers)
    print("At the bottom i is %d" %i)



print("The numbers:")

for num in numbers:
    print(num)


#更改
print("------------------------------------------------------")


def change(number):
    i = 0
    numbers = []
    while i < number:
        print("At the top i is  %d"% i)
        numbers.append(i)
        i = i + 1
        print("Numbers now :",numbers)
        print("At the bottom i is %d"%i)

#for循环
for i in range(0,7):
    numbers = []
    print("At the top i is %d "%i)
    numbers.append(i)
    i = i + 1
    print("Numbers now :",numbers)
    print("At the bottom i is %d " %i)
    
    

        
        
    
