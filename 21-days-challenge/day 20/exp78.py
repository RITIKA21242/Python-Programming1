# Question 2: Car Age Calculation

# Q.
# Create a class Car with data members brand and year.
# Initialize these values using a constructor.
# Define a member function calculate_age() that displays the age of the car, assuming the current year is 2026.
# Create an object and call the function.

class car: 
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    
    def calculate_age(self):
        print("Car age: ", 2026 - self.year)

c1 = car("Honda", 2019)
c1.calculate_age()
