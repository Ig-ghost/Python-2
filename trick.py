a = [1, 2, 3]
b = a
b.append(4)
# print(a)

def add_to_lst(value, lst = []):
    new_lst = []
    new_lst.append(value)
    return new_lst

# print(add_to_lst(1))
# print(add_to_lst(2))
# print(add_to_lst(2))
# print(bool(0))
# print(bool([0]))
# print(bool(None))
# print(bool(' '))

# print(5 / 2)
# print(5 // 2) #floor divison
# print(5 % 2) #modulus(remainder)

s = 'hello'
# print(s[0])
s[0] = 'm'
print(s)