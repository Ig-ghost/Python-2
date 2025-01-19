#dictionaries --> key value pairs

student = {
    'name' : 'mahak',
    'age' : 18,
    'subjects' : ['maths', 'python', 'science']
}
# print(type(student))
# print(student)

# print(student['name'])
# print(student['age'])

# #dictionary operations
# print(student)
# student['grade'] = 'A'
# print(student)

#largest of three numbers

#10 20 30 --> 30

a = 0
b = 20

# if a > b:
#     print('a is greater', a)
# elif a == b:
#     print('both values are equal')
# elif a == 0:
#     print(' a is 0')
# else:
#     print('b is greater', b)

#logical operators --> AND OR NOT

# print(20 > 3 and 8 > 4 and 5 == 5)
#      false    true        false

#and 
#true false -> false
#false true  -> false
#true true -> true

# print(5 > 30 or 4 > 7 or 9 == 9)

# print(3 != 3) #not equals

#greatest of three numbers

# def largest_of_three(x, y, z):
#     if x > y and x > z:
#         return x
#     elif y > x and y > z:
#         return y
#     else:
#         return z
    
# great = largest_of_three(100, 200, 30)
# print(great)


#adding numbers of list
# numbers = [10, 2, 3, 4, 5, 6] #21
# print(sum(numbers))

# sum = 0
# for n in numbers:
#     sum = sum + n #0 + 1 + 2 + 3 ... + 6

# print(sum)

#factorial 5! = 5*4*3*2*1 = 120

# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result = result * i
#     return result

# print(factorial(6))

#swapping two numbers

# a = 10
# b = 20

# print('a =', a) #a = 20
# print('b =', b) #b = 10

# a, b = b, a
# print('a =', a) #a = 20
# print('b =', b) #b = 10

# lst = [1, 2, 3, 40, 5, 6]
# print(max(lst))
# print(min(lst))

#counting vowels -> aeiou

#pytohon #output 2

def count_vowels(string): #argument
    vowels = 'aeiouAEIOU'
    count = 0
    for s in string:
        if s in vowels: #in -> membership operator
            # count = count + 1
            count += 1
    return count

print(count_vowels('aaa'))

# string = 'python'
# for s in string:
#     print(s)