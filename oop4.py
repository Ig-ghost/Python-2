#object oriented programming
#classes and objects 
#classes -> blueprint for objects

#constructor -> automatically called whenever an object is created


class student:
    # name = 'john' #attribute
    def __init__(self, name, course): #constructor
        self.username = name
        self.usercourse = course

    def show(self): #method
        print(f'Name : {self.username}, Course : {self.usercourse}')

a = student('sanjay', 'nit') #object
# print(a.name)
# a.show()
# a.__init__()

def add(a, b): # a & b are arguments
    print(a + b)

# add(5, 3) #5 & 3 are parameters

b = student('Rehnuma', 'polytechnic')
# b.show()

c = student('Mahak', 'NIT')
# c.show()

#private attributes

class BankAccount:
    name = 'john' #public attribute
    __amount = 500 #private attributes
    __isManager = False

    def show(self): #getter
        print(f'amount is {self.__amount} and they are Manager : {self.__isManager}')

d = BankAccount()
#object.attribute/ method
# print(d.name)
# print(d.__amount)
# print(d.__isManager)
# d.show()

class Student:
    def __init__(self, name, marks):
        self.username = name #public attributes
        self.__usermarks = marks #private

    def show(self):
        print(f'Name : {self.username}, marks : {self.__usermarks}')

Aaysha = student('Aaysha', 100)
print(Aaysha.username)
# print(Aaysha.__usermarks)
Aaysha.show()