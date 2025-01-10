#dictionaries -> stores the data in key value pairs.

d = {
    1 : 'one',
    2 : 'two',
    3 : 'three'
}

# print(d)
# print(type(d))

#using dictionary constructor

d2 = dict(a = 1, A = 'two', c = 'three')
# print(d2)

#case sensitive
#keys must be unique



# #accesing elements
# print(d3.get('name'))
# print(d3.get('lang'))

# #adding element
# d3['age'] = 20

# #updating value
# d3['name'] = 'ravi'
# print(d3)

#removing items

d3 = {
    'name' : 'Sanjay',
    'lang' : 'Python'
}

# del d3['name']
# print(d3)

#pop -> returns the value

# val = d3.pop('lang')
# print(val)

#popitem -> return key and value

key, val = d3.popitem()
# print(f'key : {key}, value : {val}')

# name = 'mohit'
# occ = 'dev'
# print(name, "is a", occ)
# print(f'{name} is a {occ}')

#iteration in dictionary


#iterate over keys
# for key in d4:
#     print(key)

#iterate over values
# for value in d4.values():
#     print(value)

#iterate over keys and values together
# for key, value in d4.items():
#     print(f'{key} : {value}')


#dictionary methods

d4 = {
    'name' : 'ravi',
    'occ' : 'dev',
    'age' : 22,
    'lang' : 'Python'
}
# print(d4)
# d4.clear()
# print(d4)

# print(d4.get('occ'))

# print(list(d4.keys()))

d5 = {
    'name' : 'john',
    'lang' : 'c'
}

# d4.update(d5)
# print(d4)

# print(list(d4.values()))

d4.pop('name')
print(d4)

#counting frequncy of characters in a string
#ppython

#p 2 y 1 t 1 h 1 o n

def count_freq(input_string):
    words = input_string.split()
    
    word_count = {}

    for word in words:
        word = word.lower()
        word_count[word] = word_count.get(word, 0) + 1

    return word_count


res = count_freq('python is is a language')

for word, count in res.items():
    print(word, count)

# print('Python'.lower())

#reverse

def reverse_list(lst):
    reversed_list = []

    for i in range(len(lst) -1, -1, -1):
        lst.append(lst[i])

    return lst

ans = reverse_list([2, 3, 4, 5, 6])
print(ans)