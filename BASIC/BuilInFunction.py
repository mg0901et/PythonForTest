#BUILT-IN FUNCTIONS

#MAX
demo_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
max_value = max(demo_list)
print("Maximum value in the list:", max_value)

#MIN
min_value = min(demo_list)
print("Minimum value in the list:", min_value)

#iter
i = iter(demo_list)
print("First element using iter():", next(i))
print("First element using iter():", next(i))

#reversed
j = reversed(demo_list)
print("Elements in reverse:", next(j))
print("Elements in reverse :", next(j))

#Slice
print("Original list:", demo_list)
x = slice(0, 8, 2) #slice from index 0 to 8 with step 2
print("Sliced list:", demo_list[x])

#SORT
unsorted_list = [34, 12, 5, 67, 23, 89, 1]
print("Unsorted list:", unsorted_list)
unsorted_list.sort()
print("Sorted list:", unsorted_list)

#SUM
sum_value = sum(demo_list)
print("Sum of all elements in the list:", sum_value)

#INPUT
