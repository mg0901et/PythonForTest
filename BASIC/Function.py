#FUNCTION IN PYTHON

def greet(name):
    """
    This called a Docstring.
    This Fuction Greets the person with the given name.
    
    :param name: Person's name as a string.
    :return: Greeting message as a string.

    """
    return "Hello, " + name + "!"   


print(greet("Alice"))  # Output: Hello, Alice!  
print(greet("Bob"))    # Output: Hello, Bob!

def add(a, b):
    return a + b
print("Sum of 5 and 3 is:", add(5, 3))       # Output: 8
print("Sum of -1 and 1 is:", add(-1, 1))      # Output: 0


#Parameter vs Argument
def multiply(x, y):  # x and y are parameters
    return x * y    

print("Product of 4 and 5 is:", multiply(4, 5))  # 4 and 5 are Arguments


#postional Arguments
def subtract(a, b): 
    return a - b 

print("Subtracting 5 from 10 gives:", subtract(10, 5))  #10 and 5 are Positional Arguments

#Required Arguments
def divide(a, b):
    return a / b
print("Dividing 10 by 2 gives:", divide(10, 2))  # Both arguments are Required Arguments

#Optional Arguments

def power(base, exponent=2):  # exponent is an Optional Argument with default value 2
    return base ** exponent 

print("2 raised to the power of 3 is:", power(2, 3))  # Output: 8
print("3 squared is:", power(3))                      # Output: 9 (uses default exponent 2)

#Keyword Arguments
def introduce(name, age):
    return f"My name is {name} and I am {age} years old."   

print(introduce(age=25, name="Charlie"))  # Using Keyword Arguments
# Output: My name is Charlie and I am 25 years old.