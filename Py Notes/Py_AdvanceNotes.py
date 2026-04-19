# Python Advanced notes with code from here
# Advanced Python programming concepts and techniques
# To run your .py file use 'python filename.py' or 'python3 filename.py'

#NOTE 1] ___ Advanced Decorators____________
# Deep dive into decorators with parameters, class decorators, and more

import functools
import time
from typing import Callable, Any

# Decorator with parameters
def repeat(times: int):
    def decorator(func: Callable):
        @functools.wraps(func)  # Preserve original function metadata
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator

# Decorator that accepts arguments
def timer_with_threshold(threshold: float):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            duration = end - start
            if duration > threshold:
                print(f"WARNING: {func.__name__} took {duration:.4f}s (threshold: {threshold}s)")
            else:
                print(f"{func.__name__} completed in {duration:.4f}s")
            return result
        return wrapper
    return decorator

# Using parameterized decorators
@repeat(3)
def greet(name: str) -> str:
    return f"Hello, {name}!"

@timer_with_threshold(0.1)
def slow_function(n: int) -> int:
    time.sleep(0.2)  # Simulate slow operation
    return sum(range(n))

print(f"Repeated greetings: {greet('Alice')}")
result = slow_function(1000)
print(f"Result: {result}")

# Class decorator
def add_method(cls):
    def new_method(self):
        return f"New method added to {self.__class__.__name__}"
    cls.new_method = new_method
    return cls

@add_method
class MyClass:
    def __init__(self, value):
        self.value = value
    
    def original_method(self):
        return f"Original method: {self.value}"

obj = MyClass(42)
print(obj.original_method())
print(obj.new_method())

# Property decorator with getter, setter, and deleter
class Temperature:
    def __init__(self, celsius: float = 0):
        self._celsius = celsius
    
    @property
    def celsius(self) -> float:
        return self._celsius
    
    @celsius.setter
    def celsius(self, value: float):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible")
        self._celsius = value
    
    @property
    def fahrenheit(self) -> float:
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value: float):
        self._celsius = (value - 32) * 5/9

temp = Temperature(25)
print(f"Celsius: {temp.celsius}")
print(f"Fahrenheit: {temp.fahrenheit}")
temp.fahrenheit = 68
print(f"Celsius: {temp.celsius}")

#NOTE 2] ___ Advanced Generators and Coroutines____________
# Generator-based coroutines, send(), throw(), and close()

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Generator with send() method
def accumulator():
    total = 0
    while True:
        value = yield total
        if value is not None:
            total += value

# Coroutines with send() and throw()
def coroutine_example():
    print("Coroutine started")
    try:
        while True:
            x = yield
            print(f"Received: {x}")
    except GeneratorExit:
        print("Coroutine closing")
    except Exception as e:
        print(f"Exception in coroutine: {e}")
        raise

# Using generators
fib = fibonacci_generator()
print("First 10 Fibonacci numbers:")
for _ in range(10):
    print(next(fib), end=" ")
print()

# Using accumulator with send()
acc = accumulator()
next(acc)  # Prime the generator
print(f"Sent 10, got: {acc.send(10)}")
print(f"Sent 20, got: {acc.send(20)}")
print(f"Sent 30, got: {acc.send(30)}")

# Using coroutines
co = coroutine_example()
next(co)  # Prime the coroutine
co.send("Hello")
co.send("World")
co.throw(ValueError("Custom error"))
co.close()  # Close the coroutine

#NOTE 3] ___ Metaprogramming with Metaclasses____________
# Creating custom metaclasses and dynamic class creation

class SingletonMeta(type):
    """Metaclass that implements the Singleton pattern"""
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Logger(metaclass=SingletonMeta):
    def __init__(self):
        self.messages = []
    
    def log(self, message):
        self.messages.append(message)
        print(f"LOG: {message}")

# Testing singleton
logger1 = Logger()
logger2 = Logger()
print(f"Same instance: {logger1 is logger2}")
logger1.log("First message")
logger2.log("Second message")
print(f"Messages: {logger1.messages}")

# Metaclass for automatic method registration
class MethodRegistryMeta(type):
    def __new__(cls, name, bases, namespace):
        # Create the class
        new_class = super().__new__(cls, name, bases, namespace)
        
        # Register methods that start with 'cmd_'
        if not hasattr(new_class, '_command_registry'):
            new_class._command_registry = {}
        
        for attr_name, attr_value in namespace.items():
            if attr_name.startswith('cmd_') and callable(attr_value):
                command_name = attr_name[4:]  # Remove 'cmd_' prefix
                new_class._command_registry[command_name] = attr_value
        
        return new_class

class CommandProcessor(metaclass=MethodRegistryMeta):
    def cmd_hello(self, name):
        return f"Hello, {name}!"
    
    def cmd_goodbye(self, name):
        return f"Goodbye, {name}!"
    
    def execute_command(self, command, *args):
        if command in self._command_registry:
            return self._command_registry[command](self, *args)
        else:
            return f"Unknown command: {command}"

processor = CommandProcessor()
print(processor.execute_command("hello", "Alice"))
print(processor.execute_command("goodbye", "Bob"))
print(f"Available commands: {list(processor._command_registry.keys())}")

# Dynamic class creation
def create_class(class_name: str, base_classes: tuple, class_dict: dict):
    return type(class_name, base_classes, class_dict)

# Create a class dynamically
DynamicClass = create_class(
    "DynamicClass",
    (object,),
    {
        "__init__": lambda self, value: setattr(self, "value", value),
        "get_value": lambda self: self.value,
        "set_value": lambda self, value: setattr(self, "value", value)
    }
)

