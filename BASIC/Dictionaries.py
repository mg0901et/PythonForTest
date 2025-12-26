#Dictionaries in Python
#Disctionaries are used to store data values in key:value pairs.

demo_dict = {}
print("Empty Dictionary:", demo_dict)
print("Type of demo_dict:", type(demo_dict))

demo_dict = {'Name': 'John', 'Age': 25, 1: 'New York'}
print("Dictionary with values:", demo_dict)

print("Accessing value with key 'Name':", demo_dict['Name'])

demo_dict['job'] = 'Engineer'
print("Dictionary after adding new key-value pair:", demo_dict)

demo_dict['Age'] = 26
print("Dictionary after updating 'Age':", demo_dict)

demo_dict.pop(1)
print("Dictionary after removing key 1:", demo_dict)    

demo_dict.popitem()
print("Dictionary after removing last item:", demo_dict)

print(demo_dict.get('Name'))
print(demo_dict.keys())
print(demo_dict.values())
print(demo_dict.items())

demo_dict.update({'Country': 'USA'})
print("Dictionary after update:", demo_dict)

