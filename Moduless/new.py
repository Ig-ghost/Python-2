#python modules --> to use functions classes and other

# import calc

# print(10 + 2)
# print(calc.add(10, 2))

# print(calc.subtract(10, 2))

# print(calc.mul(2,2,2))

# from calc import add

# print(add(10, 2))
# print(calc.mul(2, 2, 2))

# import math

# from math import sqrt, factorial

# print(sqrt(16))
# # 5! = 5 * 4 * 3 * 2 * 1
# print(factorial(5))

# from math import * 
# print(sqrt(25))
# print(factorial(6))

# import sys
# print(sys.path)

# import math as m
# print(m.sqrt(16))
# print(m.factorial(5))

# from math import * 
# print(sqrt(25))

# print(pi)

# print(degrees(2))

# print(radians(114.59155902616465))

# print(sin(90))

# print(cos(20))

# print(tan(60))

# print(factorial(5))

# from random import *

# # print(random() * 10)
# print(randint(0,8))

# print(random() * 100)

# lst = [1, 2, True, 'python', 'hello']
# print(choice(lst))

# print(random())

# from datetime import date
# from time import *

# print(time()) #january 1st 1970

# print(date.fromtimestamp(1737034613.1814058))

#random password generator

import random
import string

def generate_password(length = 12):
    if length < 4:
        raise ValueError ('length should be at least four')
    
    uppercase_letters = string.ascii_uppercase #A - Z
    lowercase_letters = string.ascii_lowercase #a - z
    digits = string.digits #0 - 9
    special = string.punctuation #@ # $

    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special)
    ]

    all_characters = uppercase_letters + lowercase_letters + digits + special
    password = password + random.choices(all_characters, k = length - 4)

    random.shuffle(password)

    return password

# length = int(input('Enter Length : '))
try:
    random_password = generate_password()
    print(f'Generated Password : {random_password}')
except ValueError as e:
    print(e)
# a = string.ascii_lowercase
# # print(random.choices(a, k = 9))
# all_char = string.ascii_lowercase + string.ascii_uppercase
# print(all_char)   

a = [1, 2, 3, 4]
random.shuffle(a)
print(a)