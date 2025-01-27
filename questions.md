### Attempt all questions if you're having trouble in solving than we will have a separate class for questions

### **Easy Questions**:
1. **Adding and Removing Elements**  
   Write a program to create a set, add the numbers 5, 10, and 15 to it, and then remove the number 10.

2. **Set Union**  
   Write a program to find the union of two sets:  
   ```python
   set1 = {1, 2, 3}  
   set2 = {3, 4, 5}
   ```

---

### **Intermediate Questions**:
3. **Unique Elements in a List**  
   Write a program that takes a list as input and prints the unique elements using a set.  
   Example: Input: `[1, 2, 2, 3, 4, 4, 5]`, Output: `{1, 2, 3, 4, 5}`.

4. **Common Elements Between Two Lists**  
   Write a program to find the common elements between two lists using sets.  
   Example: List1 = `[1, 2, 3, 4]`, List2 = `[3, 4, 5, 6]`, Output: `{3, 4}`.

5. **Set Difference**  
   Write a program to find the difference between two sets:  
   ```python
   set1 = {10, 20, 30, 40}  
   set2 = {30, 40, 50, 60}
   ```  
   Output: `{10, 20}`.

---

Here are **5 practice questions** based on the topics of strings:

---

### **Easy Questions**:
1. Write a program to remove leading and trailing spaces from the string:  
   **Input**: `"  Hello, World!  "`  
   **Output**: `"Hello, World!"`

2. Write a program to replace all occurrences of the word `"Python"` with `"Java"` in the string:  
   **Input**: `"I love Python. Python is amazing!"`  
   **Output**: `"I love Java. Java is amazing!"`

---

### **Intermediate Questions**:
3. Write a program to check if two strings are anagrams.  
   **Input**: `"listen"`, `"silent"`  
   **Output**: `"These are anagrams."`

4. Write a program to capitalize the first letter of each word in a sentence.  
   **Input**: `"python programming is fun"`  
   **Output**: `"Python Programming Is Fun"`

5. Write a program to find and replace all vowels in a string with the character `"*"`.  
   **Input**: `"Hello, World!"`  
   **Output**: `"H*ll*, W*rld!"`

---

Here are **5 practice questions** for **File Handling**:

---

### **Easy Questions**:
1. Write a program to open a file in read mode (`r`) and print its contents line by line.  
   **Input**: A file named `sample.txt` with the content:  
   ```
   Hello, World!
   Welcome to Python File Handling.
   ```
   **Output**:  
   ```
   Hello, World!
   Welcome to Python File Handling.
   ```

2. Write a program to append user input to a file using the append mode (`a`).  
   **Input**: Append `"Learning File Handling"` to a file named `data.txt`.

---

### **Intermediate Questions**:
3. Write a program to count the number of lines, words, and characters in a given file.  
   **Input**: A file named `text.txt` with the content:  
   ```
   Python is amazing.
   File handling is simple.
   ```
   **Output**:  
   ```
   Lines: 2  
   Words: 6  
   Characters: 38
   ```

4. Write a program to copy the content of one file to another.  
   **Input**: Source file `source.txt` and target file `target.txt`.  
   **Output**: The content of `source.txt` should be written into `target.txt`.

5. Write a program to read a file and count how many times a specific word (e.g., `"Python"`) appears in the file.  
   **Input**: A file named `example.txt` with the content:  
   ```
   Python is fun. Learning Python is exciting.
   ```  
   **Output**:  
   ```
   The word 'Python' appears 2 times.
   ```

---

Here are **5 practice questions** for **Day 6: Error Handling**:

---

### **Easy Questions**:
1. Write a program that handles division by zero using a `try`-`except` block.  
   **Input**: `10 / 0`  
   **Output**: `"Error: Division by zero is not allowed."`

2. Write a program to handle invalid input errors using `try`-`except`.  
   **Input**: Prompt the user to enter a number. If the input is not a number, display an error message.  
   **Output**:  
   - Input: `"abc"`  
   - Output: `"Error: Invalid input. Please enter a number."`

---

### **Intermediate Questions**:
3. Write a program to handle multiple exceptions (e.g., `ZeroDivisionError` and `ValueError`).  
   **Input**: Ask the user to enter two numbers and divide the first by the second.  
   **Output**:  
   - Input 1: `10`, `0`  
     Output: `"Error: Division by zero is not allowed."`  
   - Input 2: `"abc"`, `5`  
     Output: `"Error: Invalid input. Please enter a valid number."`

