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
