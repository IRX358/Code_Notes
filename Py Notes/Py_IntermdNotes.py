# Python Intermediate notes with code from here
# Building on basic concepts to cover intermediate Python programming
# To run your .py file use 'python filename.py' or 'python3 filename.py'

#NOTE 1] ___ Object-Oriented Programming (OOP) - Classes and Objects____________
# Classes are blueprints for creating objects

class Person:
    # Class attribute (shared by all instances)
    species = "Homo sapiens"
    
    # Constructor/Initializer method
    def __init__(self, name, age):
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age
    
    # Instance method
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."
    
    # Another instance method
    def celebrate_birthday(self):
        self.age += 1
        return f"Happy birthday {self.name}! You're now {self.age}."
    
    # Class method (decorator needed)
    @classmethod
    def get_species(cls):
        return cls.species
    
    # Static method (doesn't depend on instance or class)
    @staticmethod
    def is_adult(age):
        return age >= 18

# Creating objects (instances)
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(person1.introduce())
print(person2.celebrate_birthday())
print(f"Species: {Person.get_species()}")
print(f"Is 25 adult? {Person.is_adult(25)}")

#NOTE 2] ___ Inheritance____________
# Creating child classes that inherit from parent classes

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass  # To be overridden by subclasses
    
    def eat(self):
        return f"{self.name} is eating."

class Dog(Animal):
    def __init__(self, name, breed):
        # Call parent constructor
        super().__init__(name)
        self.breed = breed
    
    # Override parent method
    def speak(self):
        return f"{self.name} says Woof!"
    
    # New method specific to Dog
    def fetch(self):
        return f"{self.name} is fetching the ball."

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
    
    def speak(self):
        return f"{self.name} says Meow!"
    
    def purr(self):
        return f"{self.name} is purring."

# Using inheritance
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Orange")

print(dog.speak())
print(dog.eat())
print(dog.fetch())
print(cat.speak())
print(cat.eat())
print(cat.purr())

#NOTE 3] ___ Multiple Inheritance____________
# A class can inherit from multiple parent classes

class Flyable:
    def fly(self):
        return "Flying high!"

class Swimmable:
    def swim(self):
        return "Swimming gracefully!"

class Duck(Flyable, Swimmable):
    def __init__(self, name):
        self.name = name
    
    def quack(self):
        return f"{self.name} says Quack!"

duck = Duck("Donald")
print(duck.fly())
print(duck.swim())
print(duck.quack())

#NOTE 4] ___ Polymorphism and Duck Typing____________
# Different objects can respond to the same method call

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

# Polymorphic function
def print_shape_info(shape):
    print(f"Area: {shape.area():.2f}")
    print(f"Perimeter: {shape.perimeter():.2f}")

rectangle = Rectangle(5, 3)
circle = Circle(4)

print("Rectangle:")
print_shape_info(rectangle)
print("\nCircle:")
print_shape_info(circle)

#NOTE 5] ___ Encapsulation and Properties____________
# Using private attributes and property decorators

class BankAccount:
    def __init__(self, account_number, initial_balance):
        self._account_number = account_number  # Protected attribute (convention)
        self.__balance = initial_balance  # Private attribute (name mangling)
    
    # Getter method
    @property
    def balance(self):
        return self.__balance
    
    # Setter method
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = amount
    
    # Read-only property
    @property
    def account_number(self):
        return self._account_number
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount
        return f"Deposited ${amount}. New balance: ${self.__balance}"
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.__balance}"

account = BankAccount("123456789", 1000)
print(account.deposit(500))
print(account.withdraw(200))
print(f"Current balance: ${account.balance}")

#NOTE 6] ___ Special Methods (Magic Methods)____________
# Dunder methods that define behavior for built-in operations

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    # String representation (for users)
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    # Official representation (for developers)
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    # Equality comparison
    def __eq__(self, other):
        if isinstance(other, Book):
            return (self.title == other.title and 
                   self.author == other.author and 
                   self.pages == other.pages)
        return False
    
    # Less than comparison
    def __lt__(self, other):
        if isinstance(other, Book):
            return self.pages < other.pages
        return NotImplemented
    
    # Addition (concatenation)
    def __add__(self, other):
        if isinstance(other, Book):
            return f"{self.title} + {other.title}"
        return NotImplemented
    
    # Length
    def __len__(self):
        return self.pages
    
    # Making object callable
    def __call__(self):
        return f"Reading '{self.title}' by {self.author}"

