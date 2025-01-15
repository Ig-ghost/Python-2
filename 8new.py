#error handling --> handling errors during execution

# n  = 10
# try:
#     res = n / 0
# except ZeroDivisionError:
#     print('cant be divided by zero')

# print('hello')

#difference between exception and error

# print('hello')
      
# n  = 10
# num = int(input('Enter a number'))
# print(n / num)

#syntaxn of error handling

# try:
#     #code that might raise exception
#     n = 0
#     user = int(input('enter number'))
#     res = 100 / user
# except ZeroDivisionError:
#     #code to handle exception
#     print('cant be divided by zero')
# except ValueError:
#     print('Enter a valid number')
# else:
#     #if no exceptions
#     print(f'result is {res}')
# finally:
#     #runs everytime
#     print('execution completed')

# try:
#     s = int('str')

#     inv = 1 / s

# except ValueError:
#     print('not valid')

# except ZeroDivisionError:
#     print('zero has no inverse')

#catching multiple exceptions

# a = ['10', 'twenty', 30]
# try:
#     # s = int('str')

#     inv = 1 / s

# except (ValueError, TypeError) as e:
#     print('error', e)

# except IndexError:
#     print('index out of range')

# try:
#     res = '100'/20

# except TypeError:
#     print('arithmetic error')

# except:
#     print('something went wrong')

# print('100'/20)

#raising an error

def set(age):
    if age < 0:
        raise TypeError("age can't be negative")
    print(f'age is set to {age}')

try:
    set(-56)
except TypeError as e:
    print(e)