dynamic_obj = DynamicClass(42)
print(f"Dynamic class value: {dynamic_obj.get_value()}")

#NOTE 4] ___ Descriptors____________
# Creating custom descriptors for controlled attribute access

class ValidatedAttribute:
    """Descriptor that validates attribute values"""
    def __init__(self, name, validator):
        self.name = name
        self.validator = validator
        self.private_name = f"_{name}"
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.private_name)
    
    def __set__(self, obj, value):
        if not self.validator(value):
            raise ValueError(f"Invalid value for {self.name}: {value}")
        setattr(obj, self.private_name, value)

class LazyAttribute:
    """Descriptor that computes value lazily"""
    def __init__(self, function):
        self.function = function
        self.attribute_name = function.__name__
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        value = self.function(obj)
        setattr(obj, self.attribute_name, value)
        return value

# Using descriptors
class Person:
    # Validated attributes
    age = ValidatedAttribute("age", lambda x: isinstance(x, int) and x >= 0)
    email = ValidatedAttribute("email", lambda x: "@" in x and "." in x)
    
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    
    @LazyAttribute
    def expensive_computation(self):
        print("Computing expensive value...")
        time.sleep(0.1)  # Simulate expensive computation
        return sum(range(1000))

person = Person("Alice", 30, "alice@example.com")
print(f"Name: {person.name}, Age: {person.age}, Email: {person.email}")

# Access lazy attribute (computed only once)
print(f"Expensive result: {person.expensive_computation}")
print(f"Expensive result (cached): {person.expensive_computation}")

#NOTE 5] ___ Advanced Context Managers____________
# Custom context managers with exception handling and cleanup

import threading
from contextlib import contextmanager

class DatabaseConnection:
    """Context manager for database connections"""
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connection = None
        self.transaction_active = False
    
    def __enter__(self):
        print(f"Connecting to database: {self.connection_string}")
        self.connection = f"Connection to {self.connection_string}"
        self.transaction_active = True
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None and self.transaction_active:
            print("Committing transaction")
        elif exc_type is not None and self.transaction_active:
            print(f"Rolling back transaction due to {exc_type.__name__}")
        
        print("Closing database connection")
        self.connection = None
        self.transaction_active = False
        return False  # Don't suppress exceptions
    
    def execute(self, query):
        if not self.connection:
            raise RuntimeError("No active connection")
        print(f"Executing: {query}")
        return f"Result of {query}"

# Thread-safe counter using context manager
class ThreadSafeCounter:
    def __init__(self):
        self._value = 0
        self._lock = threading.Lock()
    
    @contextmanager
    def locked(self):
        self._lock.acquire()
        try:
            yield
        finally:
            self._lock.release()
    
    def increment(self):
        with self.locked():
            old_value = self._value
            self._value += 1
            return old_value, self._value
    
    @property
    def value(self):
        with self.locked():
            return self._value

# Using advanced context managers
try:
    with DatabaseConnection("postgresql://localhost/mydb") as db:
        db.execute("SELECT * FROM users")
        db.execute("INSERT INTO logs VALUES ('test')")
        # Uncomment to test rollback:
        # raise ValueError("Database error")
except Exception as e:
    print(f"Caught exception: {e}")

# Testing thread-safe counter
counter = ThreadSafeCounter()
def worker(counter, iterations):
    for _ in range(iterations):
        old, new = counter.increment()
        print(f"Thread {threading.current_thread().name}: {old} -> {new}")

threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(counter, 5), name=f"Worker-{i}")
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Final counter value: {counter.value}")

#NOTE 6] ___ Advanced Exception Handling and Custom Exceptions____________
# Creating exception hierarchies and advanced error handling

class ApplicationError(Exception):
    """Base exception for application"""
    def __init__(self, message, error_code=None):
        super().__init__(message)
        self.error_code = error_code
        self.timestamp = time.time()

class ValidationError(ApplicationError):
    """Raised when validation fails"""
    def __init__(self, field, value, message=None):
        self.field = field
        self.value = value
        if message is None:
            message = f"Validation failed for {field}: {value}"
        super().__init__(message, error_code="VALIDATION_ERROR")

class BusinessLogicError(ApplicationError):
    """Raised when business logic is violated"""
    def __init__(self, message, context=None):
        self.context = context or {}
        super().__init__(message, error_code="BUSINESS_LOGIC_ERROR")

# Exception handling with context
def process_user_data(data):
    try:
        # Validate required fields
        if not data.get("email"):
            raise ValidationError("email", data.get("email"), "Email is required")
        
        if "@" not in data.get("email", ""):
            raise ValidationError("email", data.get("email"), "Invalid email format")
        
        age = data.get("age")
        if age is not None and (not isinstance(age, int) or age < 0):
            raise ValidationError("age", age, "Age must be a positive integer")
        
        # Business logic validation
        if age and age < 18:
            raise BusinessLogicError("User must be at least 18 years old", {"age": age})
        
        return {"status": "success", "processed_data": data}
    
    except ValidationError as e:
        return {
            "status": "error",
            "error_type": "validation",
            "field": e.field,
            "value": e.value,
            "message": str(e),
            "error_code": e.error_code
        }
    except BusinessLogicError as e:
        return {
            "status": "error",
            "error_type": "business_logic",
            "message": str(e),
            "context": e.context,
            "error_code": e.error_code
        }
    except Exception as e:
        return {
            "status": "error",
            "error_type": "unexpected",
            "message": str(e),
            "error_code": "UNEXPECTED_ERROR"
        }

