from fpdf import FPDF

# Create PDF instance
pdf = FPDF()

# Configure PDF settings
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_margins(left=10, right=10, top=10)

# Add first page
pdf.add_page()
pdf.set_font("Arial", size=14)

# --- Title Section ---
pdf.set_fill_color(173, 216, 230)  # Light blue background
pdf.cell(0, 10, "Complete Python Basics Guide", ln=1, fill=True, align='C')
pdf.ln(10)

# --- Helper Function for Code Blocks ---
def add_code_block(pdf, code, indent=4):
    pdf.set_font("Courier", size=10)
    pdf.set_text_color(0, 0, 128)  # Dark blue
    for line in code.split('\n'):
        pdf.cell(indent)  # Add indentation
        pdf.multi_cell(0, 5, line)
    pdf.ln(3)
    pdf.set_font("Arial", size=12)
    pdf.set_text_color(0, 0, 0)  # Reset to black

# --- 1. Variables & Data Types ---
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, "1. Variables & Data Types", ln=1)
pdf.set_font("Arial", size=10)
pdf.multi_cell(0, 6, "Python uses dynamic typing. Basic types include:")
code = '''# Integer
age = 25
# Float
price = 9.99
# String
name = "Alice"
# Boolean
is_valid = True
# Type checking
print(type(age))  # Output: <class 'int'>'''
add_code_block(pdf, code)

# --- 2. Operators ---
pdf.set_font("Arial", 'B', 12)
pdf.set_text_color(0, 100, 0)  # Dark green
pdf.cell(0, 10, "2. Operators", ln=1)
code = '''# Arithmetic
print(10 + 3)   # Addition
print(2 ** 4)   # Exponentiation

# Comparison
print(5 > 3)    # True
print("a" == "A")  # False

# Logical
has_license = True
has_car = False
print(has_license and has_car)  # False'''
add_code_block(pdf, code)

# --- 3. Control Flow ---
pdf.set_font("Arial", 'B', 12)
pdf.set_text_color(139, 0, 0)  # Dark red
pdf.cell(0, 10, "3. Control Flow", ln=1)
code = '''# If-elif-else
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
else:
    grade = 'C'

# Ternary operator
result = "Pass" if score >= 60 else "Fail"'''
add_code_block(pdf, code)

# --- 4. Loops ---
pdf.set_font("Arial", 'B', 12)
pdf.set_text_color(128, 0, 128)  # Purple
pdf.cell(0, 10, "4. Loops", ln=1)
code = '''# For loop
for i in range(3):
    print(f"Number {i}")

# While loop
count = 3
while count > 0:
    print(count)
    count -= 1

# Loop control
for num in range(10):
    if num == 5:
        break
    print(num)'''
add_code_block(pdf, code)

# --- 5. Functions ---
pdf.set_font("Arial", 'B', 12)
pdf.set_text_color(0, 0, 128)  # Navy blue
pdf.cell(0, 10, "5. Functions", ln=1)
code = '''# Function definition
def calculate_area(width, height):
    """Calculate rectangle area"""
    return width * height

# Function call
print(calculate_area(5, 4))  # 20

# Default parameters
def greet(name="Guest"):
    print(f"Hello, {name}!")'''
add_code_block(pdf, code)

# --- 6. Data Structures ---
pdf.set_font("Arial", 'B', 12)
pdf.set_text_color(255, 140, 0)  # Dark orange
pdf.cell(0, 10, "6. Data Structures", ln=1)

pdf.set_font("Arial", 'I', 10)
pdf.cell(0, 6, "Lists:", ln=1)
code = '''fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits[1])  # banana'''
add_code_block(pdf, code)

pdf.set_font("Arial", 'I', 10)
pdf.cell(0, 6, "Dictionaries:", ln=1)
code = '''person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(person.get("age"))  # 30'''
add_code_block(pdf, code)

# --- 7. File Handling ---
pdf.set_font("Arial", 'B', 12)
pdf.set_text_color(0, 128, 128)  # Teal
pdf.cell(0, 10, "7. File Handling", ln=1)
code = '''# Writing to file
with open("data.txt", "w") as file:
    file.write("Hello World")

# Reading from file
with open("data.txt", "r") as file:
    content = file.read()
print(content)'''
add_code_block(pdf, code)

# --- 8. OOP ---
pdf.set_font("Arial", 'B', 12)
pdf.set_text_color(128, 0, 0)  # Maroon
pdf.cell(0, 10, "8. Object-Oriented Programming", ln=1)
code = '''class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print(f"{self.name} says woof!")

buddy = Dog("Buddy")
buddy.bark()'''
add_code_block(pdf, code)

# --- 9. Error Handling ---
pdf.set_font("Arial", 'B', 12)
pdf.set_text_color(139, 69, 19)  # Brown
pdf.cell(0, 10, "9. Error Handling", ln=1)
code = '''try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Cleanup done")'''
add_code_block(pdf, code)

# --- 10. Advanced Features ---
pdf.set_font("Arial", 'B', 12)
pdf.set_text_color(0, 100, 0)  # Dark green
pdf.cell(0, 10, "10. Advanced Features", ln=1)

pdf.set_font("Arial", 'I', 10)
pdf.cell(0, 6, "List Comprehensions:", ln=1)
code = '''squares = [x**2 for x in range(5)]
evens = [x for x in range(10) if x % 2 == 0]'''
add_code_block(pdf, code)

pdf.set_font("Arial", 'I', 10)
pdf.cell(0, 6, "Lambda Functions:", ln=1)
code = '''square = lambda x: x ** 2
print(square(5))  # 25'''
add_code_block(pdf, code)

# --- Finalize PDF ---
pdf.set_font("Arial", size=10)
pdf.set_text_color(0, 0, 0)
pdf.ln(10)
pdf.multi_cell(0, 6, "End of Python Basics Guide. Created with FPDF.")

# Save output
pdf.output("complete_python_guide.pdf")
print("PDF generated successfully: complete_python_guide-2.pdf")