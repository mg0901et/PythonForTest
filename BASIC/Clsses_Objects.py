#OBJECTS IN PYTHON

#CLASS -->> Example A employee Form can be a class
#OBJECT -->> Example An employee named John can be an object of the class employee form


class AreaRectangle:

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth  

    def area(self):
        return self.length * self.breadth
    
rect1 = AreaRectangle(10, 5)  #Creating an object of the class AreaRectangle
print("Area of Rectangle:", rect1.area())  #Calling the area method to calculate area
print("\n")

#Employee class example
class Example:
    pass

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display_employee(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)

emp1 = Employee("John Doe", 30, 50000)
emp1.display_employee()
print("\n")

#CLASS VARIABLE AND INSTANCE VARIABLE

class RateOfInterest:

    Intrest = 6  #Class Variable

    def __init__(self, name, loan):
        self.name = name  #Instance Variable
        self.loan = loan  #Instance Variable  

    def calculate_interest(self):

        print("Total Interest :- ", self.loan * self.Intrest/100) # If we Define RateOfInterest.Intrest it will be treated as class variable

cust1 = RateOfInterest("Alice", 10000)
cust1.calculate_interest()

cust2 = RateOfInterest("Bob", 20000)
cust2.calculate_interest()

cust3 = RateOfInterest("Charlie", 15000)
cust3.Intrest = 7  #Modifying class variable for this instance only
cust3.calculate_interest()
