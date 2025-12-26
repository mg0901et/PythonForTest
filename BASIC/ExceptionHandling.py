#Exception Handling in Python

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except TypeError:
        return "Error: Invalid input type. Please provide numbers."
    else:
        return f"The result is {result}"
    finally:
        print("Execution of divide_numbers is complete.")   #This block always executes

print(divide_numbers(10, 2))  # Valid division 
print(divide_numbers(10, 0))  # Division by zero
print(divide_numbers(10, 'a'))  # Invalid input type
print("\n")
# Raise Exception Example
def check_positive(number):
    if number < 0:
        raise ValueError("The number must be positive.")
    return f"{number} is a positive number."

try:
    print(check_positive(5))  # Valid input
    print(check_positive(-3))  # This will raise an exception
except ValueError as ve:
    print(f"Caught an exception: {ve}") 