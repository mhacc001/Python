# -*- coding: utf-8 -*-
"""Copy of Intro to Python Assignment

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dxwRs8XHDX5iltAHc4AEvpw3OGe0lRxv

# Python Assignment - Google Colab Notebook

### Instructions
This assignment will test your knowledge on Python basics, control flow, data structures, and functions. You will need to write a function for each question and ensure it returns the correct output. The assignment will be automatically graded using test functions. Follow the instructions carefully for each question.

## Table of Contents

1. Question 1: Python Basics
2. Question 2: Control Flow
3. Question 3: Data Structures
4. Question 4: Functions and Critical Thinking

### Question 1: Python Basics

**Task:** Write a function named `capitalize_words` that takes a string as input and returns a new string where every word is capitalized. Assume that words are separated by spaces.

**Function Signature:**
```python
def capitalize_words(input_string):
    pass
```

**Example:**
```python
print(capitalize_words("hello world"))  # Output: "Hello World"
print(capitalize_words("python programming is fun"))  # Output: "Python Programming Is Fun"
```

<br>
<br>

### Write your code in the cell below:
"""

# This is the function that you need to populate with your code
def capitalize_words(input_string):
   return input_string.title()


    ## Write your code here
print(capitalize_words("hello world"))  # Output: "Hello World"
print(capitalize_words("python programming is fun"))  # Output: "Python Programming Is Fun"


    ### Your code ends here

# Example tests for your reference
print(capitalize_words("hello world"))  # Output: "Hello World"
print(capitalize_words("python programming is fun"))  # Output: "Python Programming Is Fun"

"""---

## Question 2: Control Flow

**Task:** Write a function named `fizz_buzz` that takes three integers as input: `start`, `end`, and `divisor`. The function should return a list of strings. For each number from `start` to `end` (inclusive), the function should:
- Add "Fizz" to the list if the number is divisible by `divisor`.
- Add the number itself as a string to the list if it is not divisible by `divisor`.

**Function Signature:**
```python
def fizz_buzz(start, end, divisor):
    pass
```

**Example:**
```python
print(fizz_buzz(1, 10, 3))  
# Output: ['1', '2', 'Fizz', '4', '5', 'Fizz', '7', '8', 'Fizz', '10']
print(fizz_buzz(5, 15, 5))  
# Output: ['Fizz', '6', '7', '8', '9', 'Fizz', '11', '12', '13', '14', 'Fizz']
```

For the range from start to end, if a number is divisible by divisor, the string "Fizz" should be added to the result list.

If a number is not divisible by divisor, the number itself should be added as a string to the result list.

For example, `fizz_buzz(1, 10, 3)` results in ['1', '2', 'Fizz', '4', '5', 'Fizz', '7', '8', 'Fizz', '10'] because 3, 6, and 9 are divisible by 3, so
`"Fizz"` is added for these numbers. The other numbers are not divisible by 3, so their string representations are added.

Similarly, `fizz_buzz(5, 15, 5)` results in ['Fizz', '6', '7', '8', '9', 'Fizz', '11', '12', '13', '14', 'Fizz'] because 5, 10, and 15 are divisible by 5, so "Fizz" is added for these numbers. The other numbers are not divisible by 5, so their string representations are added.
<br>
<br>
### Write your code in the cell below:
"""

# This is the function that you need to populate with your code
def fizz_buzz(start, end, divisor):
    result = []
    for number in range(start, end + 1):
        if number % divisor == 0:
            result.append("Fizz")
        else:
            result.append(str(number))
    return result
    ## Write your code here

print(fizz_buzz(1, 10, 3))

print(fizz_buzz(5, 15, 5))
    ### Your code ends here

# Example tests for your reference
print(fizz_buzz(1, 10, 3))
# Output: ['1', '2', 'Fizz', '4', '5', 'Fizz', '7', '8', 'Fizz', '10']
print(fizz_buzz(5, 15, 5))
# Output: ['Fizz', '6', '7', '8', '9', 'Fizz', '11', '12', '13', '14', 'Fizz']

"""---

## Question 3: Data Structures

**Task:** Write a function named `unique_elements` that takes a list of lists as input and returns a set of unique elements found in all the nested lists.



**Function Signature:**
```python
def unique_elements(nested_lists):
    pass
```

**Example:**
```python
print(unique_elements([[1, 2, 3], [2, 3, 4], [4, 5, 6]]))  
# Output: {1, 2, 3, 4, 5, 6}
print(unique_elements([[10, 20], [20, 30, 40], [10, 50]]))  
# Output: {10, 20, 30, 40, 50}
```

**Note: Sets are unordered, so don't pay too much attention to the order of the set. Just return the set that you get and make sure that it has all the values. Order is irrelevant.**

<br>
<br>

### Write your code in the cell below:
"""

# This is the function that you need to populate with your code
def unique_elements(nested_lists):
    unique_set = set()
    for sublist in nested_lists:
        unique_set.update(sublist)
    return unique_set

    ## Write your code here
print(unique_elements([[1, 2, 3], [2, 3, 4], [4, 5, 6]]))

print(unique_elements([[10, 20], [20, 30, 40], [10, 50]]))

    ### Your code ends here

# Example tests for your reference
print(unique_elements([[1, 2, 3], [2, 3, 4], [4, 5, 6]]))
# Output: {1, 2, 3, 4, 5, 6}
print(unique_elements([[10, 20], [20, 30, 40], [10, 50]]))
# Output: {10, 20, 30, 40, 50}

"""---

## Question 4: Functions and Critical Thinking

**Task:** Write a function named `word_frequency` that takes a string and returns a dictionary where the keys are words and the values are the number of times each word appears in the string. Ignore punctuation and make the function case-insensitive.

**Function Signature:**
```python
def word_frequency(input_string):
    pass
```

**Example:**
```python
print(word_frequency("Hello world! Hello everyone."))
# Output: {'hello': 2, 'world': 1, 'everyone': 1}
print(word_frequency("Python programming is fun. Programming in Python is exciting."))
# Output: {'python': 2, 'programming': 2, 'is': 2, 'fun': 1, 'in': 1, 'exciting': 1}
```

<br>
<br>

### Write your code in the cell below:
"""

# This is the function that you need to populate with your code
import string
def word_frequency(input_string):
    # Remove punctuation and make lowercase
    translator = str.maketrans('', '', string.punctuation)
    cleaned = input_string.translate(translator).lower()
    words = cleaned.split()

    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

    ## Write your code here

print(word_frequency("Hello world! Hello everyone."))
# Output: {'hello': 2, 'world': 1, 'everyone': 1}
print(word_frequency("Python programming is fun. Programming in Python is exciting."))
    ### Your code ends here

# Example tests for your reference
print(word_frequency("Hello world! Hello everyone."))
# Output: {'hello': 2, 'world': 1, 'everyone': 1}
print(word_frequency("Python programming is fun. Programming in Python is exciting."))
# Output: {'python': 2, 'programming': 2, 'is': 2, 'fun': 1, 'in': 1, 'exciting': 1}

"""

---

"""