# Test exception handling
test_data = [
    {"name": "Alice", "email": "alice@example.com", "age": 25},
    {"name": "Bob", "email": "invalid-email", "age": 30},
    {"name": "Charlie", "email": "charlie@example.com", "age": 16},
    {"name": "David", "age": 20}  # Missing email
]

for data in test_data:
    result = process_user_data(data)
    print(f"Processing {data.get('name', 'Unknown')}: {result}")

#NOTE 7] ___ Advanced Function Techniques____________
# Closures, function factories, and higher-order functions

def create_multiplier(factor):
    """Function factory that creates multiplier functions"""
    def multiplier(number):
        return number * factor
    return multiplier

# Closure with captured variables
def create_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    def get_count():
        return count
    return increment, get_count

# Higher-order function composition
def compose(*functions):
    """Compose multiple functions: compose(f, g, h)(x) == f(g(h(x)))"""
    def composed(x):
        for func in reversed(functions):
            x = func(x)
        return x
    return composed

# Memoization decorator
def memoize(func):
    """Cache function results"""
    cache = {}
    
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    
    wrapper.cache_clear = lambda: cache.clear()
    wrapper.cache_info = lambda: {'size': len(cache), 'cache': cache}
    return wrapper

# Using function techniques
double = create_multiplier(2)
triple = create_multiplier(3)

print(f"Double 10: {double(10)}")
print(f"Triple 10: {triple(10)}")

inc, get_count = create_counter()
print(f"Counter: {inc()}, {inc()}, {inc()}")
print(f"Current count: {get_count()}")

# Function composition
add_one = lambda x: x + 1
square = lambda x: x ** 2
half = lambda x: x / 2

composed = compose(half, square, add_one)
print(f"Compose result: {composed(3)}")  # half(square(add_one(3))) = half(square(4)) = half(16) = 8

# Memoization example
@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"Fibonacci(10): {fibonacci(10)}")
print(f"Fibonacci cache info: {fibonacci.cache_info()}")

#NOTE 8] ___ Advanced Data Structures and Algorithms____________
# Custom data structures and algorithm implementations

class Stack:
    """LIFO Stack implementation"""
    def __init__(self):
        self._items = []
    
    def push(self, item):
        self._items.append(item)
    
    def pop(self):
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()
    
    def peek(self):
        if not self._items:
            raise IndexError("peek from empty stack")
        return self._items[-1]
    
    def is_empty(self):
        return len(self._items) == 0
    
    def __len__(self):
        return len(self._items)

class Queue:
    """FIFO Queue implementation using collections.deque"""
    from collections import deque
    
    def __init__(self):
        self._items = deque()
    
    def enqueue(self, item):
        self._items.append(item)
    
    def dequeue(self):
        if not self._items:
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()
    
    def peek(self):
        if not self._items:
            raise IndexError("peek from empty queue")
        return self._items[0]
    
    def is_empty(self):
        return len(self._items) == 0
    
    def __len__(self):
        return len(self._items)

class BinarySearchTree:
    """Binary Search Tree implementation"""
    class Node:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value
            self.left = None
            self.right = None
    
    def __init__(self):
        self.root = None
    
    def insert(self, key, value=None):
        self.root = self._insert_recursive(self.root, key, value)
    
    def _insert_recursive(self, node, key, value):
        if node is None:
            return self.Node(key, value)
        
        if key < node.key:
            node.left = self._insert_recursive(node.left, key, value)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key, value)
        
        return node
    
    def search(self, key):
        return self._search_recursive(self.root, key)
    
    def _search_recursive(self, node, key):
        if node is None:
            return None
        
        if key == node.key:
            return node.value
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)
    
    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append((node.key, node.value))
            self._inorder_recursive(node.right, result)

# Using custom data structures
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(f"Stack pop: {stack.pop()}, {stack.pop()}, {stack.pop()}")

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(f"Queue dequeue: {queue.dequeue()}, {queue.dequeue()}, {queue.dequeue()}")

bst = BinarySearchTree()
bst.insert(5, "five")
bst.insert(3, "three")
bst.insert(7, "seven")
bst.insert(2, "two")
bst.insert(4, "four")

print(f"BST search 3: {bst.search(3)}")
print(f"BST inorder: {bst.inorder_traversal()}")

#NOTE 9] ___ Advanced Iterators and Itertools____________
# Using itertools for efficient iteration

import itertools
import random

# Infinite iterators
def fibonacci_infinite():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Using itertools
# Count from 1 to 10
print("Count:", list(itertools.islice(itertools.count(1), 10)))

# Cycle through a sequence
print("Cycle:", list(itertools.islice(itertools.cycle(['A', 'B', 'C']), 7)))

# Repeat elements
print("Repeat:", list(itertools.repeat('X', 5)))

# Combinations and permutations
items = ['A', 'B', 'C']
print("Combinations:", list(itertools.combinations(items, 2)))
print("Permutations:", list(itertools.permutations(items, 2)))
print("Product:", list(itertools.product(items, repeat=2)))

# Advanced filtering
numbers = range(1, 21)
print("Filter false:", list(itertools.filterfalse(lambda x: x % 2 == 0, numbers)))
print("Dropwhile:", list(itertools.dropwhile(lambda x: x < 10, numbers)))
print("Takewhile:", list(itertools.takewhile(lambda x: x < 10, numbers)))

# Groupby
data = [
    {'name': 'Alice', 'department': 'Engineering'},
    {'name': 'Bob', 'department': 'Engineering'},
    {'name': 'Charlie', 'department': 'Marketing'},
    {'name': 'David', 'department': 'Marketing'},
    {'name': 'Eve', 'department': 'Engineering'}
]

# Sort by department first (required for groupby)
data.sort(key=lambda x: x['department'])

