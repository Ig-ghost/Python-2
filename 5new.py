#set -> collection of items
#no duplicate items
#unordered collection
#mutable -> After creation you can add delete and perform other operations

s = {10, 20, 30}
# print(s)
# print(type(s))

#typecasting
# lst = ['a', 'b', 'c']
# print(lst)
# print(type(lst))
# s = set(lst)
# print(s)
# print(type(s))

s = {'hey', 'there', 'hey', 'there'} 
# s[0] = 'hello'

s = {'ravi', 10, 12.5, True}
print(s)


# print(people)

# people.add('Mohit')
# print(people)

# for i in range(1, 6):
#     people.add(i)

# print(people)

people = {'Jay', "Sanjay", 'Chandni', 'jatin'}
heroes = {'ironman', 'spiderman'}
villians = {'thanos', 'amrishpuri'}

# population = people.union(heroes)
# print(population)

# population = people | heroes
# print(population)




# set3 = set1.intersection(set2)

# set3 = set1 & set2
# print(set1)
# print(set2)
# print(set3)

#difference

set1 = set()
set2 = set()

for i in range(5):
    set1.add(i)

for i in range(2, 9):
    set2.add(i)

# set3 = set2.difference(set1)

# set3 = set2 - set1
# print(set2)
# print(set1)
# print(set3)

set4 = {1, 2, 3,4, 5, 6}
# print(set1)
# set4.clear()
# print(set4)

# for x in set4:
#     print(x)

lst = [1, 1, 2, 2, 3, 3, 3]

def find_unique(lst):
    unique_elem = set(lst)

    return list(unique_elem)

print(find_unique(lst))

#pass two lists and return common elements

def common(l1,l2):
    lst=set(l1).intersection(set(l2))
    return lst

print(common([1, 2, 3], [1, 2, 5]))

newset = {'apple', 'banana'}
# print('banana' in newset)

set = {"Apple", "Banana", "Cherry", "Date"}
search_value = "Banana"
for item in set:
    if item == search_value:
        print(f"The value '{search_value}' is found in the set.")
        break
else:
    print(f"The value '{search_value}' is not in the set.")