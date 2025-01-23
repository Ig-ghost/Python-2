#oop -> classes and objects
#classes are blueprint for objects

class Student:
    name = 'John' #attributes
    age = 20
    course = 'ABC'

    def show(self): #methods
        print(f'Name : {self.name}, Age : {self.age}, Course : {self.course}')

mahak = Student() 
#object.attribute / method name
mahak.name = 'Mahak'
mahak.age = 18
mahak.course = 'bsc'
# print(a.name)

# mahak.show()

satyarth = Student()
satyarth.name = 'satyarth'
satyarth.age = 20
satyarth.course = 'bsc'
# satyarth.show()

#constructor

class Car:
    def __init__(self, company = 'abc', color = 'abc', torque = '20nm'): #automatically invoked / called
        self.company = company
        self.color = color
        self.torque = torque

    def show(self):
        print(f'Compnay : {self.company}, Color : {self.color}, Torrque : {self.torque}')

a = Car()
# a.show()

b = Car('Toyota', 'White', '50nm')
# b.show()
# a.__abc__()
# b = Car()

class Bank:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def __init__(self, type):
        self.type = type

    def showHolder(self):
        print(f'type : {self.type}, holder : {self.holder}')

    def showbalance(self):
        print(f'Balance : {self.balance}')

mohit = Bank('Mohit', 20, 'current')
mohit.showHolder()
# mohit.showbalance()
# # sanjay = Bank('Sanjay', 1000)
# sanjay.showbalance()
# mohit.showbalance()

class new:
    name = 'abc'

    def show(self):
        print(self.name)

# a = new()
# a.name = 'sanjay'
# a.show()

# b = new()
# b.show()