for department, group in itertools.groupby(data, key=lambda x: x['department']):
    print(f"{department}: {[person['name'] for person in group]}")

# Custom iterator that yields prime numbers
class PrimeIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 2
        self.primes = []
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.current <= self.limit:
            if self._is_prime(self.current):
                prime = self.current
                self.current += 1
                return prime
            self.current += 1
        raise StopIteration
    
    def _is_prime(self, n):
        if n < 2:
            return False
        for p in self.primes:
            if p * p > n:
                break
            if n % p == 0:
                return False
        self.primes.append(n)
        return True

print("Primes up to 20:", list(PrimeIterator(20)))

#NOTE 10] ___ Advanced String Processing and Regular Expressions____________
import re
from typing import List, Dict, Pattern

class TextProcessor:
    """Advanced text processing utilities"""
    
    def __init__(self):
        # Compile commonly used regex patterns
        self.email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        self.phone_pattern = re.compile(r'\b\d{3}-\d{3}-\d{4}\b')
        self.url_pattern = re.compile(r'https?://[^\s<>"{}|\\^`\[\]]+')
        self.word_pattern = re.compile(r'\b\w+\b')
    
    def extract_emails(self, text: str) -> List[str]:
        return self.email_pattern.findall(text)
    
    def extract_phones(self, text: str) -> List[str]:
        return self.phone_pattern.findall(text)
    
    def extract_urls(self, text: str) -> List[str]:
        return self.url_pattern.findall(text)
    
    def word_frequency(self, text: str) -> Dict[str, int]:
        words = self.word_pattern.findall(text.lower())
        return dict(Counter(words))
    
    def clean_text(self, text: str) -> str:
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        # Remove special characters (keep letters, numbers, spaces)
        text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        return text.strip()
    
    def tokenize_sentences(self, text: str) -> List[str]:
        # Split on sentence endings
        sentences = re.split(r'[.!?]+', text)
        return [s.strip() for s in sentences if s.strip()]

# Using advanced text processing
processor = TextProcessor()

sample_text = """
Contact us at support@example.com or sales@company.org.
Call us at 555-123-4567 or 555-987-6543.
Visit our website at https://example.com or http://company.org.
For more information, email admin@website.net.
"""

print("Emails found:", processor.extract_emails(sample_text))
print("Phones found:", processor.extract_phones(sample_text))
print("URLs found:", processor.extract_urls(sample_text))

long_text = "This is a sample text. This text contains repeated words. Sample text is useful for testing."
print("Word frequency:", processor.word_frequency(long_text))
print("Cleaned text:", processor.clean_text("  Hello,   World!   How   are   you?   "))
print("Sentences:", processor.tokenize_sentences("Hello world! How are you? I'm fine. Thanks for asking."))

#NOTE 11] ___ Advanced File I/O and Serialization____________
import json
import pickle
import csv
import sqlite3
from pathlib import Path
import gzip
import bz2

class FileManager:
    """Advanced file management utilities"""
    
    @staticmethod
    def save_json(data, filename: str, compress: bool = False):
        """Save data to JSON file with optional compression"""
        if compress:
            with gzip.open(f"{filename}.gz", 'wt', encoding='utf-8') as f:
                json.dump(data, f, indent=2)
        else:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)
    
    @staticmethod
    def load_json(filename: str, compressed: bool = False):
        """Load data from JSON file with optional decompression"""
        if compressed:
            with gzip.open(f"{filename}.gz", 'rt', encoding='utf-8') as f:
                return json.load(f)
        else:
            with open(filename, 'r', encoding='utf-8') as f:
                return json.load(f)
    
    @staticmethod
    def save_pickle(data, filename: str, compress: bool = False):
        """Save data using pickle with optional compression"""
        if compress:
            with bz2.open(f"{filename}.bz2", 'wb') as f:
                pickle.dump(data, f)
        else:
            with open(filename, 'wb') as f:
                pickle.dump(data, f)
    
    @staticmethod
    def load_pickle(filename: str, compressed: bool = False):
        """Load data from pickle file with optional decompression"""
        if compressed:
            with bz2.open(f"{filename}.bz2", 'rb') as f:
                return pickle.load(f)
        else:
            with open(filename, 'rb') as f:
                return pickle.load(f)
    
    @staticmethod
    def csv_to_dict(filename: str) -> List[Dict]:
        """Convert CSV to list of dictionaries"""
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return list(reader)
    
    @staticmethod
    def dict_to_csv(data: List[Dict], filename: str):
        """Convert list of dictionaries to CSV"""
        if not data:
            return
        
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

# Database operations
class DatabaseManager:
    """Simple SQLite database manager"""
    
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.connection = None
    
    def __enter__(self):
        self.connection = sqlite3.connect(self.db_path)
        self.connection.row_factory = sqlite3.Row  # Access columns by name
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()
    
    def execute_query(self, query: str, params: tuple = None):
        """Execute a query and return results"""
        cursor = self.connection.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        return cursor.fetchall()
    
    def execute_update(self, query: str, params: tuple = None):
        """Execute an update query"""
        cursor = self.connection.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        self.connection.commit()
        return cursor.rowcount

