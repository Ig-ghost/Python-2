#strings --> sequence of characters

s = "python"
s2 = 'language' #string
# print(s2)

# print(s2[0])
# print(s2[1])

#multi line strings

s3 = """I am learning 
python"""

s4 = '''a quick brown
fox jumps over
the lazy dog'''
# print(s4[10])

#access using negative indexes

s5 = 'python'
# print(s5[-2]) #lenghth of string - (negative index value) 6 - 1 = 5
# print(s5[5])

#slicing --> extract a portion from a string through start and ending indexes


# print(s[1:5])

# print(s[:4])

# print(s[2:])

#reversing a string

#immutable 

# print(s[::-1])
# s[0] = 'i'

# del s
# print(s)

#updating a string

s = 'pythonclass'

s1 = "h" + s[1:]
# print(s1)

#replace

s = 'hello world'
# print(s)
s2 = s.replace('hello', 'there')
# print(s2)

#common methods

# print(len(s))

# print(s.upper())
# print(s.lower())
# s = '   Py Thon    '
# print(s)
# print(s.strip())

#concatenation of strings

s1 = 'hello'
s2 = 'world'

s3 = s1 +' '+ s2
# print(s3)

#repeating strigs

s = 'python'
# print(s * 5)

#using f string -> formatting strings

name = 'sanjay'
age = 19
# print(f'Name : {name}, Age : {age}')

# print('my name is {} and my age is {}'.format('Mahak', 20))

#in keyword

s = 'myfavlangispython'
# print('Python' in s)

#count the number of vowels in string

s = 'pytaeiouhon'

def count_vowels(string):
    vowels = 'aeiouAEIOU'

    count = 0

    for char in string:
        if char in vowels:
            count += 1

    return count

print(count_vowels(s))

#palindrome
a = 'amanaplanacanalpanama'
def is_palindrome(string):
    cleaned_string = string.replace(' ', '').lower()

    return cleaned_string == cleaned_string[::-1]

if is_palindrome(a):
    print('string is palindrome')
else:
    print('string is not plaindrome')