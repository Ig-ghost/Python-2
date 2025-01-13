#file handling --> process of performing operations on files such as creating file, opening, reading, writing, closing it


#modes -> r(read mode), w(write mode), a(append mode), b(binary mode)

#read mode
# file = open('myfile.txt', 'r')
# content = file.read()
# print(content)
# file.close()

#write mode
# file = open('myfile.txt', 'w')
# file.write('we are not learning java')
# file.close()

#append mode
# file = open('myfile1.txt', 'a')
# file.write('but we will start soon')
# file.write('but we will start soon')
# file.close()

#with statement

# with open('myfile2.txt', 'w') as file:
#     file.write('hello world')

# #read and write mode
# with open('myfile.txt', 'r+') as file:
#     file.write('hey there')
#     content = file.read()

#file handling programs

#read a file and print number of lines, words and characters

def count_file_details(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    num_lines = len(lines)
    num_words = sum(len(line.split()) for line in lines)
    num_chars = sum(len(line) for line in lines)

    print(f'number of lines : {num_lines}')
    print(f'number of words : {num_words}')
    print(f'number of chars : {num_chars}')

# count_file_details('myfile.txt')
# print(sum([1, 2]))

#write user input to the file

def write_user_input(file_name):
    with open(file_name, 'a') as file:
        while True:
            user_input = input('Enter text (enter "exit" to exit) : ')
            if user_input.lower() == 'exit':
                break
            file.write(user_input + ' ')

write_user_input('user.txt')