# Using advanced file operations
test_data = {
    "users": [
        {"id": 1, "name": "Alice", "email": "alice@example.com"},
        {"id": 2, "name": "Bob", "email": "bob@example.com"},
        {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
    ],
    "metadata": {"created": "2024-01-15", "version": "1.0"}
}

# Test JSON operations
FileManager.save_json(test_data, "test_data.json")
FileManager.save_json(test_data, "test_data.json", compress=True)

loaded_data = FileManager.load_json("test_data.json")
print("Loaded JSON:", loaded_data)

# Test database operations
with DatabaseManager("test.db") as db:
    # Create table
    db.execute_update("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE
        )
    """)
    
    # Insert data
    for user in test_data["users"]:
        db.execute_update(
            "INSERT OR REPLACE INTO users (id, name, email) VALUES (?, ?, ?)",
            (user["id"], user["name"], user["email"])
        )
    
    # Query data
    users = db.execute_query("SELECT * FROM users")
    print("Database users:", [dict(user) for user in users])

#NOTE 12] ___ Advanced Concurrency and Parallelism____________
import threading
import multiprocessing
import asyncio
import concurrent.futures
from queue import Queue
import time

class ThreadSafeCounter:
    """Thread-safe counter with lock"""
    def __init__(self):
        self._value = 0
        self._lock = threading.Lock()
    
    def increment(self):
        with self._lock:
            self._value += 1
    
    def get_value(self):
        with self._lock:
            return self._value

# Producer-Consumer pattern
class ProducerConsumer:
    def __init__(self, buffer_size: int = 10):
        self.buffer = Queue(maxsize=buffer_size)
        self.producer_done = False
    
    def producer(self, items: list):
        """Producer thread"""
        for item in items:
            self.buffer.put(item)
            print(f"Produced: {item}")
            time.sleep(0.1)
        self.producer_done = True
    
    def consumer(self):
        """Consumer thread"""
        while not self.producer_done or not self.buffer.empty():
            try:
                item = self.buffer.get(timeout=0.1)
                print(f"Consumed: {item}")
                time.sleep(0.15)
                self.buffer.task_done()
            except:
                continue

# Async/await example
async def async_fetch_data(url: str, delay: float):
    """Simulate async data fetching"""
    print(f"Fetching {url}...")
    await asyncio.sleep(delay)
    return f"Data from {url}"

async def async_process_urls(urls: list):
    """Process multiple URLs concurrently"""
    tasks = [async_fetch_data(url, delay) for url, delay in urls]
    results = await asyncio.gather(*tasks)
    return results

# Process pool for CPU-bound tasks
def cpu_intensive_task(n: int) -> int:
    """CPU-intensive calculation"""
    result = sum(i ** 2 for i in range(n))
    return result

# Using concurrency patterns
# Thread-based producer-consumer
pc = ProducerConsumer()
items = list(range(10))

producer_thread = threading.Thread(target=pc.producer, args=(items,))
consumer_thread = threading.Thread(target=pc.consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()

# Async/await example
async def main_async():
    urls = [
        ("https://api1.com", 0.5),
        ("https://api2.com", 0.3),
        ("https://api3.com", 0.7)
    ]
    results = await async_process_urls(urls)
    print("Async results:", results)

# Run async code
asyncio.run(main_async())

# Process pool for CPU-bound tasks
with concurrent.futures.ProcessPoolExecutor() as executor:
    numbers = [1000, 2000, 3000]
    results = list(executor.map(cpu_intensive_task, numbers))
    print("Process pool results:", results)

#NOTE 13] ___ Advanced Testing Techniques____________
import unittest
from unittest.mock import Mock, patch, MagicMock
import pytest
from typing import Any

class TestAdvancedFeatures(unittest.TestCase):
    """Advanced testing examples"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.test_data = {"a": 1, "b": 2, "c": 3}
    
    def tearDown(self):
        """Clean up after tests"""
        pass
    
    def test_with_mock(self):
        """Test using mock objects"""
        mock_service = Mock()
        mock_service.get_data.return_value = {"status": "success"}
        
        result = mock_service.get_data()
        self.assertEqual(result["status"], "success")
        mock_service.get_data.assert_called_once()
    
    @patch('time.time')
    def test_with_patch(self, mock_time):
        """Test using patch decorator"""
        mock_time.return_value = 1234567890
        from datetime import datetime
        dt = datetime.fromtimestamp(mock_time.return_value)
        self.assertEqual(dt.year, 2009)
    
    def test_exceptions(self):
        """Test exception handling"""
        with self.assertRaises(ValueError):
            int("invalid")
    
    def test_custom_assertions(self):
        """Custom assertion methods"""
        def assert_valid_email(email):
            pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            self.assertRegex(email, pattern, f"Invalid email: {email}")
        
        assert_valid_email("test@example.com")
        with self.assertRaises(AssertionError):
            assert_valid_email("invalid-email")

# Property-based testing concept (simplified)
def property_based_test():
    """Example of property-based testing"""
    import random
    
    def commutative_property(a, b):
        """Test that addition is commutative"""
        return a + b == b + a
    
    def associative_property(a, b, c):
        """Test that addition is associative"""
        return (a + b) + c == a + (b + c)
    
    # Generate random test cases
    for _ in range(100):
        a, b, c = random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100)
        assert commutative_property(a, b), f"Commutative property failed for {a}, {b}"
        assert associative_property(a, b, c), f"Associative property failed for {a}, {b}, {c}"

# Run property-based test
property_based_test()
print("Property-based tests passed!")

#NOTE 14] ___ Advanced Type Hints and Generic Programming____________
from typing import TypeVar, Generic, List, Dict, Optional, Union, Callable, Any
from abc import ABC, abstractmethod

# Generic programming
T = TypeVar('T')
K = TypeVar('K')
V = TypeVar('V')

class Stack(Generic[T]):
    """Generic stack implementation"""
    def __init__(self) -> None:
        self._items: List[T] = []
    
    def push(self, item: T) -> None:
        self._items.append(item)
    
    def pop(self) -> T:
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()
    
    def is_empty(self) -> bool:
        return len(self._items) == 0

