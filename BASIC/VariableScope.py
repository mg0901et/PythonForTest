#SCOPE OF A VARIABLE
#LEGB Rule: Local -> Enclosing -> Global -> Built-in

x = 5  # Global variable
def my_function():
    x = 10  # Local variable
    print("Inside the function, x =", x)

def another_function():
    print("Outside the function, x =", x)


my_function()
another_function()

#GLobal Keyword
def my_global_function():
    global y  # Declare y as a global variable
    y = 15
    print("Inside the function, y =", y)

def print_global_y():
    print("Outside the function, y =", y)

my_global_function()
print_global_y()    

#Enclosing Scope
def outer_function():
    z = 20  # Enclosing variable
    def inner_function():
        print("Inside the inner function, z =", z)
    inner_function()

outer_function()