book1 = Book("Python Crash Course", "Eric Matthes", 560)
book2 = Book("Automate the Boring Stuff", "Al Sweigart", 504)
book3 = Book("Python Crash Course", "Eric Matthes", 560)

print(str(book1))
print(repr(book1))
print(f"Book1 == Book2: {book1 == book2}")
print(f"Book1 == Book3: {book1 == book3}")
print(f"Book1 < Book2: {book1 < book2}")
print(f"Book1 + Book2: {book1 + book2}")
print(f"Length of book1: {len(book1)} pages")
print(book1())

#NOTE 7] ___ Advanced File Handling____________
# Working with different file modes and contexts

import os
import json
import csv

# File modes:
# 'r' - read (default)
# 'w' - write (overwrites existing file)
# 'a' - append
# 'r+' - read and write
# 'b' - binary mode
# 't' - text mode (default)

# Writing and reading JSON
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "swimming", "coding"]
}

# Write JSON to file
with open("data.json", "w") as json_file:
    json.dump(data, json_file, indent=2)

# Read JSON from file
with open("data.json", "r") as json_file:
    loaded_data = json.load(json_file)
    print(f"Loaded JSON: {loaded_data}")

# Working with CSV files
students = [
    ["Name", "Age", "Grade"],
    ["Alice", 20, "A"],
    ["Bob", 21, "B"],
    ["Charlie", 19, "A"]
]

