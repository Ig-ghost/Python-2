# class -> 

#form 
#name : ----
#age : ----
#station number : ----

#Name : -----sanjay
#age : ----15
#station number : ----200 --> object of sanjay

#Name : -----rehnuma
#age : ----20
#station number : ----201

class Book: #title author and price
    name = 'abc'
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def show(self): #method
        print(f'Title : {self.title}, Author : {self.author}, Price : {self.price}')

book1 = Book('the jungle book', 'Mogli', 500)
# book1.__init__() #constructor is automatically called
# book1.show()
# print(book1.title1)
# book1.show()

#this is multi cursor alt + click
#this is multi cursor alt + click

book2 = Book('Python Expert', 'Aaysha', 6000)
# book2.show()

#student grades manangement

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def update_grades(self, new_grade):
        self.grade = new_grade

    def display_grades(self):
        print(f'Name : {self.name}, Grades : {self.grade}')

student1 = Student('Sanjay', 'A')
student1.update_grades('A+')
student1.display_grades()

student2 = Student('Aaysha', 'A+')
student2.display_grades()

name = 'john'
age = 15
#name is john and age is 15
print('name is', name, 'and age is', age)
print(f'name is {name} and age is {age}')

# print('grades')
# python and web development