class Repository(Generic[K, V]):
    """Generic repository pattern"""
    def __init__(self) -> None:
        self._data: Dict[K, V] = {}
    
    def save(self, key: K, value: V) -> None:
        self._data[key] = value
    
    def get(self, key: K) -> Optional[V]:
        return self._data.get(key)
    
    def delete(self, key: K) -> bool:
        return self._data.pop(key, None) is not None
    
    def find_all(self) -> List[V]:
        return list(self._data.values())

# Abstract base classes
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        pass

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height
    
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
    
    def area(self) -> float:
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self) -> float:
        import math
        return 2 * math.pi * self.radius

# Function with complex type hints
def process_shapes(shapes: List[Shape]) -> Dict[str, float]:
    """Process a list of shapes and return statistics"""
    total_area = sum(shape.area() for shape in shapes)
    total_perimeter = sum(shape.perimeter() for shape in shapes)
    avg_area = total_area / len(shapes) if shapes else 0
    avg_perimeter = total_perimeter / len(shapes) if shapes else 0
    
    return {
        "total_area": total_area,
        "total_perimeter": total_perimeter,
        "average_area": avg_area,
        "average_perimeter": avg_perimeter
    }

# Using generic types and abstract classes
int_stack = Stack[int]()
int_stack.push(1)
int_stack.push(2)
print(f"Stack pop: {int_stack.pop()}")

user_repo = Repository[int, str]()
user_repo.save(1, "Alice")
user_repo.save(2, "Bob")
print(f"User 1: {user_repo.get(1)}")

shapes = [Rectangle(5, 3), Circle(2), Rectangle(10, 4)]
stats = process_shapes(shapes)
print(f"Shape statistics: {stats}")

#NOTE 15] ___ Performance Optimization and Profiling____________
import cProfile
import pstats
from functools import lru_cache
import timeit
import memory_profiler