4. Write a program that uses `try`, `except`, and `finally` to handle file-related errors.  
   **Task**: Open a file, read its contents, and print them. If the file does not exist, catch the error and display a message. Always print `"Operation complete."` in the `finally` block.

5. Write a program to simulate an ATM withdrawal. Catch errors for invalid inputs (e.g., non-numeric amounts) and insufficient funds.  
   **Input**: Current balance = `5000`.  
   - Input 1: Withdraw amount = `"abc"`  
     Output: `"Error: Invalid amount entered."`  
   - Input 2: Withdraw amount = `6000`  
     Output: `"Error: Insufficient funds."`  
   - Input 3: Withdraw amount = `3000`  
     Output: `"Transaction successful. Remaining balance: 2000."`
---
Here are **10 intermediate Python programming questions** that cover a variety of topics:

---

### **1. List Manipulation**  
Write a program to rotate a list to the right by `k` steps.  
**Input**: `lst = [1, 2, 3, 4, 5], k = 2`  
**Output**: `[4, 5, 1, 2, 3]`

---

### **2. String Manipulation**  
Write a program to count the frequency of each character in a string (case-insensitive).  
**Input**: `"HelloWorld"`  
**Output**: `{'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}`

---

### **3. Dictionary Operations**  
Write a program to merge two dictionaries. If a key exists in both, add their values.  
**Input**:  
`dict1 = {'a': 10, 'b': 20}, dict2 = {'b': 30, 'c': 40}`  
**Output**: `{'a': 10, 'b': 50, 'c': 40}`

---

### **4. File Handling**  
Write a program to read a file and print the top 3 most frequent words along with their frequencies.  
**Input File**:  
```
Python is great. Python is dynamic. Python is fun.
```
**Output**:  
```
Python: 3  
is: 3  
great: 1
```

---

### **5. Set Operations**  
Write a program to find all elements that are present in either of the two sets but not in both.  
**Input**: `set1 = {1, 2, 3, 4}, set2 = {3, 4, 5, 6}`  
**Output**: `{1, 2, 5, 6}`

---

### **6. Nested Loops**  
Write a program to generate the following pattern:  
```
1  
1 2  
1 2 3  
1 2 3 4  
1 2 3 4 5
```

---

### **7. Error Handling**  
Write a program that takes two inputs and divides the first by the second. Handle cases where the input is not a number or the denominator is zero.  

---

### **8. Sorting**  
Write a program to sort a list of dictionaries by a key.  
**Input**:  
```python
students = [{'name': 'Alice', 'marks': 85}, {'name': 'Bob', 'marks': 92}, {'name': 'Charlie', 'marks': 78}]
```  
**Output**:  
```python
[{'name': 'Charlie', 'marks': 78}, {'name': 'Alice', 'marks': 85}, {'name': 'Bob', 'marks': 92}]
```

---

### **9. Prime Numbers**  
Write a program to generate all prime numbers between 1 and `n`.  
**Input**: `n = 20`  
**Output**: `[2, 3, 5, 7, 11, 13, 17, 19]`

---

### **10. Fibonacci Sequence**  
Write a program to print the Fibonacci sequence up to the `n`th term using a loop.  
**Input**: `n = 7`  
**Output**: `[0, 1, 1, 2, 3, 5, 8]`

--- 
Here are 10 Object-Oriented Programming (OOP) questions focusing on classes, constructors, getters, setters, and access modifiers. These are of intermediate level and avoid advanced concepts.

---

### **1. Basic Class**
Write a program to define a class `Person` with an attribute `name` and a method `greet` that prints "Hello, my name is [name]".  
Input: `name = "Alice"`  
Output:  
```
Hello, my name is Alice
```

---

### **2. Class with Constructor**
Create a class `Rectangle` with attributes `length` and `breadth`. Write a method `area` that returns the area of the rectangle.  
Input: `length = 5, breadth = 3`  
Output:  
```
Area: 15
```

---

### **3. Getters and Setters**
Define a class `Student` with attributes `name` and `grade`. Use a getter to retrieve the grade and a setter to update it. Ensure the setter validates the grade (must be between 0 and 100).  
Input:  
```python
student.name = "John"
student.set_grade(85)
print(student.get_grade())
```  
Output:  
```
85
```

---

### **4. Private Attributes**
Write a program to create a class `BankAccount` with private attributes `balance` and `account_number`. Add a method to display the balance and another method to deposit money, updating the balance.  
Input:  
```python
account.deposit(500)
account.display_balance()
```  
Output:  
```
Balance: 500
```

