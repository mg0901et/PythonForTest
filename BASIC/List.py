#Define a list
my_list = [1, 2, 3, 4, 5, "hello", 3.14, True]

print("Original List:", my_list)

print(my_list[0])        # Access first element
print(my_list[-1])       # Access last element
print(my_list[2:5])     # Slicing

print(type(my_list))  # Check type

print(my_list.append(6))  # Append element
print("After Append:", my_list)

print(my_list.remove("hello"))  # Remove element
print("After Remove:", my_list)

print(len(my_list))  # Length of list
print(my_list.count(3))  # Count occurrences of 3

my_list.sort()  # Sort the list (will raise error due to mixed types)
print("After Sort:", my_list)

my_list.reverse()  # Reverse the list
print("After Reverse:", my_list)

my_list.insert(2, "new")  # Insert element at index 2
print("After Insert:", my_list) 

print(my_list.index(4))  # Find index of element 4

my_list.clear()  # Clear the list
print("After Clear:", my_list)