# Performance decorators
def performance_monitor(func):
    """Monitor function performance"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        start_memory = memory_profiler.memory_usage()[0]
        
        result = func(*args, **kwargs)
        
        end_time = time.time()
        end_memory = memory_profiler.memory_usage()[0]
        
        print(f"{func.__name__}:")
        print(f"  Time: {end_time - start_time:.4f}s")
        print(f"  Memory: {end_memory - start_memory:.2f}MB")
        print(f"  Result: {result}")
        
        return result
    return wrapper

# Memoization with LRU cache
@lru_cache(maxsize=128)
def expensive_function(n: int) -> int:
    """Expensive computation with caching"""
    if n <= 1:
        return n
    return expensive_function(n - 1) + expensive_function(n - 2)

# Performance comparison
def slow_fibonacci(n: int) -> int:
    """Slow recursive fibonacci"""
    if n <= 1:
        return n
    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)

@performance_monitor
def test_slow_fibonacci(n: int) -> int:
    return slow_fibonacci(n)

@performance_monitor
def test_fast_fibonacci(n: int) -> int:
    return expensive_function(n)

# Test performance
print("Performance comparison:")
test_slow_fibonacci(30)
test_fast_fibonacci(30)

# Profiling with cProfile
def profile_function():
    """Profile a function"""
    def complex_operation():
        result = []
        for i in range(1000):
            result.append(i ** 2)
        return sum(result)
    
    # Profile the function
    profiler = cProfile.Profile()
    profiler.enable()
    
    for _ in range(100):
        complex_operation()
    
    profiler.disable()
    
    # Print stats
    stats = pstats.Stats(profiler)
    stats.sort_stats('cumulative')
    stats.print_stats(10)  # Top 10 functions

profile_function()

#NOTE 16] ___ Advanced Python Features____________
# Dataclasses, enums, and other modern Python features

from dataclasses import dataclass, field
from enum import Enum, auto, IntEnum, Flag
from typing import ClassVar
import weakref

# Dataclasses
@dataclass
class Person:
    name: str
    age: int
    email: str = field(default="")
    id_counter: ClassVar[int] = 0
    id: int = field(init=False)
    
    def __post_init__(self):
        Person.id_counter += 1
        self.id = Person.id_counter
    
    def is_adult(self) -> bool:
        return self.age >= 18

@dataclass
class Employee(Person):
    employee_id: str
    department: str
    salary: float = field(repr=False)  # Don't show in repr
    
    def annual_bonus(self) -> float:
        return self.salary * 0.1

# Enums
class Status(Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"

class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

class Permission(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()
    ADMIN = READ | WRITE | EXECUTE

# Weak references for memory management
class ResourceManager:
    def __init__(self):
        self.resources = weakref.WeakSet()
    
    def add_resource(self, resource):
        self.resources.add(resource)
    
    def cleanup(self):
        print(f"Cleaning up {len(self.resources)} resources")

class Resource:
    def __del__(self):
        print(f"Resource {id(self)} cleaned up")

# Using advanced features
person = Person("Alice", 30, "alice@example.com")
employee = Employee("Bob", 25, "bob@example.com", "EMP001", "Engineering", 75000)

print(f"Person: {person}")
print(f"Employee: {employee}")
print(f"Is adult: {person.is_adult()}")
print(f"Annual bonus: ${employee.annual_bonus():.2f}")

# Using enums
status = Status.APPROVED
priority = Priority.HIGH
permissions = Permission.READ | Permission.WRITE

print(f"Status: {status.value}")
print(f"Priority: {priority.name} ({priority})")
print(f"Permissions: {permissions}")

# Weak references
manager = ResourceManager()
r1 = Resource()
r2 = Resource()

manager.add_resource(r1)
manager.add_resource(r2)

del r1  # Should be automatically cleaned up
manager.cleanup()

#NOTE 17] ___ Advanced Networking and Web Programming____________
import socket
import http.server
import socketserver
import urllib.request
import urllib.parse
import json
from threading import Thread

# Simple HTTP server
class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"message": "Hello from Python server!", "timestamp": time.time()}
            self.wfile.write(json.dumps(data).encode())
        else:
            super().do_GET()
    
    def do_POST(self):
        if self.path == '/api/echo':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            try:
                data = json.loads(post_data.decode())
                response = {"echo": data, "received": True}
            except:
                response = {"error": "Invalid JSON", "received": False}
            
            self.wfile.write(json.dumps(response).encode())

# HTTP client
class HTTPClient:
    @staticmethod
    def get(url: str) -> dict:
        """Make GET request"""
        with urllib.request.urlopen(url) as response:
            return json.loads(response.read().decode())
    
    @staticmethod
    def post(url: str, data: dict) -> dict:
        """Make POST request"""
        encoded_data = urllib.parse.urlencode(data).encode()
        req = urllib.request.Request(url, data=encoded_data, method='POST')
        req.add_header('Content-Type', 'application/x-www-form-urlencoded')
        
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode())

# Socket programming example
class SimpleEchoServer:
    def __init__(self, host: str = 'localhost', port: int = 9999):
        self.host = host
        self.port = port
        self.server_socket = None
    
    def start(self):
        """Start the echo server"""
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        
        print(f"Echo server listening on {self.host}:{self.port}")
        
        try:
            while True:
                client_socket, address = self.server_socket.accept()
                print(f"Connection from {address}")
                
                # Handle client in a separate thread
                client_thread = Thread(target=self.handle_client, args=(client_socket,))
                client_thread.start()
        except KeyboardInterrupt:
            print("Server shutting down...")
        finally:
            if self.server_socket:
                self.server_socket.close()
    
    def handle_client(self, client_socket: socket.socket):
        """Handle individual client connection"""
        try:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                
                message = data.decode()
                print(f"Received: {message}")
                
                # Echo back the message
                response = f"Echo: {message}"
                client_socket.send(response.encode())
        except Exception as e:
            print(f"Error handling client: {e}")
        finally:
            client_socket.close()

#NOTE 18] ___ Advanced Debugging and Logging____________
import logging
import sys
import traceback
from typing import Optional

# Advanced logging configuration
def setup_logging():
    """Set up advanced logging configuration"""
    # Create formatters
    detailed_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
    )
    
    simple_formatter = logging.Formatter(
        '%(levelname)s - %(message)s'
    )
    
    # Create handlers
    file_handler = logging.FileHandler('app.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(detailed_formatter)
    
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(simple_formatter)
    
    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)
    
    # Create specific loggers
    database_logger = logging.getLogger('database')
    api_logger = logging.getLogger('api')
    
    return database_logger, api_logger

# Custom exception with debugging info
class DebuggableException(Exception):
    def __init__(self, message: str, context: dict = None):
        super().__init__(message)
        self.context = context or {}
        self.traceback = traceback.format_exc()
    
    def __str__(self):
        base_msg = super().__str__()
        if self.context:
            context_str = ", ".join(f"{k}={v}" for k, v in self.context.items())
            return f"{base_msg} (Context: {context_str})"
        return base_msg

# Debug decorator
def debug_function(func):
    """Decorator to add debugging information to functions"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(func.__module__)
        logger.debug(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        
        try:
            result = func(*args, **kwargs)
            logger.debug(f"{func.__name__} returned {result}")
            return result
        except Exception as e:
            logger.error(f"Exception in {func.__name__}: {e}")
            logger.debug(f"Traceback: {traceback.format_exc()}")
            raise
    
    return wrapper

# Performance profiler
class PerformanceProfiler:
    def __init__(self):
        self.timings = {}
    
    def profile(self, name: str):
        """Context manager for profiling"""
        return ProfileContext(self, name)
    
    def add_timing(self, name: str, duration: float):
        if name not in self.timings:
            self.timings[name] = []
        self.timings[name].append(duration)
    
    def get_stats(self) -> dict:
        stats = {}
        for name, times in self.timings.items():
            stats[name] = {
                'count': len(times),
                'total': sum(times),
                'average': sum(times) / len(times),
                'min': min(times),
                'max': max(times)
            }
        return stats

class ProfileContext:
    def __init__(self, profiler: PerformanceProfiler, name: str):
        self.profiler = profiler
        self.name = name
        self.start_time = None
    
    def __enter__(self):
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        duration = time.time() - self.start_time
        self.profiler.add_timing(self.name, duration)

# Using advanced debugging and logging
setup_logging()
database_logger, api_logger = setup_logging()

@debug_function
def divide_numbers(a: float, b: float) -> float:
    """Divide two numbers with debugging"""
    if b == 0:
        raise DebuggableException(
            "Division by zero",
            context={"a": a, "b": b, "operation": "division"}
        )
    return a / b

# Using performance profiler
profiler = PerformanceProfiler()

try:
    with profiler.profile("division"):
        result = divide_numbers(10, 2)
        print(f"Result: {result}")
    
    with profiler.profile("error_case"):
        result = divide_numbers(10, 0)
        print(f"Result: {result}")
except DebuggableException as e:
    print(f"Caught debuggable exception: {e}")
    print(f"Context: {e.context}")

print("Performance stats:", profiler.get_stats())

#NOTE 19] ___ Advanced Security and Cryptography____________
import hashlib
import hmac
import secrets
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os

class SecurityUtils:
    """Security utilities for encryption, hashing, and secure random generation"""
    
    @staticmethod
    def generate_secure_token(length: int = 32) -> str:
        """Generate cryptographically secure random token"""
        return secrets.token_urlsafe(length)
    
    @staticmethod
    def hash_password(password: str, salt: bytes = None) -> tuple:
        """Hash password using PBKDF2"""
        if salt is None:
            salt = os.urandom(32)
        
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = kdf.derive(password.encode())
        return key, salt
    
    @staticmethod
    def verify_password(password: str, hashed: bytes, salt: bytes) -> bool:
        """Verify password against hash"""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        try:
            kdf.verify(password.encode(), hashed)
            return True
        except:
            return False
    
    @staticmethod
    def generate_encryption_key() -> bytes:
        """Generate encryption key"""
        return Fernet.generate_key()
    
    @staticmethod
    def encrypt_data(data: str, key: bytes) -> bytes:
        """Encrypt data using Fernet symmetric encryption"""
        f = Fernet(key)
        return f.encrypt(data.encode())
    
    @staticmethod
    def decrypt_data(encrypted_data: bytes, key: bytes) -> str:
        """Decrypt data using Fernet symmetric encryption"""
        f = Fernet(key)
        return f.decrypt(encrypted_data).decode()
    
    @staticmethod
    def create_hmac_signature(data: str, secret_key: str) -> str:
        """Create HMAC signature for data"""
        signature = hmac.new(
            secret_key.encode(),
            data.encode(),
            hashlib.sha256
        ).hexdigest()
        return signature
    
    @staticmethod
    def verify_hmac_signature(data: str, signature: str, secret_key: str) -> bool:
        """Verify HMAC signature"""
        expected_signature = SecurityUtils.create_hmac_signature(data, secret_key)
        return hmac.compare_digest(signature, expected_signature)

# Using security utilities
security = SecurityUtils()

# Generate secure token
token = security.generate_secure_token()
print(f"Secure token: {token}")

# Password hashing
password = "my_secure_password"
hashed_password, salt = security.hash_password(password)
print(f"Password hashed successfully")

# Verify password
is_valid = security.verify_password("my_secure_password", hashed_password, salt)
print(f"Password verification: {is_valid}")

# Encryption/Decryption
encryption_key = security.generate_encryption_key()
secret_message = "This is a secret message"
encrypted = security.encrypt_data(secret_message, encryption_key)
decrypted = security.decrypt_data(encrypted, encryption_key)

print(f"Original: {secret_message}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")

# HMAC signature
data_to_sign = "Important data"
secret_key = "my_secret_key"
signature = security.create_hmac_signature(data_to_sign, secret_key)
is_signature_valid = security.verify_hmac_signature(data_to_sign, signature, secret_key)

print(f"Data: {data_to_sign}")
print(f"Signature: {signature}")
print(f"Signature valid: {is_signature_valid}")

#NOTE 20] ___ Advanced Python Best Practices and Patterns____________
from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable

# Protocol for duck typing
@runtime_checkable
class Drawable(Protocol):
    def draw(self) -> str: ...
    def area(self) -> float: ...

class Circle:
    def __init__(self, radius: float):
        self.radius = radius
    
    def draw(self) -> str:
        return f"Drawing circle with radius {self.radius}"
    
    def area(self) -> float:
        import math
        return math.pi * self.radius ** 2

class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    def draw(self) -> str:
        return f"Drawing rectangle {width}x{height}"
    
    def area(self) -> float:
        return self.width * self.height

def render_shape(shape: Drawable) -> None:
    """Render any drawable shape"""
    print(shape.draw())
    print(f"Area: {shape.area():.2f}")

# Singleton pattern with metaclass
class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class DatabaseConnection(metaclass=SingletonMeta):
    def __init__(self):
        self.connection_id = id(self)
    
    def connect(self):
        print(f"Connecting to database (ID: {self.connection_id})")

# Observer pattern
class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        pass

class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer: Observer):
        self._observers.append(observer)
    
    def detach(self, observer: Observer):
        self._observers.remove(observer)
    
    def notify(self, message: str):
        for observer in self._observers:
            observer.update(message)

