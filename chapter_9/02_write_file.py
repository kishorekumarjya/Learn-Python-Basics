import os

content = "Hi Dear, This is Kishore Kumar\nThis is my friend \r 6:40 Am - 7% Battery charges"

# Define the directory and file path
directory = "chapter_9/docs"
file_path = os.path.join(directory, "writeMyfile.txt")

# Check if the directory exists, if not, create it
if not os.path.exists(directory):
    os.makedirs(directory)

# Open the file and write content
with open(file_path, "w") as f:
    f.write(content)
