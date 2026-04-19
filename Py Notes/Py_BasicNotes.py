# Python notes with code from here
# Python is an interpreted, high-level, general-purpose programming language
# To run your .py file use 'python filename.py' or 'python3 filename.py'
# ANCHOR - To run one particular snippet select it and then "Ctrl+Shift+P" -> "Run Python File in Terminal" (Python extension to be installed)

#NOTE 1] ___ Variables_____________
ir = 220
ii = "22rr"
hero = "IRX358"
ii = 885
# ab = "rerere"  # This would cause NameError if not defined first

"""
Python variables are dynamically typed and don't need explicit declaration
Variable naming rules:
- Can contain letters, numbers, underscores
- Cannot start with a number
- Case sensitive
- Cannot use Python keywords
"""

print(ir)
# Print multiple values using f-strings or comma separation
print(f"Values: {ir}, {ii}, {hero}")

#NOTE 2] ___ Data Types and Type System___________
# Python is dynamically typed but strongly typed
# Built-in data types in Python

# Primitive/Basic data types
name = "ir"  # string datatype (immutable)
age = 18  # integer datatype (unlimited precision)
height = 5.8  # float datatype (64-bit double precision)
is_student = True  # boolean datatype
empty_value = None  # NoneType (similar to null in other languages)

# Complex number
complex_num = 3 + 4j

# Check data types
print(type(name))  # <class 'str'>
print(type(age))  # <class 'int'>
print(type(height))  # <class 'float'>
print(type(is_student))  # <class 'bool'>
print(type(empty_value))  # <class 'NoneType'>

# Reference types [Non-primitive]
# Lists, Tuples, Dictionaries, Sets

# List (mutable, ordered)
heros = ['iron man', 'hulk', 'thor']

# Tuple (immutable, ordered)
coordinates = (10, 20, 30)

# Dictionary (mutable, key-value pairs)
person = {
    "name": "tony stark",
    "persona": "philanthropist",
    "avenger_as": "Iron man",
    "rank": 1
}

# Set (mutable, unordered, unique elements)
unique_numbers = {1, 2, 3, 4, 5}

#NOTE - 3]___ Type Conversion____________
score = "88"
num_score = int(score)  # String to integer
float_score = float(score)  # String to float
str_score = str(88)  # Integer to string

# Boolean conversion
bool_val = bool(0)  # False
bool_val2 = bool(1)  # True
bool_val3 = bool("")  # False
bool_val4 = bool("non-empty")  # True

print(f"String '88' to int: {num_score}")
print(f"Integer 88 to string: '{str_score}'")

#NOTE - 4]___ Operators___________
value = 3
neg_value = -value  # Unary minus

