import keyword
#Define a Variable
#We dont need to define the type of variable while declaring it.

username = "mayank"
print(username)

#print the type of variable
print(type(username))

#Variable can change its value and type
username = 1234
print(username)
print(type(username))

#ID of variable is Same if we define one variables with another
a = 10
b = a
print(id(a))
print(id(b))

#ID of variable changes if we change the value of variable
#ID is dependent on the value of variable
a = 20
print(id(a))
print(id(b))

#Variable Naming Rules

#1. Variable name can contain alphabets, digits and underscore(_)
my_variable1 = "Hello"
print(my_variable1)     

#2. Variable name should not start with digit
#1variable = "World"   # This will give error

#3. Variable name should not contain special characters like @, #, $, etc.
#my@variable = "!"    # This will give error  
  
#4. Variable name should not be a reserved keyword
#for = 10             # This will give error

#5. Variable names are case-sensitive
var = 5
Var = 10
print(var)  # Output: 5
print(Var)  # Output: 10


#Print all reserved keywords in Python
print(keyword.kwlist)