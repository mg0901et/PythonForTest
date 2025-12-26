# ZIP FUNCTION
# It Can work with multiple iterables (like lists, tuples, etc.)
#In Set and Dictionary it will not work because they are unordered collections.

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3, 4]

zipped = zip(list1, list2)
print(zipped)  # Output: <zip object at ...>
print(type(zipped))  # Output: <class 'zip'>
print(list(zipped))  # Output: [('a', 1), ('b', 2), ('c', 3)]

for x, y in zip(list1, list2):
    print(x, y)