class EmailNotifier(Observer):
    def update(self, message: str):
        print(f"Email notification: {message}")

class SMSNotifier(Observer):
    def update(self, message: str):
        print(f"SMS notification: {message}")

# Strategy pattern
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float) -> str:
        return f"Paid ${amount} via Credit Card"

class PayPalPayment(PaymentStrategy):
    def pay(self, amount: float) -> str:
        return f"Paid ${amount} via PayPal"

class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy
    
    def set_strategy(self, strategy: PaymentStrategy):
        self._strategy = strategy
    
    def process_payment(self, amount: float) -> str:
        return self._strategy.pay(amount)

# Using advanced patterns
# Protocol usage
circle = Circle(5)
rectangle = Rectangle(10, 4)

render_shape(circle)
render_shape(rectangle)

# Singleton pattern
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(f"Same instance: {db1 is db2}")

# Observer pattern
subject = Subject()
email_notifier = EmailNotifier()
sms_notifier = SMSNotifier()

subject.attach(email_notifier)
subject.attach(sms_notifier)
subject.notify("System update available")

# Strategy pattern
processor = PaymentProcessor(CreditCardPayment())
print(processor.process_payment(100.0))

processor.set_strategy(PayPalPayment())
print(processor.process_payment(50.0))

# Factory pattern
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type: str):
        if animal_type.lower() == "dog":
            return Dog()
        elif animal_type.lower() == "cat":
            return Cat()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

# Using factory
animal = AnimalFactory.create_animal("dog")
print(f"Dog says: {animal.speak()}")

animal = AnimalFactory.create_animal("cat")
print(f"Cat says: {animal.speak()}")

# You've mastered advanced Python! Ready for production-level development!
