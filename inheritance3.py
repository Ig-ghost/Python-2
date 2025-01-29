#4. Hierchichal Inheritance -> single parent more than 1 child
#5. Hybrid Inheritance -> combining more than 1 type of inherirtance

class Teacher: #parent class
    def __init__(self, name):
        self.name = name

    def teach(self):
        print(f'teaching students {self.name}')

class MathTeacher(Teacher):
    def __init__(self, name, mathSkills):
        super().__init__(name) #self.name = name
        self.mathSkills = mathSkills
  
    def teachMath(self):
        print(f'teaching maths {self.name} {self.mathSkills}')

class EnglishTeacher(Teacher):
    def __init__(self, name, englishSkills):
        super().__init__(name)
        self.englishSkills = englishSkills
  
    def teachEnglish(self):
        print(f'teaching english {self.name} {self.englishSkills}')

a = Teacher('John')
# a.teach()
# a.teachMath()

b = MathTeacher('Bubloo', 90)
# b.teachMath()
# b.teach()

c = EnglishTeacher('Jasmine', 99)
# c.teachEnglish()
# c.teach()

#hybrid inheritance

class Employee:
    def employee(self):
        print('this is employee')

class Student:
    def student(self):
        print('this is student')

class Kid(Student):
    def kid(self):
        print('this is kid')

class Programmer(Employee, Kid):
    def programmer(self):
        print('this is programmer')

# a = Student()
# a.student()

# b

#for MRO

class A:
    def show(self):
        print('class A')

class B(A):
    def show(self):
        print('class B')
    # pass

class C(A):
    def show(self):
        print('class C')
    # pass

class D(C, B):
    pass

d = D()
d.show()

print(D.mro())
print(help(D))
#method resolution order

# this is a python program and this is 
# this is a python program and this is 
# this is a python program and this is 
# this is a python program and this is 
# this is a python program and this is 