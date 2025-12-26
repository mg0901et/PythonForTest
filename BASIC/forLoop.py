#FOR LOOP IN PYTHON

# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
# With the for loop we can execute a set of statements, once for each item in a sequence.

# Example 1: Iterating through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)    
print("FOR LOOP ENDS HERE \n")
# Example 2: Iterating through a string
for letter in "banana":
    print(letter)
print("FOR LOOP ENDS HERE \n")

# Example 3: Using the range() function
for i in range(5):
    print(i)
print("FOR LOOP ENDS HERE \n")

cities = [["New York", "NY"], ["Los Angeles", "CA"], ["Chicago", "IL"]]
for city, state in cities:
    print(f"{city} is in {state}")
print("FOR LOOP ENDS HERE \n")

my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict.items())
for key, value in my_dict.items():
    print(f"{key}: {value}")
print("FOR LOOP ENDS HERE \n")

