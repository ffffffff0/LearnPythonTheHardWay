class TheThing(object):
    def __init__(self):
        self.number = 0

    def some_function(self):
        print('i got a called')

    def add_me_up(self, more):
        self.number += more
        return self.number

# two different things
a = TheThing()
b = TheThing()


a.some_function()
b.some_function()

print(a.add_me_up(20))
print(b.add_me_up(30))

print(a.number)
print(b.number)

# study this . This is how you pass a variable
# from one class to anthoer you will need this


class TheMultiplier(object):
    def __init__(self, base):
        self.base = base

    def do_it(self, m):
        return m * self.base

x = TheMultiplier(a.number)
print(x.do_it(b.number))


class Animal(object):
    # Animal类的构建
    pass


class Dog(Animal):
    # Dog类的构建，并继承Animal类
    def __init__(self, name):
        # 设置Dog的内置变量
        self.name = name


class Cat(Animal):
    # Cat类的创建，并继承Animal
    def __init__(self, name):
        # Cat内置变量的设置
        self.name = name


class Person(object):
    # Person类的创建
    def __init__(self, name):
        # Person的内置变量的设置
        self.name = name
        self.pet = None


class Employee(Person):
    # Emplyee的创建,并继承Person类
    def __init__(self, name, salary):
        Person.__init__(self, name)
        # 继承Employee类中的变量
        self.salary = salary


class Fish(object):
    pass


class Salmon(Fish):
    pass


class Halibut(Fish):
    pass

rover = Dog('Rover')
satan = Cat('Satan')
mary = Person('Mary')
mary.pet = satan
frank = Employee('Frank', 120000)
frank.pet = rover
flipper = Fish()
crouse = Salmon
harry = Halibut()