print(2 + 2)  # addition
print(2 - 2)  # subtraction
print(2 * 2)  # multiplication
print(2 ** 2)  # exponentiation
print(2 / 2)  # float division
print(2 // 2)  # floor division
print(2 % 2)  # modulo

# String operations
str1 = "iir"
str2 = " ffan"
full_name = str1 + str2  # concatenation
print(f"1" + str(2) + str(2))  # o/p: 122
print(str(2) + str(1) + "2")  # o/p: 322

#NOTE - 5]___ Comparison Operators____________
"""
> , < , >= , <= : comparison operators
== : equality operator (compares values)
is : identity operator (compares memory addresses)
is not : negative identity operator
"""

a = 10
b = 10
c = [1, 2, 3]
d = [1, 2, 3]

print(a == b)  # True
print(a is b)  # True (small integers are cached)
print(c == d)  # True (same content)
print(c is d)  # False (different objects)

#NOTE 6] ___ Memory Management____________

"""
In Python:
- Primitive types (int, float, str, bool, None) are stored differently
- For small integers (-5 to 256), Python caches them for efficiency
- Lists, dictionaries, sets, and custom objects are stored in heap memory
- Variables are references to objects
"""

# Example of reference behavior
list1 = [1, 2, 3]
list2 = list1  # Both reference the same list
list2.append(4)  # Modifies the original list
print(f"list1: {list1}")  # [1, 2, 3, 4]
print(f"list2: {list2}")  # [1, 2, 3, 4]

# Creating a copy
list3 = list1.copy()  # or list1[:]
list3.append(5)
print(f"list1: {list1}")  # [1, 2, 3, 4]
print(f"list3: {list3}")  # [1, 2, 3, 4, 5]

#NOTE - 7]___ Strings__________
namee = 'ir'
projects = 5

# Poor way (old style)
print(namee + " has this many projects: " + str(projects))

# Professional way using f-strings (Python 3.6+)
print(f"Hello my name is {namee.upper()} and I have {projects} projects done...")

# String methods
text = "  Hello World  "
print(text.length if hasattr(text, 'length') else len(text))  # Python uses len()
print(text.upper())
print(text.lower())
print(text.strip())  # removes whitespace
print(text.lstrip())  # removes left whitespace
print(text.rstrip())  # removes right whitespace

text2 = "hello world python"
print(text2.split(' '))  # ['hello', 'world', 'python']
print(text2.replace(' ', '_'))  # hello_world_python
print(text2.count('o'))  # 2
print(text2.find('world'))  # 6
print(text2.startswith('hello'))  # True
print(text2.endswith('python'))  # True

#NOTE 8] ___ Numbers and Maths___________

# Number types
integer_num = 42
float_num = 3.14159
complex_num = 2 + 3j

# Number methods
num = 123.456
print(round(num, 2))  # 123.46
print(abs(-5))  # 5
print(pow(2, 3))  # 8

# Math module
import math
print(math.pi)  # 3.141592653589793
print(math.e)  # 2.718281828459045
print(math.sqrt(16))  # 4.0
print(math.ceil(4.2))  # 5
print(math.floor(4.9))  # 4
print(math.factorial(5))  # 120
print(math.gcd(48, 18))  # 6

# Random numbers
import random
print(random.random())  # Random float between 0 and 1
print(random.randint(1, 10))  # Random integer between 1 and 10
print(random.choice([1, 2, 3, 4, 5]))  # Random choice from list

# Generate random number in range
min_val = 12
max_val = 18
random_num = random.randint(min_val, max_val)
print(f"Random number between {min_val} and {max_val}: {random_num}")

#NOTE - 9]___ Date and Time____________
from datetime import datetime, date, time, timedelta

# Current date and time
now = datetime.now()
print(f"Current datetime: {now}")
print(f"Date: {now.date()}")
print(f"Time: {now.time()}")

# Format datetime
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # 2024-01-15 14:30:45
print(now.strftime("%A, %B %d, %Y"))  # Monday, January 15, 2024

# Create specific date
my_date = date(2023, 1, 23)  # Year, Month, Day
my_datetime = datetime(2023, 1, 23, 5, 30)  # Year, Month, Day, Hour, Minute

print(f"Specific date: {my_date}")
print(f"Specific datetime: {my_datetime}")

# Timestamp
timestamp = datetime.timestamp(now)
print(f"Timestamp: {timestamp}")

# Date arithmetic
today = date.today()
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)

print(f"Yesterday: {yesterday}")
print(f"Today: {today}")
print(f"Tomorrow: {tomorrow}")

#NOTE - 10]___ Lists (Arrays)____________
# Lists in Python are mutable, ordered collections
# Can contain elements of different data types
# Indexing starts from zero

arr = [2, 2, 2, 1, 3, 4, 5, True, "ir"]
arr2 = list([1, 2, 3, 4, 5, 6])  # Using list constructor

# List methods
arr2.append(7)  # Add to end
arr2.pop()  # Remove from end
arr2.insert(0, 0)  # Insert at beginning
arr2.pop(0)  # Remove from beginning
arr2.remove(3)  # Remove specific value
arr2.extend([7, 8, 9])  # Extend with another list

# List operations
print(3 in arr2)  # Check if element exists
print(arr2.index(4))  # Find index of element
print(arr2.count(2))  # Count occurrences

# Slicing
print(arr2[1:5])  # Elements from index 1 to 4 (exclusive)
print(arr2[:3])  # First 3 elements
print(arr2[-3:])  # Last 3 elements

# List comprehension
squares = [x**2 for x in range(10)]
print(f"Squares: {squares}")

