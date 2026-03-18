# Program to Implement Different Types of Inheritance
# (a) Single Inheritance
# (b) Multilevel Inheritance

class Parent:
    def show(self):
        print("This is Parent class")

class Child(Parent):
    def display(self):
        print("This is Child class")

c = Child()
c.show()
c.display()

class GrandParent:
    def gshow(self):
        print("GrandParent class")

class Parent(GrandParent):
    def pshow(self):
        print("Parent class")

class Child(Parent):
    def cshow(self):
        print("This is Child class")

obj = Child()
obj.gshow()
obj.pshow()
obj.cshow()