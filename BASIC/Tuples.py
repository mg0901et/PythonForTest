#Tuples in Python

demo_tuple = ("apple", "banana", "cherry")
print(demo_tuple)

#Tuples are immutable
#demo_tuple[1] = "orange"  # This will raise a TypeError
print(demo_tuple[1])  # Accessing elements

demo_tuple2 = ("orange",1,10.7,True)
print(demo_tuple2)

#Tuple Length
print(len(demo_tuple2))
print(type(demo_tuple2))

print(demo_tuple.count("banana"))  # Count occurrences of an element

print(demo_tuple.index("cherry"))  # Find index of an element   

for item in demo_tuple:  # Loop through tuple
    print(item)

demo_tuple3 = demo_tuple + demo_tuple2  # Concatenate tuples
print(demo_tuple3)

