num = 15

# print(10 % 2)

# if num % 2 == 0:
#     print('number is even')
# elif num % 3 == 0:
#     print('divisible by 3')
# else:
#     print('number is odd')

#loops

# for i in range(6):
#     print(i,'hello world')

# n = 5
# while n > 0: #n = 5, n = 4, n = 3, n = 2, n = 1, n = 0 false
#     print(n)
#     n = n - 1 # n = 4, n = 3, n = 2, n = 1, n = 0

# for i in range(5): #0 1 2 3 4 
#     print('hello world')

#functions

def welcome(): #defining the function
    print('hello user')

# welcome() #calling the function

def add(a, b, c): #arguments
    print(a + b + c)

# add(100, 20, 50) #parameters

# def multiply(a, b):
#     print(a * b)

# multiply(10, 5)

# def multiply(a,b):
#     return a * b

# a = multiply(10, 3)
# print(a)

#list -> type of array

    #0   1   2   3   4 
# print(a)
# print(type(a))
# print(a[0])
# print(a[3])

#list operations
a = [20, 25, 26, 89, 56, 20]
print(a)
# a.append(50)
# a.append(50)
# print(a)
# a.remove(26)
# print(a)

print(sorted(a))