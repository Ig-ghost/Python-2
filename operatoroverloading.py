#operator overloading
# + - / * 

# print(4 + 3)
# print('course' + 'nit')

# print(3 * 4)
# print('python' * 4)

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    #dunder methods / magic methods
    def __add__(self, other):
        return self.x + other.x, self.y + other.y, self.z + other.z# 4 + 5, 15 + 6
    
    def __sub__(self, other):
        return self.x - other.x, self.y - other.y, self.z - other.z
    
    def __mul__(self, other):
        return self.x * other.x, self.y * other.y, self.z * other.z
    
    def __truediv__(self, other):
        return self.x / other.x, self.y / other.y, self.z / other.z

a = Vector(10, 50, 40)
b = Vector(5, 10, 4)
c = Vector(5, 10, 4)
#output -> 9, 11, 7
#output -> -1, -1, 1
#output -> 20, 30, 12
#output -> 2, 5, 10
# print(a + b)
# print(Vector.__add__(a, b))

# print(a - b)
# print(Vector.__sub__(a, b))

# print(a * b)

# print(a / b)

def add(*args):
    return sum(args)

# print(add(2, 5, 5, 5, 6, 8, 7))

a = ( 1, 2, 3, 4, 5,6 )
print(sum(a))

#lambda functions -> functions without name
#lambda -> lambda arguments : expression
add = lambda a = 4, b = 6: a + b
print(add())

def add(a, b):
    return a + b