from fpdf import FPDF

class VSCodePDF(FPDF):
    def __init__(self):
        super().__init__()
        # VS Code color scheme
        self.colors = {
            'background': (40, 44, 52),    # VS Code dark theme bg
            'text': (212, 212, 212),       # Default text color
            'keyword': (86, 156, 214),     # Blue for keywords
            'string': (152, 195, 121),     # Green for strings
            'comment': (106, 153, 85),     # Gray-green for comments
            'function': (220, 220, 170),   # Yellow for functions
            'number': (184, 215, 163),     # Light green for numbers
            'operator': (197, 134, 192)    # Purple for operators
        }
    
    def add_vscode_codeblock(self, code, lang='python'):
        self.set_font('Courier', '', 10)
        self.set_draw_color(*self.colors['background'])
        self.set_line_width(0.5)
        
        # Code block background
        self.set_fill_color(*self.colors['background'])
        self.rect(self.x, self.y, 190, 7 * (code.count('\n') + 2), 'DF')
        
        # Code content
        self.set_xy(self.x + 4, self.y + 2)
        for line in code.split('\n'):
            self._add_vscode_line(line)
            self.ln(5)
        self.ln(3)

    def _add_vscode_line(self, line):
        original_x = self.x
        in_string = False
        string_char = ''
        buffer = ''
        color_stack = []

        def flush_buffer():
            if buffer:
                self.set_text_color(*current_color)
                self.cell(self.get_string_width(buffer), 5, buffer)
                return self.get_x()
            return original_x

        current_color = self.colors['text']
        
        i = 0
        while i < len(line):
            char = line[i]
            
            # Handle strings
            if char in ('"', "'") and not in_string:
                in_string = True
                string_char = char
                flush_buffer()
                buffer = ''
                current_color = self.colors['string']
                i += 1
                continue
            elif in_string and char == string_char:
                in_string = False
                flush_buffer()
                buffer = ''
                current_color = self.colors['text']
                i += 1
                continue
            
            # Handle comments
            if char == '#' and not in_string:
                flush_buffer()
                buffer = line[i:]
                self.set_text_color(*self.colors['comment'])
                self.cell(self.get_string_width(buffer), 5, buffer)
                break
            
            # Handle keywords
            if not in_string:
                for keyword in ['def', 'class', 'if', 'else', 'elif', 'for', 
                               'while', 'return', 'import', 'from', 'as', 'try',
                               'except', 'finally', 'with', 'True', 'False', 'None']:
                    if line[i:i+len(keyword)] == keyword and \
                       (i + len(keyword) >= len(line) or not line[i+len(keyword)].isalnum()):
                        flush_buffer()
                        self.set_text_color(*self.colors['keyword'])
                        self.cell(self.get_string_width(keyword), 5, keyword)
                        i += len(keyword)
                        buffer = ''
                        current_color = self.colors['text']
                        break
                else:
                    buffer += char
                    i += 1
            else:
                buffer += char
                i += 1

        flush_buffer()
        self.set_x(original_x + 4)
        self.ln(5)

# --- Create PDF with VS Code Styling ---
pdf = VSCodePDF()
pdf.add_page()
pdf.set_margins(10, 10, 10)

# Title
pdf.set_font('Arial', 'B', 16)
pdf.set_text_color(86, 156, 214)  # VS Code blue
pdf.cell(0, 10, "Python Basics in VS Code Style", ln=True, align='C')
pdf.ln(15)

# Variables Section
pdf.set_font('Arial', 'B', 12)
pdf.set_text_color(*pdf.colors['text'])
pdf.cell(0, 10, "1. Variables and Data Types", ln=True)
code = '''# Variable declaration
name = "Alice"  # String
age = 30        # Integer
price = 19.99   # Float
is_valid = True # Boolean'''
pdf.add_vscode_codeblock(code)

# Functions Section
pdf.ln(10)
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, "2. Functions", ln=True)
code = '''def calculate_total(price, quantity=1):
    """Calculate total price with tax"""
    tax_rate = 0.08
    total = (price * quantity) * (1 + tax_rate)
    return round(total, 2)'''
pdf.add_vscode_codeblock(code)

# Control Flow Section
pdf.ln(10)
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, "3. Control Flow", ln=True)
code = '''# If-elif-else statement
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
else:
    grade = 'C'

# Ternary operator
status = "Pass" if score >= 60 else "Fail"'''
pdf.add_vscode_codeblock(code)

# Class Example
pdf.ln(10)
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, "4. Classes and Objects", ln=True)
code = '''class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

rect = Rectangle(5, 3)
print(f"Area: {rect.area()}")'''
pdf.add_vscode_codeblock(code)

# Error Handling
pdf.ln(10)
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, "5. Error Handling", ln=True)
code = '''try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
finally:
    print("Cleanup complete")'''
pdf.add_vscode_codeblock(code)

# Save PDF
pdf.output("python_vscode_style-6.pdf")
print("PDF generated with VS Code styling!")