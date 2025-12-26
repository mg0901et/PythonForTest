#Aritimatics Operators
a = 10  
b = 3
print("Addition:", a + b)          # Addition
print("Subtraction:", a - b)       # Subtraction
print("Multiplication:", a * b)    # Multiplication
print("Division:", a / b)          # Division
print("Reminder:", a % b)           # Modulus
print("Exponentiation:", a ** b)   # Exponentiation
print("Floor Division:", a // b)   # Floor Division 

#Assignment Operators
x = 5
print("\nInitial value of x:", x)
x += 2
print("After x += 2:", x)
x -= 1
print("After x -= 1:", x)
x *= 3
print("After x *= 3:", x)
x /= 2
print("After x /= 2:", x)
x %= 4
print("After x %= 4:", x)
x **= 2
print("After x **= 2:", x)
x //= 3
print("After x //= 3:", x)  


#Comparison Operators
p = 7
q = 10
print("\nIs p equal to q?", p == q)          # Equal    
print("Is p not equal to q?", p != q)        # Not Equal
print("Is p greater than q?", p > q)         # Greater Than
print("Is p less than q?", p < q)            # Less Than
print("Is p greater than or equal to q?", p >= q)  # Greater Than or Equal To
print("Is p less than or equal to q?", p <= q)   # Less Than or Equal To

#Logical Operators
m = True
n = False
print("\nLogical AND (m and n):", m and n)   # Logical AND
print("Logical OR (m or n):", m or n)         # Logical OR
print("Logical NOT (not m):", not m)          # Logical NOT 

#identity Operators
str1 = "hello"
str2 = "hello"
str3 = str1
print("\nIs str1 identical to str2?", str1 is str2)   # Identity Operator
print("Is str1 identical to str3?", str1 is str3)     # Identity Operator
print("Is str1 not identical to str2?", str1 is not str2) # Identity Operator
print("Is str1 not identical to str3?", str1 is not str3) # Identity Operator

#Membership Operators
my_list = [1, 2, 3, 4, 5]
print("\nIs 3 in my_list?", 3 in my_list)         # Membership Operator
print("Is 6 not in my_list?", 6 not in my_list)  # Membership Operator

#Bitwise Operators
c = 5      # In binary: 0101
d = 3      # In binary: 0011
print("\nBitwise AND (c & d):", c & d)       # Bitwise AND
print("Bitwise OR (c | d):", c | d)          # Bitwise OR
print("Bitwise XOR (c ^ d):", c ^ d)         # Bitwise XOR
print("Bitwise NOT (~c):", ~c)                # Bitwise NOT
print("Left Shift (c << 1):", c << 1)    # Left Shift
print("Right Shift (c >> 1):", c >> 1)   # Right Shift


#Operators Precedence
"""
Parentheses ()
Exponentiation **
Unary +, - 
Multiplication *, Division /, Floor Division //, Modulus %
Addition +, Subtraction -
Comparison Operators
Equality Operators
Logical NOT
Logical AND
Logical OR  
Conditional Expressions
"""
result = 10 + 3 * 2 ** 2 / 4 - 1
print("\nResult of 10 + 3 * 2 ** 2 / 4 - 1:", result)  # Operator Precedence        
# Parentheses to change precedence
result_with_parentheses = (10 + 3) * (2 ** 2) / (4 - 1)
print("Result with parentheses (10 + 3) * (2 ** 2) / (4 - 1):", result_with_parentheses)    # Operator Precedence with Parentheses          
