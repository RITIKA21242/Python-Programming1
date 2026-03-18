#  Create a class of student (name, sap id, marks[phy,chem,maths]). Create 3 
# objects by taking inputs from the user and display details of all students.  

class student_details:
    def __init__(self, name, sap_id, maths, cs, phy):
        self.name = name
        self.sap_id = sap_id
        self.maths = maths
        self.cs = cs
        self.phy = phy
    
    def display(self):
        print("Name : ", self.name)
        print("Sap ID: ", self.sap_id)
        print("Maths marks: ", self.maths)
        print("CS marks: ", self.cs)
        print("Physics Marks: ", self.phy)
    
    def calculate_average(self):
        return(self.maths + self.cs + self.phy) / 100
    
    def show_results(self):
        if self.maths > 40 and self.cs > 40 and self.phy > 40:
            print("Result: Pass")
        else:
            print("Result: Fail")


student = []
n = int(input("enter no of student details to be displayed: "))

for i in range(n):
    print("Enter details of student")
    name=input("Enter name: ")
    sapid= int(input("enter your sapid: "))
    maths= int(input("enter marks of maths: "))
    cs = int(input("enter marks of cs: "))
    phy = int(input("enter marks of physics: "))

s = student_details(name , sapid, maths, cs, phy)
student.append(s)

percentage = 0

print("\n ---Student Details---")
for s in student:
    s.display()
    print("Percentage: ", s.calculate_average())
    s.show_results()
    print()
    percentage += s.calculate_average()

print("Class Average: ", percentage / n )
