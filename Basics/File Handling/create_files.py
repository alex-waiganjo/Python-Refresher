# f = open("Readme.md",'w') # Creates file if it does not exist

import os
file_name = 'Readme.md'
f = open(file_name, 'w')
f = open(
    f'C:/Users/ALEX/Desktop/Python Refresher/Basics/File Handling/{file_name}', "a")
content = """# File Handling in Python\n
## Some of the file handling examples include\n
- Creating Files
- Reading Files
- Writing to files
- Removing/deleting Files
"""
f.write(content)
f.close()


# Remove a File
# os.remove("Readme.md")

# Make a Folder
os.mkdir("Data")

# Remove a Folder
# os.rmdir("Slug")
