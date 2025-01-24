#prime numbers -> 5 -> 1 & 5

# num = 0

# if num > 1:
#     for i in range(2, (num // 2) + 1):
#         if(num % i) == 0:
#             print('not prime')
#             break
#     else:
        # print('prime')

def prime(num):
    if num < 1:
        return False
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True
print(prime(11))
if(prime(10)):
    print('prime')
else:
    print('not prime')

print(int(11 ** 0.5) )
# for i in range(2, num ):
#     # if(i == 6):
#     #     break
#     print(i)
        

# print(num / 2)
# print(num // 2)

# for i in range(1, 5 + 1):
#     print(i)

# fibonacci 0 1 1 2 3 