#object oriented progrmming

# class Person:
#     def __init__(self, name):
#         #for initializing attributes
#         self.name = name

#     def show(self):
#         print(f'Name : {self.name}')

# a = Person('John')
# a.show()
# print(a.name)

#inheritance

class Animal: #parent class / base class
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f'Name : {self.name}')

class Dog(Animal): #child class
    def speak(self):
        print(f'Dog Name : {self.name}')

a = Animal('Bruno')
# a.speak()

b = Dog('John')
# b.speak()

class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print(f'Name : {self.name}, Id : {self.id}')


class Emp(Person):
    # def __init__(self, name, id, lang): #constructor of emp class
    #     super().__init__(name, id) ##constructor of emp class
    #     self.lang = lang

    def display(self):
        print(f'Name : {self.name}, id : {self.id}')

emp = Person('John', 300)
emp.display()
newemp = Emp('brumo', 20)
newemp.display()