# Write CSV
with open("students.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(students)

# Read CSV
with open("students.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)

# File and directory operations
print(f"Current directory: {os.getcwd()}")
print(f"Files in current directory: {os.listdir('.')}")

# Create directory
if not os.path.exists("test_dir"):
    os.makedirs("test_dir")
    print("Created directory: test_dir")

# Check if file exists
if os.path.exists("data.json"):
    print("data.json exists")

# Get file size
file_size = os.path.getsize("data.json")
print(f"Size of data.json: {file_size} bytes")

#NOTE 8] ___ Advanced Exception Handling____________
# Custom exceptions and advanced error handling

class InsufficientFundsError(Exception):
    """Custom exception for insufficient funds"""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds: balance ${balance}, attempted withdrawal ${amount}")

class InvalidAmountError(Exception):
    """Custom exception for invalid amounts"""
    pass

class AdvancedBankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def deposit(self, amount):
        try:
            if amount <= 0:
                raise InvalidAmountError("Deposit amount must be positive")
            self.balance += amount
            return f"Deposited ${amount}. Balance: ${self.balance}"
        except InvalidAmountError as e:
            return f"Error: {e}"
    
    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise InvalidAmountError("Withdrawal amount must be positive")
            if amount > self.balance:
                raise InsufficientFundsError(self.balance, amount)
            self.balance -= amount
            return f"Withdrew ${amount}. Balance: ${self.balance}"
        except (InvalidAmountError, InsufficientFundsError) as e:
            return f"Error: {e}"
        except Exception as e:
            return f"Unexpected error: {e}"

# Exception chaining
def risky_operation():
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        raise ValueError("Division failed") from e

# Testing advanced exception handling
account = AdvancedBankAccount(100)
print(account.deposit(-50))  # Should raise InvalidAmountError
print(account.withdraw(150))  # Should raise InsufficientFundsError
print(account.withdraw(50))  # Should succeed

#NOTE 9] ___ List Methods and Advanced Operations____________
# Deep dive into list operations and methods

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Sorting
sorted_asc = sorted(numbers)  # Returns new sorted list
sorted_desc = sorted(numbers, reverse=True)

numbers.sort()  # Sorts in place
numbers.sort(reverse=True)  # Sorts in place descending

# Custom sorting
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

# Sort by age
people.sort(key=lambda person: person["age"])
print(f"Sorted by age: {people}")

# Sort by name
people.sort(key=lambda person: person["name"])
print(f"Sorted by name: {people}")

# Advanced list operations
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# List concatenation
combined = list1 + list2

# List repetition
repeated = list1 * 3

# Checking for common elements
common_elements = list(set(list1) & set(list2))

# Removing duplicates while preserving order
def remove_duplicates(seq):
    seen = set()
    return [x for x in seq if not (x in seen or seen.add(x))]

with_duplicates = [1, 2, 2, 3, 4, 4, 5]
unique_preserved = remove_duplicates(with_duplicates)
print(f"Unique preserved order: {unique_preserved}")

#NOTE 10] ___ Dictionary Methods and Advanced Operations____________
# Advanced dictionary operations and methods

# Dictionary merging (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = dict1 | dict2  # Union operator

# Dictionary update with unpacking
dict3 = {**dict1, **dict2, "e": 5}

# Default dictionary
from collections import defaultdict

word_count = defaultdict(int)
text = "hello world hello python world"
for word in text.split():
    word_count[word] += 1

print(f"Word count: {dict(word_count)}")

# OrderedDict (preserves insertion order)
from collections import OrderedDict

ordered = OrderedDict()
ordered["first"] = 1
ordered["second"] = 2
ordered["third"] = 3

# Counter
from collections import Counter

numbers = [1, 2, 3, 1, 2, 1, 4, 5, 2, 1]
counter = Counter(numbers)
print(f"Most common: {counter.most_common(3)}")

#NOTE 11] ___ Set Operations and Advanced Uses____________
# Advanced set operations and applications

# Set comprehensions
squares = {x**2 for x in range(10)}
even_squares = {x**2 for x in range(10) if x % 2 == 0}

# Finding unique elements across multiple lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list3 = [7, 8, 9, 10]

unique_elements = set(list1) | set(list2) | set(list3)
common_elements = set(list1) & set(list2) & set(list3)

# Set operations for data analysis
def analyze_data(data_lists):
    all_elements = set()
    for data_list in data_lists:
        all_elements.update(data_list)
    
    common_in_all = set(data_lists[0])
    for data_list in data_lists[1:]:
        common_in_all &= set(data_list)
    
    return {
        "total_unique": len(all_elements),
        "common_in_all": len(common_in_all),
        "unique_elements": all_elements,
        "common_elements": common_in_all
    }

analysis = analyze_data([list1, list2, list3])
print(f"Data analysis: {analysis}")

#NOTE 12] ___ Advanced String Operations____________
# Regular expressions and advanced string processing

import re

text = "Contact us at email@example.com or phone 123-456-7890. Visit https://example.com"

# Regular expressions
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
phone_pattern = r'\b\d{3}-\d{3}-\d{4}\b'
url_pattern = r'https?://[^\s]+'

emails = re.findall(email_pattern, text)
phones = re.findall(phone_pattern, text)
urls = re.findall(url_pattern, text)

print(f"Emails found: {emails}")
print(f"Phones found: {phones}")
print(f"URLs found: {urls}")

# String methods for data cleaning
dirty_text = "  Hello,   World!   How   are   you?   "
cleaned = " ".join(dirty_text.split())  # Remove extra whitespace
print(f"Cleaned text: '{cleaned}'")

# Advanced string formatting
name = "Alice"
age = 30
height = 5.8

# Using format specifiers
formatted = f"Name: {name:<10} | Age: {age:>3} | Height: {height:>5.2f}"
print(formatted)

#NOTE 13] ___ Working with Dates and Times____________
# Advanced datetime operations

from datetime import datetime, timedelta, timezone
import calendar

# Timezone awareness
utc_now = datetime.now(timezone.utc)
local_now = datetime.now()

# Date arithmetic
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)
delta = end_date - start_date

print(f"Days between dates: {delta.days}")

# Working with business days (excluding weekends)
def business_days_between(start, end):
    business_days = 0
    current = start
    while current <= end:
        if current.weekday() < 5:  # Monday to Friday
            business_days += 1
        current += timedelta(days=1)
    return business_days

business_days = business_days_between(start_date, end_date)
print(f"Business days: {business_days}")

# Calendar operations
year = 2024
month = 2
month_calendar = calendar.monthcalendar(year, month)
print(f"Calendar for {calendar.month_name[month]} {year}:")
for week in month_calendar:
    print(week)

#NOTE 14] ___ Functional Programming Concepts____________
# Map, filter, reduce, and lambda functions

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Map - apply function to all elements
squared = list(map(lambda x: x**2, numbers))
doubled = list(map(lambda x: x * 2, numbers))

# Filter - select elements that meet condition
evens = list(filter(lambda x: x % 2 == 0, numbers))
greater_than_5 = list(filter(lambda x: x > 5, numbers))

# Reduce - apply function cumulatively
sum_all = reduce(lambda x, y: x + y, numbers)
product_all = reduce(lambda x, y: x * y, numbers, 1)  # 1 is initial value

# Combining operations
result = reduce(lambda x, y: x + y, 
                filter(lambda x: x > 5, 
                       map(lambda x: x**2, numbers)))

print(f"Original: {numbers}")
print(f"Squared: {squared}")
print(f"Evens: {evens}")
print(f"Sum: {sum_all}")
print(f"Product: {product_all}")
print(f"Complex result: {result}")

#NOTE 15] ___ List Comprehensions with Conditions____________
# Advanced list comprehensions

# Nested list comprehensions
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(f"Matrix: {matrix}")

# Flattening nested lists
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for sublist in nested for item in sublist]
print(f"Flattened: {flattened}")

