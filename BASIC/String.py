#String Operations in Python

x = "Hello, World!"
print(x)                  # Output the string

print(x[0])               # Output the first character of the string
print(x[7:12])           # Output characters from position 7 to 11

x = "Hello, \"World!\""
print(x)              # Output string with escaped quotes

z = """This is a
multiline string.
It can span multiple lines."""
print(z)              # Output the multiline string

print("string" in z)    # Check if "string" is in z
print("Python" not in z) # Check if "Python" is not in z

#String Functions
a = " Hello, World! "
print(len(a))               # Output the length of the string

y = 10
print(type(y))              # Output the type of variable y 
print(type(str(y)))         # Convert y to string and output

print(a.find("World"))      # Find the position of "World" in a 

print(a.upper())          # Convert a to uppercase
print(a.lower())          # Convert a to lowercase  
print(a)

print(a.count("o"))        # Count occurrences of "o" in a

print(a.replace("H", "J"))  # Replace "H" with "J" in a

print(a.isupper())        # Check if a is uppercase
print(a.islower())        # Check if a is lowercase

print(a.split(","))      # Split a into a list at each comma

print(a.strip())         # Remove leading and trailing whitespace from a


#String Slicing
a = "Hello, World!"
print(a[2:5])            # Output characters from position 2 to 4
print(a[:5])             # Output the first 5 characters
print(a[2:])             # Output from position 2 to the end
print(a[-5:-2])          # Output characters from position -5 to -3     
print(a[::-1])           # Output the string in reverse order


#String Formatting

x = "Mayank Python"
y = "Trying to learn everthing"

print("Welcome to " + x + ", " + y)  # Concatenate strings using +
print(f"Welcome to {x}, {y}")          # Using f-strings for formatting