---

### **5. Public and Private Methods**
Create a class `Calculator` with a public method `add` and a private method `_square`. Use `add` to add two numbers and internally call `_square` to return the square of the sum.  
Input: `a = 3, b = 2`  
Output:  
```
Addition: 5
Square of the sum: 25
```

---

### **6. Class with Multiple Methods**
Define a class `Circle` with an attribute `radius`. Add methods to calculate the diameter, circumference, and area of the circle.  
Input: `radius = 7`  
Output:  
```
Diameter: 14
Circumference: 43.96
Area: 153.86
```

---

### **7. Class with Validation**
Create a class `Employee` with attributes `name` and `salary`. Use a setter for `salary` to ensure it is not negative. If it is, set it to 0 by default.  
Input:  
```python
emp.set_salary(-5000)
print(emp.get_salary())
```  
Output:  
```
Salary: 0
```

---

### **8. Class with Default Constructor**
Define a class `Book` with attributes `title`, `author`, and `price`. Use a default constructor to initialize these attributes and a method to display book details.  
Input:  
```python
book.title = "Python Basics"
book.author = "John Doe"
book.price = 299
book.display_details()
```  
Output:  
```
Title: Python Basics
Author: John Doe
Price: 299
```

---

### **9. Combining Getters and Setters with Computations**
Create a class `Triangle` with attributes `base` and `height`. Use getters and setters for both. Add a method to compute the area of the triangle using these attributes.  
Input: `base = 10, height = 5`  
Output:  
```
Area: 25
```

---

### **10. Class Interaction**
Write a program with two classes, `Student` and `Subject`. The `Student` class should have a method `add_subject` to store subjects in a list. The `Subject` class should store the name of the subject.  
Input:  
```python
student.add_subject("Math")
student.add_subject("Science")
print(student.get_subjects())
```  
Output:  
```
Subjects: ['Math', 'Science']
```

---
Here are **10 Python program questions** that gradually progress from basics to object-oriented programming (OOP). These are slightly above intermediate level to give a good challenge while covering a variety of Python concepts.

---

### **1. Basic: Reverse a String**  
Write a program to reverse a string without using built-in functions.  
Input: `"hello"`  
Output: `"olleh"`

---

### **2. List: Find the Second Largest Number**  
Write a program to find the second largest number in a list.  
Input: `[10, 20, 4, 45, 99]`  
Output: `45`

---

### **3. Dictionary: Frequency Counter**  
Write a program to count the frequency of each character in a string using a dictionary.  
Input: `"programming"`  
Output:  
```
{'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}
```

---

### **4. Tuples: Swap Two Variables Without Using a Third Variable**  
Write a program to swap two variables using tuples.  
Input: `a = 5, b = 10`  
Output:  
```
After swapping: a = 10, b = 5
```

---

### **5. File Handling: Word Counter**  
Write a program to count the number of lines, words, and characters in a file.  
Input: A text file with the content:  
```
Hello world
Python is fun
```  
Output:  
```
Lines: 2
Words: 5
Characters: 25
```

---

### **6. Functions: Generate Fibonacci Sequence**  
Write a program to generate the Fibonacci sequence up to the nth term using a function.  
Input: `n = 7`  
Output: `[0, 1, 1, 2, 3, 5, 8]`

---

### **7. Error Handling: Handle Division by Zero**  
Write a program that asks for two numbers and divides them. Use `try` and `except` to handle division by zero errors gracefully.  
Input:  
```
Enter numerator: 10  
Enter denominator: 0  
```  
Output:  
```
Error: Cannot divide by zero.
```

---

### **8. Class with Constructor**  
Define a class `Rectangle` with attributes `length` and `breadth`. Write a method to calculate the perimeter of the rectangle.  
Input:  
```python
rect = Rectangle(4, 7)
print(rect.perimeter())
```  
Output:  
```
22
```

---

### **9. Private Attributes with Getter and Setter**  
Create a class `BankAccount` with a private attribute `balance`. Use a getter method to display the balance and a setter method to deposit money (ensure the deposit amount is positive).  
Input:  
```python
account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())
```  
Output:  
```
Balance: 1500
```

---

### **10. Inheritance: Animal and Dog (will discuss soon)**  
Write a program with a base class `Animal` that has a method `sound`. Create a derived class `Dog` that overrides the `sound` method to print "Bark".  
Input:  
```python
dog = Dog()
dog.sound()
```  
Output:  
```
Bark
```