# Conditional list comprehensions
numbers = range(1, 21)
squares_of_evens = [x**2 for x in numbers if x % 2 == 0]
squares_or_cubes = [x**2 if x % 2 == 0 else x**3 for x in numbers]

# Dictionary comprehensions
word_lengths = {word: len(word) for word in ["hello", "world", "python"]}
square_dict = {x: x**2 for x in range(1, 11)}

# Set comprehensions
unique_squares = {x**2 for x in [1, 2, 2, 3, 3, 4, 4, 5]}

print(f"Squares of evens: {squares_of_evens}")
print(f"Word lengths: {word_lengths}")
print(f"Square dictionary: {square_dict}")
print(f"Unique squares: {unique_squares}")

#NOTE 16] ___ Working with Iterators and Generators____________
# Creating custom iterators and generators

class Countdown:
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        current = self.start
        self.start -= 1
        return current

# Using the custom iterator
countdown = Countdown(5)
for number in countdown:
    print(f"Countdown: {number}")

# Generator functions
def fibonacci_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# Using generator
fib_sequence = list(fibonacci_generator(10))
print(f"Fibonacci sequence: {fib_sequence}")

# Generator expressions
squares_gen = (x**2 for x in range(10))
print(f"First 5 squares: {list(squares_gen)[:5]}")

#NOTE 17] ___ Context Managers____________
# Creating custom context managers

class DatabaseConnection:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connection = None
    
    def __enter__(self):
        print(f"Connecting to database: {self.connection_string}")
        self.connection = f"Connected to {self.connection_string}"
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing database connection")
        self.connection = None
        if exc_type:
            print(f"Error occurred: {exc_val}")
        return False  # Don't suppress exceptions

# Using context manager
with DatabaseConnection("postgresql://localhost/mydb") as conn:
    print(f"Using connection: {conn}")
    # Simulate an error
    # raise ValueError("Database error")

# Using contextlib for simpler context managers
from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    print(f"Opening file: {filename}")
    f = open(filename, mode)
    try:
        yield f
    finally:
        print(f"Closing file: {filename}")
        f.close()

# Using the context manager
with file_manager("test.txt", "w") as f:
    f.write("Hello from context manager!")

#NOTE 18] ___ Modules and Packages____________
# Creating and using custom modules

# This would typically be in a separate file called my_module.py
"""
# my_module.py
def greet(name):
    return f"Hello, {name}!"

PI = 3.14159

class Calculator:
    def add(self, a, b):
        return a + b
"""

# Importing and using modules (simulated here)
def greet(name):
    return f"Hello, {name}!"

PI = 3.14159

class Calculator:
    def add(self, a, b):
        return a + b

# Using the module content
print(greet("World"))
print(f"PI value: {PI}")

calc = Calculator()
print(f"2 + 3 = {calc.add(2, 3)}")

#NOTE 19] ___ Working with JSON and APIs____________
# JSON serialization and basic API interaction

import json
import urllib.request
import urllib.parse

