# General

- Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
- Why indentation is so important in Python
- How to use the if, if ... else statements
- How to use comments
- How to affect values to variables
- How to use the while and for loops
- How is Python’s for different from C‘s?
- How to use the break and continues statements
- How to use else clauses on loops
- What does the pass statement do, and when to use it
- How to use range
- What is a function and how do you use functions
- What does return a function that does not use any return statement
- Scope of variables
- What’s a traceback
- What are the arithmetic operators and how to use them

## Projects

### 0. Positive anything is better than negative nothing

This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print whether the number stored in the variable number is positive or negative.

- You can find the source code here
- The variable number will store a different value every time you will run this program
- You don’t have to understand what import, random. randint do. Please do not touch this code
- The output of the program should be:
    - The number, followed by
        - if the number is greater than 0: is positive
        - if the number is 0: is zero
        - if the number is less than 0: is negative
    - followed by a new line

### 1. The last digit 

This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable number.

- You can find the source code here
- The variable number will store a different value every time you will run this program
- You don’t have to understand what import, random.randint do. Please do not touch this code. This line should not change: number = random.randint(-10000, 10000)
- The output of the program should be:
    - The string Last digit of, followed by
    - the number, followed by
    - the string is, followed by the last digit of number, followed by
        - if the last digit is greater than 5: the string and is greater than 5
        - if the last digit is 0: the string and is 0
        - if the last digit is less than 6 and not 0: the string and is less than 6 and not 0
    - followed by a new line

### 2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game 

Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

- You can only use one print function with string format
- You can only use one loop in your code
- You are not allowed to store characters in a variable
- You are not allowed to import any module

### 3. When I was having that alphabet soup, I never thought that it would pay off 

Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

- Print all the letters except q and e
- You can only use one print function with string format
- You can only use one loop in your code
- You are not allowed to store characters in a variable
- You are not allowed to import any module

### 4. Hexadecimal printing 

Write a program that prints all numbers from 0 to 98 in decimal and in hexadecimal (as in the following example)

- You can only use one print function with string format
- You can only use one loop in your code
- You are not allowed to store numbers or strings in a variable
- You are not allowed to import any module

### 5. 00...99

Write a program that prints numbers from 0 to 99.

- Numbers must be separated by ,, followed by a space
- Numbers should be printed in ascending order, with two digits
- The last number should be followed by a new line
- You can only use no more than 2 print functions with string format
- You can only use one loop in your code
- You are not allowed to store numbers or strings in a variable
- You are not allowed to import any module

### 6. Inventing is a combination of brains and materials. The more brains you use, the less material you need 

Write a program that prints all possible different combinations of two digits.

- Numbers must be separated by ,, followed by a space
- The two digits must be different
- 01 and 10 are considered the same combination of the two digits 0 and 1
- Print only the smallest combination of two digits
- Numbers should be printed in ascending order, with two digits
- The last number should be followed by a new line
- You can only use no more than 3 print functions with string format
- You can only use no more than 2 loops in your code
- You are not allowed to store numbers or strings in a variable
- You are not allowed to import any module

### 7. islower

Complete this source code

- You can find the source code here
- You are not allowed to use any loops or conditional statements
- Your program should be exactly 8 lines long
- word_first_3 should contain the first 3 letters of the variable word
- word_last_2 should contain the last 2 letters of the variable word
- middle_word should contain the value of the variable word without the first and last letters

### 8. To uppercase

Complete this source code to print object-oriented programming with Python, followed by a new line.

- You can find the source code here
- You are not allowed to use any loops or conditional statements
- Your program should be exactly 5 lines long
- You are not allowed to create new variables
- You are not allowed to use string literals

### 9. There are only 3 colors, 10 digits, and 7 notes; it's what we do with them that's important 

Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.
Your script should be maximum 98 characters long (please check with wc -m 9-easter_egg.py)

### 10. a + b

Technical interview preparation:

- You are not allowed to google anything
- Whiteboard first
- This task and all future technical interview prep tasks will include checks for the efficiency of your solution, i.e. is your solution’s runtime fast enough, does your solution require extra memory usage / mallocs, etc.
Write a function in C that checks if a singly linked list has a cycle in it.

- Prototype: int check_cycle(listint_t *list);
- Return: 0 if there is no cycle, 1 if there is a cycle
Requirements:

- Only these functions are allowed: write, printf, putchar, puts, malloc, free

### 11. a ^ b

Write a Python script that prints exactly and that piece of art is useful - Dora Korpar, 2015-10-19, followed by a new line.

- Use the function write from the sys module
- You are not allowed to use print
- Your script should print to stderr
- Your script should exit with the status code 1
- (Dora Korpar was a Holberton student in Cohort 0 of San Francisco)

### 12. Fizz Buzz 

Write a script that compiles a Python script file.
The Python file name will be stored in the environment variable $PYFILE
The output filename has to be $PYFILEc (ex: export PYFILE=my_main.py => output filename: my_main.pyc)

### 13. Insert in sorted linked list 

Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode: