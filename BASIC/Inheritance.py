#INHERITANCE IN PYTHON

class ParentClass:

    def __init__(self):
        print("Parent class intance")

    def parent_method(self):
        print("This is parent MONEY")


class ChildClass(ParentClass):
    pass

parent1 = ParentClass()
parent1.parent_method()

child1 = ChildClass()
child1.parent_method()



#Multiple Inheritance

# Priority is given to the first child class then there parent class

class MoveCharacter:

    def move_fwd(self):
        print("Move Forward")
    
    def move_bwd(self):
        print("Move Backward")

class JumpCharacter:

    def jump_high(self):
        print("Jump High")
    
    def jump_low(self):
        print("Jump Low")

class pokemon(MoveCharacter, JumpCharacter):
    def move_fwd(self):
        print("Move Forward *2 speed")
    pass

pikachu = pokemon()
pikachu.move_fwd()
pikachu.jump_high()

print("\n")

#Multilevel Inheritance
class GrandParent:
    def grandparent_method(self):
        print("This is grandparent method")

class Parent(GrandParent):
    def parent_method(self):
        print("This is parent method")

class Child(Parent):
    def child_method(self):
        print("This is child method")


child_instance = Child()
child_instance.grandparent_method()
child_instance.parent_method()
child_instance.child_method()
print(Child.mro())  # To show the method resolution order