# + - * / etc...
#overload -> giving them meaning beyond their predefined meaning

# print(5 + 3)
# print('hello' + 'world') #concatenation

# print(4 * 4)
# print('python' * 4)

class Vector:
    def __init__(self, i, j, k, m):
        self.i = i
        self.j = j
        self.k = k
        self.m = m

    #dunder / magic methods
    def __add__(self, *other):
        return Vector(
            self.i + sum(map(lambda v: v.i, other)), #sum[2, 2]
            self.j + sum(map(lambda v: v.j, other)), #sum[3, 3] -> 9
            self.k + sum(map(lambda v: v.k, other)), #sum[5, 5]
            self.m + sum(map(lambda v: v.m, other)) #sum[10, 10]
        )
    
    def __sub__(self, other):
        return self.i - other.i, self.j - other.j, self.k - other.k
    
    def __mul__(self, other):
        return self.i * other.i, self.j * other.j, self.k * other.k
    
    def __truediv__(self, other):
        return Vector(self.i / other.i, self.j / other.j, self.k / other.k)
    
    def __str__(self):
        return f'{self.i}, {self.j}, {self.k}, {self.m}'

a = Vector(10, 30, 25, 20)
b = Vector(2, 3, 5, 10)
c = Vector(2, 3, 5, 10)
#           (14, 36, 35, 40)
#           (-5, 0, -4)
#           (6, 9, 21, 200)
#           (5, 10, 5, 2)
# 1i + 3j + 3k 
# 6i + 3j + 7k 
# 7i + 6j + 10k

print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Name is {self.name}'

user = Person('John')
# user.show()
# print(user.name)
# print(user)

def add(*args): #*args stores an iterable object
    return sum(args)

# print(add(10, 5, 4 , 5 , 8, 9, 10, 10 , 80, 10, 20, 50))



# lambda functions--> anonymus function (functions without name)

# lambda arguments : expression

add = lambda x, y: x + y

# def add(a, b):
#     return a + b

# print(add(2, 4))

a = [1, 2, 3, 5]
#output -> [1, 4, 9, 25]

squared = list(map(lambda x: x**2, a))
# print(squared)

#map returns an iterable object