#object oriented programming --> class and object (methods and attributes)
#procedural programming --> 

# def welcome():
#     print('hello')

# welcome()

# print('hi')
# print(5 + 10)

#oops

#procedural
# brand = 'suzuki'
# color = 'red'

# def drive():
#     print('the car is drving ')

# print(brand) #brand : ferrari, color : red
# print('brand :',brand, ',color :', color)

# print(f'brand : {brand}, color : {color}') #f strings
# drive()
# hey = 'hello'
# print(f'{{}}')

#procedural programming --> step by step instructions

brand = 'Toyota' #instructions
color = 'red'

def drive():
    print('the car is driving')

# print(f'Brand : {brand}, Color : {color}')
# drive()

# print(f'{{}}}')

#oops --> object orientd programming

#classes and objects -> railway form

class Car: #class
    brand = 'Toyota' #attributes / properties
    color = 'red'

    def showDetails(self): #methods
        print(f'Brand : {self.brand}, Color : {self.color}')

a = Car() #a is object
# print(a.brand)
# print(a.color)

# a.showDetails()

b = Car() # b is object
b.brand = 'Ferrari'
b.color = 'Blue'
# print(b.brand)
# b.showDetails()


class Railway:
    name = 'John Doe' #attributes
    age = 20
    station = 'Rampur'

    def showDetails(self): #method
        print(f'Name : {self.name}, Age : {self.age}, Station : {self.station}')

sanjay = Railway()
sanjay.name = 'Sanjay'
sanjay.age = 18
sanjay.station = 'New York'
sanjay.showDetails()

satyarth = Railway()
satyarth.name = 'Satyarth'
satyarth.age = 18
satyarth.station = 'California'
satyarth.showDetails()

print(type(satyarth))

