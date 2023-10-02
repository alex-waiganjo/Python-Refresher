# Reading text from a file
f = open("C:/Users/ALEX/Desktop/Python Refresher/Basics/strings.py","r")
print(f.read())
f.close()

# Writing text to an existing file
f = open("C:/Users/ALEX/Desktop/Python Refresher/Basics/strings.py", "a")
f.write("#Basics ")
f.close()

# Read the content from a file
f = open("C:/Users/ALEX/Desktop/Python Refresher/Basics/strings.py","r")
print(f.readline())
print(f.readline())
f.close()

