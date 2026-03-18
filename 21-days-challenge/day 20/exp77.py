# Question 1: Student Class

# Q.
# Define a class named Student. The class should have the following data members:

# name (string)

# roll_no (integer)

#  Include a member function display() that prints the student’s name and roll number.
# Create an object of the class and demonstrate the working of the method

class student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
    
    def display(self):
        print("Name: ", self.name)
        print("Roll no :", self.rollno)

s1 = student("Aman", 23)
s1.display()