---
Here are **10 Python program questions** focused on **single inheritance**. These include scenarios with and without constructors and basic method overriding.

---

### **1. Inheritance Without Constructor: Parent-Child Relationship**  
Create a base class `Animal` with a method `eat()` that prints `"Animals eat food"`. Create a derived class `Dog` that inherits from `Animal` and adds a method `bark()` to print `"Dogs bark"`.  
**Input**:  
```python
dog = Dog()
dog.eat()
dog.bark()
```

**Output**:  
```
Animals eat food  
Dogs bark  
```

---

### **2. Inheritance With Constructor: Parent Initialization in Child**  
Create a class `Person` with a constructor that initializes `name` and `age`. Create a subclass `Employee` that adds a `job_title` attribute. Display the name, age, and job title.  
**Input**:  
```python
emp = Employee("Alice", 30, "Developer")
emp.display_info()
```

**Output**:  
```
Name: Alice  
Age: 30  
Job Title: Developer  
```

---

### **3. Method Overriding: Display Information**  
Create a class `Vehicle` with a method `description()` that prints `"This is a vehicle."`. Override the `description()` method in a derived class `Car` to print `"This is a car."`.  
**Input**:  
```python
v = Vehicle()
v.description()

c = Car()
c.description()
```

**Output**:  
```
This is a vehicle.  
This is a car.  
```

---

### **4. Parent Method Call in Overridden Method**  
Modify the previous question so that the overridden `description()` method in the `Car` class also calls the `description()` method from the `Vehicle` class.  
**Input**:  
```python
c = Car()
c.description()
```

**Output**:  
```
This is a vehicle.  
This is a car.  
```

---

### **5. Inheritance Without Constructor: Adding Methods in Child Class**  
Create a base class `Shape` with a method `area()` that prints `"Calculating area..."`. Create a subclass `Circle` that adds a method `calculate_area(radius)` to calculate and print the area of a circle.  
**Input**:  
```python
circle = Circle()
circle.area()
circle.calculate_area(5)
```

**Output**:  
```
Calculating area...  
Area of the circle: 78.5  
```

---

### **6. Inheritance With Constructor: Initialize Parent and Child Attributes**  
Create a base class `Account` with attributes `name` and `balance`. Create a subclass `SavingsAccount` that adds an attribute `interest_rate`. Write a method in `SavingsAccount` to calculate and display interest earned.  
**Input**:  
```python
account = SavingsAccount("John", 1000, 5)
account.display_interest()
```

**Output**:  
```
Interest earned: 50.0  
```

---

### **7. Accessing Parent Method from Child**  
Create a base class `Device` with a method `power_on()` that prints `"Device is powering on."`. Create a subclass `Phone` that overrides `power_on()` to print `"Phone is powering on."`, but also calls the parent method.  
**Input**:  
```python
p = Phone()
p.power_on()
```

**Output**:  
```
Device is powering on.  
Phone is powering on.  
```

---

### **8. Single Inheritance Without Constructor: Extending Functionality**  
Create a class `Book` with a method `details()` that prints `"Books contain knowledge."`. Create a subclass `EBook` that adds a method `download()` to print `"Downloading ebook..."`.  
**Input**:  
```python
ebook = EBook()
ebook.details()
ebook.download()
```

**Output**:  
```
Books contain knowledge.  
Downloading ebook...  
```

---

### **9. Single Inheritance With Constructor and Overriding**  
Create a class `Animal` with a constructor that initializes `name`. Create a subclass `Bird` that overrides the constructor to also include `can_fly` attribute and display both values.  
**Input**:  
```python
bird = Bird("Parrot", True)
bird.display_info()
```

**Output**:  
```
Name: Parrot  
Can Fly: True  
```

---

### **10. Method Overriding and Adding New Methods**  
Create a base class `BankAccount` with a method `withdraw()` that prints `"Withdraw from BankAccount"`. Create a subclass `CurrentAccount` that overrides `withdraw()` and adds a new method `overdraft_limit()`.  
**Input**:  
```python
account = CurrentAccount()
account.withdraw()
account.overdraft_limit()
```

**Output**:  
```
Withdraw from CurrentAccount  
Overdraft limit is $500  
```

---

These questions cover single inheritance with constructors, method overriding, and basic use of parent and child class methods. Let me know if you need solutions or further clarification! 😊
