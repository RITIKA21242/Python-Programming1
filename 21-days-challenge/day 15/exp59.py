# Functions to explain concepts
# a) Keyword Argument

def student(name, age):
    print(name, age)

student(age=18, name="Ritika")

# Default Argument

# A value assigned beforehand, used if no argument is passed.

def greet(name = "Guest"):
    print("Hello", name)

greet()
greet("Ritika")