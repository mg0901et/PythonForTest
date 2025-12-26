# File IO in python  File read and write in python

# Mode 
# 1:Read from a file : r
# 2:Write to a file : w
# 3:Append to a file : a
# 4:Read and Write to a file : r+

# Write to a file
file = open("textfile.txt", "w")  # Open file in write mode
file.write("Hello, World!\n")     # Write a line to the file
file.write("This is a test file.\n")
file.close()                       # Close the file


#Read from a file
file = open("textfile.txt", "r")  # Open file in read mode
content = file.read()              # Read the entire content of the file
print("File Content:\n", content)  # Print the content                   # Close the file
file.close()

file = open("textfile.txt", "r")
readline = file.readline()  # Open file in read mode
print("Read Line:\n", readline)  # Print the content
print("Read Line:\n", file.readline())  # Print the content
file.close()

# Read and Write to a file
file = open("textfile.txt", "r+")  # Open file in read and write
content = file.read()              # Read the entire content of the file
print("File Content Before Write:\n", content)  # Print the content
file.write("Adding a new line.\n")  # Write a new line to the file
file.seek(0)                       # Move the cursor to the beginning of the file
updated_content = file.read()      # Read the updated content of the file
print("File Content After Write:\n", updated_content)  # Print the updated content
file.close()                       # Close the file

print("\n")


# With KeyWord in Python
# We are using the 'with' because in the traditional way we have to close the file manually

# Write to a file
with open("textfile.txt", "w") as file:
    file.write("Hello, World with 'with' keyword!\n")
    file.write("This is a test file using 'with'.\n")  

# Read from a file
with open("textfile.txt", "r") as file:
    content = file.read()
    print("File Content with 'with' keyword:\n", content)


print("\n")

