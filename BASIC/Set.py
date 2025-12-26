#We will discuss SET here

#A set is an unordered collection data type that is iterable, mutable, and has no duplicate elements.

demo_set = {10,20,30,40,50}  #This is a set
demo_set2 = { 10, "banana", "cherry"}  #This is another set
demo_set3 = set((1,2,3,4,5))  #This is also a set created using set() function

print(demo_set)
print(demo_set2)
print(demo_set3)

demo_set = {10,20,30,40,50,10,20,30}  #Duplicates will be ignored
print(demo_set)  #Output will be {10,20,30,40,50}

demo_set4 = set(())  #Empty set
print(demo_set4)  #Output will be set() 
print( type(demo_set4))  #Output will be <class 'set'>

print(len(demo_set))  #Output will be 5

print(20 in demo_set)  #Output will be True
print(100 in demo_set)  #Output will be False

#Methods in Set

#Adding elements to a set
demo_set.add(60)  #Adding single element
print(demo_set)  #Output will be {10,20,30,40,50,60}

demo_set.remove(30)  #Removing an element, raises KeyError if element not found
print(demo_set)  #Output will be {10,20,40,50,60}

demo_set.discard(100)  #Removing an element, does not raise error if element not found
print(demo_set)  #Output will be {10,20,40,50,60}       

demo_set.pop()  #Removes and returns an arbitrary element from the set
print(demo_set)   

demo_set.clear()  #Removes all elements from the set
print(demo_set)  #Output will be set() 

demo_set1 = {1,2,3}
demo_set2 = {3,4,5}

demo_set3 = demo_set1.union(demo_set2)  #Union of two sets
print("Union of sets:", demo_set3)  #Output will be {1,2,3,4,5}

demo_set4 = demo_set1.intersection(demo_set2)  #Intersection of two sets
print("Intersection of sets:", demo_set4)  #Output will be {3}

demo_set5 = demo_set1.difference(demo_set2)  #Difference of two sets
print("Difference of sets (set1 - set2):", demo_set5)  #Output will be {1,2}

demo_set6 = demo_set2.symmetric_difference(demo_set1)  #Symmetric difference of two sets
print("Symmetric difference of sets:", demo_set6)  #Output will be {1,2,4,5}

print("Update set1 with union of set2:", demo_set1.update(demo_set2))  #Updates set1 with union of set2
print(demo_set1)  #Output will be {1,2,3,4,5}