# Nested lists
nested = [1, 2, 3, [4, 5, 6], 7, [8, 9, [10, 11]]]
print(f"Nested list: {nested}")

# Flatten nested list (simple case)
flat = []
for item in nested:
    if isinstance(item, list):
        flat.extend(item)
    else:
        flat.append(item)
print(f"Partially flattened: {flat}")

#NOTE 11]___ Tuples____________
# Tuples are immutable, ordered collections
# Useful for fixed collections of items

coordinates = (10, 20, 30)
single_item = (42,)  # Note the comma for single-item tuple
empty_tuple = ()

# Tuple operations
print(coordinates[0])  # Access by index
print(len(coordinates))  # Length
print(10 in coordinates)  # Check membership

# Tuple unpacking
x, y, z = coordinates
print(f"x: {x}, y: {y}, z: {z}")

# Named tuples (from collections module)
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y', 'z'])
p = Point(1, 2, 3)
print(f"Point: {p}")
print(f"x coordinate: {p.x}")

#NOTE 12]___ Dictionaries____________
# Dictionaries are mutable, unordered key-value collections
# Keys must be hashable (immutable)

# Dictionary creation
person = {
    "name": "ir",
    "age": 20,
    "location": "blore",
    "online": False,
    "last_seen": ["mon", "tue", "fri"]
}

# Accessing elements
print(person["name"])  # Using key
print(person.get("age"))  # Using get method (safer)
print(person.get("nonexistent", "default"))  # With default value

# Modifying dictionary
person["age"] = 25  # Update existing
person["email"] = "ir@example.com"  # Add new

# Dictionary methods
print(person.keys())  # Get all keys
print(person.values())  # Get all values
print(person.items())  # Get key-value pairs
print(person.pop("age"))  # Remove and return value
print(person.popitem())  # Remove and return last key-value pair

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}
print(f"Squares dictionary: {squares_dict}")

# Nested dictionaries
nested_dict = {
    "user1": {
        "name": "irfan",
        "age": 25
    },
    "user2": {
        "name": "john",
        "age": 30
    }
}
print(f"Nested dict: {nested_dict}")

#NOTE 13]___ Sets____________
# Sets are mutable, unordered collections of unique elements

# Set creation
unique_numbers = {1, 2, 3, 4, 5}
empty_set = set()  # Empty set ({} creates empty dict)
from_list = set([1, 2, 2, 3, 3, 4])  # From list (removes duplicates)

# Set operations
unique_numbers.add(6)  # Add element
unique_numbers.remove(1)  # Remove element (raises error if not found)
unique_numbers.discard(10)  # Remove element (no error if not found)

# Mathematical operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"Union: {set1.union(set2)}")  # or set1 | set2
print(f"Intersection: {set1.intersection(set2)}")  # or set1 & set2
print(f"Difference: {set1.difference(set2)}")  # or set1 - set2
print(f"Symmetric difference: {set1.symmetric_difference(set2)}")  # or set1 ^ set2

# Set methods
print(set1.issubset({1, 2, 3, 4, 5, 6}))  # True
print(set1.issuperset({1, 2, 3}))  # True

#NOTE 14]___ Basic Input/Output____________
# Getting user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))  # Convert to int

print(f"Hello {name}, you are {age} years old!")

# Formatted output
price = 19.99
quantity = 3
total = price * quantity

print(f"Price: ${price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total: ${total:.2f}")

# Using format method (older style)
print("Price: ${:.2f}, Quantity: {}, Total: ${:.2f}".format(price, quantity, total))

#NOTE 15]___ Control Flow - If Statements____________
# if-else statement
is_raining = True
if is_raining:
    print("Take an umbrella")
else:
    print("No umbrella needed")

# if-elif-else statement
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")

# Ternary operator (conditional expression)
age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Status: {status}")

# Truthy and Falsy values
"""
Falsy values in Python:
- False
- None
- 0, 0.0, 0j
- Empty sequences: "", (), [], {}
- Empty set: set()
- Custom objects with __bool__ or __len__ returning False/0

All other values are truthy
"""

#NOTE 16]___ Loops____________
# for loop
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(f"Number: {num}")

