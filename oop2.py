def greet():
    print('hello there')

# greet()

#rotation


# lst = [4, 5, 1, 2, 3]
k = 3
#output = [1, 2, 3, 4, 5]

def rotate_list(lst, k):
    k = k % len(lst) #3

    rotated = lst[-k:] + lst[:-k]

    return rotated


lst = [1, 2, 3, 4, 5] 
k = 2
#expected -> [4, 5, 1, 2, 3]
roatated = rotate_list(lst, k)
print(roatated)
print(rotate_list(lst, k))
# print(len(lst))

# print(lst[-3:]) #len(lst) - 3 = 7 -3 = 4
# print(lst[:4]) #0th index - len(lst) - k
# # print(lst[4:]) #len(lst) - 3 = 7 -3 = 4

