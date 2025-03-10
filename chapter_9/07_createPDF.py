from fpdf import FPDF

class PythonGuidePDF(FPDF):
    def __init__(self):
        super().__init__()
        # Optimal readability color scheme (light theme)
        self.colors = {
            'background': (255, 255, 255),  # White
            'text': (0, 0, 0),              # Black
            'keyword': (0, 0, 255),         # Blue
            'string': (0, 128, 0),          # Green
            'comment': (128, 128, 128),     # Gray
            'function': (255, 165, 0),      # Orange
            'number': (139, 0, 139),        # Dark magenta
            'operator': (128, 0, 128),      # Purple
            'highlight': (255, 255, 200)    # Light yellow
        }
        self.set_auto_page_break(auto=True, margin=15)
        self.set_margins(10, 10, 10)

    def header_section(self, title):
        self.set_font('Arial', 'B', 14)
        self.set_text_color(0, 0, 139)  # Dark blue
        self.cell(0, 10, title, ln=True)
        self.ln(5)

    def code_block(self, code):
        self.set_fill_color(*self.colors['highlight'])
        self.rect(self.x, self.y, 190, 7 * (code.count('\n') + 1), 'F')
        self._syntax_highlight(code)
        self.ln(10)

    def _syntax_highlight(self, code):
        self.set_font('Courier', '', 12)
        for line in code.split('\n'):
            self._highlight_line(line)
            self.ln(5)

    def _highlight_line(self, line):
        x = self.x
        in_string = False
        buffer = ''
        current_color = self.colors['text']

        for i, char in enumerate(line):
            if char in ('"', "'") and not in_string:
                self._flush_buffer(buffer, current_color)
                buffer = ''
                current_color = self.colors['string']
                in_string = True
            elif in_string and char in ('"', "'"):
                self._flush_buffer(buffer + char, current_color)
                buffer = ''
                current_color = self.colors['text']
                in_string = False
                continue
                
            buffer += char

            # Detect keywords
            if not in_string:
                for kw in ['def', 'class', 'if', 'else', 'elif', 'for', 
                          'while', 'return', 'import', 'from', 'as', 'try',
                          'except', 'finally', 'with', 'async', 'await', 
                          'lambda', 'nonlocal', 'global', 'yield']:
                    if line[i-len(kw)+1:i+1] == kw and (i+1 >= len(line) or line[i+1] in ' \t\n():'):
                        self._flush_buffer(buffer[:-len(kw)], current_color)
                        self._flush_buffer(kw, self.colors['keyword'])
                        buffer = ''

            # Detect comments
            if char == '#' and not in_string:
                self._flush_buffer(buffer, current_color)
                self._flush_buffer(line[i:], self.colors['comment'])
                return

        self._flush_buffer(buffer, current_color)
        self.set_x(x)

    def _flush_buffer(self, text, color):
        if text:
            self.set_text_color(*color)
            self.write(5, text)

# Create PDF
pdf = PythonGuidePDF()
pdf.add_page()

# Cover Page
pdf.set_font('Arial', 'B', 24)
pdf.set_text_color(0, 0, 139)  # Dark blue
pdf.cell(0, 40, "Python Programming Guide", ln=True, align='C')
pdf.set_font('Arial', '', 16)
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 10, "From Basics to Advanced Concepts", ln=True, align='C')
pdf.ln(30)

# Table of Contents
pdf.header_section("Table of Contents")
toc = [
    ("1. Fundamentals", 2),
    ("2. Data Structures", 3),
    ("3. Functions & Modules", 4),
    ("4. OOP Concepts", 5),
    ("5. Advanced Features", 6),
    ("6. Modern Python", 7)
]
for title, page in toc:
    pdf.cell(0, 10, f"{title} ................................ {page}", ln=True)
pdf.add_page()

# --- 1. Fundamentals ---
pdf.header_section("1. Fundamentals")
pdf.code_block('''# Variables and Types
name: str = "Alice"  # Type hinting
age: int = 30        # Integer
PI: float = 3.14159  # Float
is_valid: bool = True

# Formatted strings
print(f"{name} is {age} years old")''')

pdf.code_block('''# Control Flow
numbers = [1, 2, 3, 4, 5]

# List comprehension with condition
squares = [x**2 for x in numbers if x % 2 == 0]
print(squares)  # [4, 16]''')

# --- 2. Data Structures ---
pdf.add_page()
pdf.header_section("2. Data Structures")
pdf.code_block('''# Advanced Dictionary Usage
from collections import defaultdict

word_counts = defaultdict(int)
for word in ["apple", "banana", "apple"]:
    word_counts[word] += 1
print(word_counts)  # defaultdict(<class 'int'>, {'apple': 2, 'banana': 1})''')

pdf.code_block('''# Named Tuples
from typing import NamedTuple

class Point(NamedTuple):
    x: float
    y: float

p = Point(1.5, 2.5)
print(p.x, p.y)  # 1.5 2.5''')

# --- 3. Functions & Modules ---
pdf.add_page()
pdf.header_section("3. Functions & Modules")
pdf.code_block('''# Type Hints and Decorators
from typing import Callable

def log_execution(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_execution
def add_numbers(a: int, b: int) -> int:
    return a + b

print(add_numbers(2, 3))''')

# --- 4. OOP Concepts ---
pdf.add_page()
pdf.header_section("4. OOP Concepts")
pdf.code_block('''# Class Inheritance and Mixins
class Loggable:
    def log(self, message: str):
        print(f"[{self.__class__.__name__}] {message}")

class Shape(Loggable):
    def area(self) -> float:
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
        self.log("Circle created")
    
    def area(self) -> float:
        return 3.14 * self.radius ** 2''')

# --- 5. Advanced Features ---
pdf.add_page()
pdf.header_section("5. Advanced Features")
pdf.code_block('''# Context Managers
from contextlib import contextmanager

@contextmanager
def timed_operation(name: str):
    import time
    start = time.time()
    try:
        yield
    finally:
        duration = time.time() - start
        print(f"{name} took {duration:.2f} seconds")

with timed_operation("Data Processing"):
    # Complex operation here
    time.sleep(0.5)''')

pdf.code_block('''# Generator Expressions
def fibonacci(n: int):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fibonacci(10)))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]''')

# --- 6. Modern Python ---
pdf.add_page()
pdf.header_section("6. Modern Python")
pdf.code_block('''# Async/Await
import asyncio

async def fetch_data(url: str):
    print(f"Fetching {url}")
    await asyncio.sleep(1)
    return f"Data from {url}"

async def main():
    results = await asyncio.gather(
        fetch_data("https://api.com/1"),
        fetch_data("https://api.com/2")
    )
    print(results)

asyncio.run(main())''')

pdf.code_block('''# Data Classes
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    email: str = ""

user = User("Alice", 30)
print(user)  # User(name='Alice', age=30, email='')''')

# Save PDF
pdf.output("python_comprehensive_guide-7.pdf")
print("PDF generated successfully!")