# for loop with range
for i in range(5):  # 0 to 4
    print(f"Index: {i}")

for i in range(1, 6):  # 1 to 5
    print(f"Count: {i}")

for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(f"Even: {i}")

# while loop
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# break and continue
for i in range(10):
    if i == 3:
        continue  # Skip iteration when i is 3
    if i == 7:
        break  # Exit loop when i is 7
    print(f"i: {i}")

# else clause with loops
for i in range(3):
    print(f"Loop iteration: {i}")
else:
    print("Loop completed normally")

# Nested loops
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

#NOTE 17]___ Functions____________
# Defining functions
def greet():
    print("Hello, World!")

def greet_person(name):
    print(f"Hello, {name}!")

def add(a, b):
    return a + b

def power(base, exponent=2):  # Default parameter
    return base ** exponent

def calculate(*args):  # Variable number of arguments
    return sum(args)

def person_info(**kwargs):  # Keyword arguments
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling functions
greet()
greet_person("IRX358")
result = add(5, 3)
print(f"Addition result: {result}")

print(f"Power: {power(3)}")  # Using default exponent
print(f"Power: {power(3, 4)}")  # Specifying exponent

print(f"Sum: {calculate(1, 2, 3, 4, 5)}")

person_info(name="John", age=30, city="New York")

# Lambda functions (anonymous functions)
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# Higher-order functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(f"Squared: {squared}")
print(f"Even numbers: {even_numbers}")

#NOTE 18]___ List Comprehensions and Generator Expressions____________
# List comprehension
squares = [x ** 2 for x in range(10)]
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]

print(f"Squares: {squares}")
print(f"Even squares: {even_squares}")

# Nested list comprehension
matrix = [[i * j for j in range(3)] for i in range(3)]
print(f"Matrix: {matrix}")

# Generator expressions (memory efficient)
squares_gen = (x ** 2 for x in range(10))
print(f"First square: {next(squares_gen)}")

#NOTE 19]___ Error Handling____________
# Basic try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Multiple exceptions
try:
    num = int("abc")
except ValueError:
    print("Invalid number!")
except TypeError:
    print("Type error occurred!")

# Exception with else and finally
try:
    file = open("nonexistent.txt", "r")
except FileNotFoundError:
    print("File not found!")
else:
    print("File opened successfully!")
    file.close()
finally:
    print("This always executes!")

#NOTE 20]___ Basic File Operations____________
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a test file.\n")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(f"File content:\n{content}")

# Reading line by line
with open("example.txt", "r") as file:
    for line in file:
        print(f"Line: {line.strip()}")

# Appending to a file
with open("example.txt", "a") as file:
    file.write("This line is appended.\n")

#NOTE 21]___ Modules and Imports____________
# Import entire module
import math
print(f"Pi: {math.pi}")

# Import specific function
from random import randint
print(f"Random number: {randint(1, 10)}")

# Import with alias
import datetime as dt
print(f"Current time: {dt.datetime.now()}")

# Import all (not recommended for large modules)
from statistics import *
numbers = [1, 2, 3, 4, 5]
print(f"Mean: {mean(numbers)}")

#NOTE 22]___ String Formatting Advanced____________
name = "IRX358"
age = 25
height = 5.8

# f-string (Python 3.6+)
print(f"Name: {name}, Age: {age}, Height: {height:.2f}")

# format method
print("Name: {}, Age: {}, Height: {:.2f}".format(name, age, height))

# Using format specifiers
print(f"Binary: {age:b}")
print(f"Hexadecimal: {age:x}")
print(f"Scientific: {height:e}")
print(f"Percentage: {0.75:.2%}")

#NOTE 23]___ Enumerate and Zip____________
# Enumerate - get index and value
fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Zip - combine iterables
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

#NOTE 24]___ Type Hints (Optional but recommended)____________
def add_numbers(a: int, b: int) -> int:
    return a + b

def process_list(items: list[str]) -> list[str]:
    return [item.upper() for item in items]

# Using type hints
result = add_numbers(5, 3)
processed = process_list(["hello", "world"])

print(f"Addition result: {result}")
print(f"Processed list: {processed}")

# You're no longer a beginner! Let's move to intermediate topics.
