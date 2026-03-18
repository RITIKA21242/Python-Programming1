# uestion 4: Multiple Objects of a Class

# Q.
# Write a Python program to create a class Laptop with data members brand and ram.
# Define a function to display laptop details.
# Create two objects of the class with different values and display their details.

class laptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram

    def show_details(self):
        print("Brand : ", self.brand)
        print("Ram: ", self.ram, "GB")

l1 = laptop("HP", 8)
l2 = laptop("Lenevo", 16)

l1.show_details()
l2.show_details()