# Working with complex JSON
complex_data = {
    "users": [
        {"id": 1, "name": "Alice", "skills": ["Python", "JavaScript", "SQL"]},
        {"id": 2, "name": "Bob", "skills": ["Java", "C++", "Python"]},
        {"id": 3, "name": "Charlie", "skills": ["React", "Node.js", "MongoDB"]}
    ],
    "metadata": {
        "total_users": 3,
        "last_updated": "2024-01-15"
    }
}

# Serialize to JSON string
json_string = json.dumps(complex_data, indent=2)
print(f"JSON string:\n{json_string}")

# Deserialize from JSON string
parsed_data = json.loads(json_string)

# Process the data
for user in parsed_data["users"]:
    print(f"{user['name']} has {len(user['skills'])} skills")

#NOTE 20] ___ Testing with unittest____________
# Basic unit testing

import unittest

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
    
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(5, 2), 2.5)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

# Running tests (would normally be done from command line)
# unittest.main()

#NOTE 21] ___ Decorators Introduction____________
# Basic decorator concepts

def timing_decorator(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

# Using decorators
@timing_decorator
@logging_decorator
def slow_function(n):
    import time
    time.sleep(0.1)  # Simulate slow operation
    return sum(range(n))

result = slow_function(1000)
print(f"Result: {result}")

#NOTE 22] ___ Advanced Data Structures____________
# Using collections module for specialized data structures

from collections import namedtuple, deque, Counter, defaultdict

# Named tuples
Point = namedtuple('Point', ['x', 'y', 'z'])
p1 = Point(1, 2, 3)
p2 = Point(4, 5, 6)

print(f"Point 1: {p1}")
print(f"Distance: {p2.x - p1.x}")

# Deque (double-ended queue)
dq = deque([1, 2, 3])
dq.append(4)  # Add to right
dq.appendleft(0)  # Add to left
dq.pop()  # Remove from right
dq.popleft()  # Remove from left

print(f"Deque operations: {dq}")

# Counter for frequency counting
text = "hello world hello python world programming"
words = text.split()
word_freq = Counter(words)
print(f"Word frequencies: {word_freq}")
print(f"Most common: {word_freq.most_common(2)}")

# Defaultdict for automatic default values
grades = defaultdict(list)
student_scores = [
    ("Alice", 85), ("Bob", 92), ("Alice", 90), ("Charlie", 78), ("Bob", 88)
]

for student, score in student_scores:
    grades[student].append(score)

print(f"Student grades: {dict(grades)}")

#NOTE 23] ___ Working with Binary Data____________
# Handling binary files and data

import struct
import pickle

# Working with binary data
numbers = [1, 2, 3, 4, 5]

# Pack numbers into binary format
binary_data = struct.pack('5i', *numbers)  # 5 integers

# Unpack binary data
unpacked = struct.unpack('5i', binary_data)

print(f"Original: {numbers}")
print(f"Unpacked: {list(unpacked)}")

# Pickle for object serialization
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Person({self.name}, {self.age})"

person = Person("Alice", 30)

# Serialize object
pickled_data = pickle.dumps(person)

# Deserialize object
unpickled_person = pickle.loads(pickled_data)

print(f"Original: {person}")
print(f"Unpickled: {unpickled_person}")

#NOTE 24] ___ Performance Considerations____________
# Measuring and improving performance

import time
import sys
from timeit import timeit

# Measuring execution time
def measure_time(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    return result, end - start

# Example functions to compare
def slow_method(n):
    result = []
    for i in range(n):
        result.append(i * 2)
    return result

def fast_method(n):
    return [i * 2 for i in range(n)]

# Compare performance
n = 1000000
_, slow_time = measure_time(slow_method, n)
_, fast_time = measure_time(fast_method, n)

print(f"Slow method: {slow_time:.4f} seconds")
print(f"Fast method: {fast_time:.4f} seconds")
print(f"Speedup: {slow_time / fast_time:.2f}x")

# Memory usage
large_list = list(range(1000000))
print(f"Size of large list: {sys.getsizeof(large_list)} bytes")

# Using timeit for precise measurements
time_taken = timeit(lambda: [i**2 for i in range(1000)], number=1000)
print(f"List comprehension time: {time_taken:.4f} seconds")

# Ready for advanced topics! Let's explore decorators, generators, metaprogramming, and more.
