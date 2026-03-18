# Print grade sheet using marks → percentage → CGPA → grade

name=input("name: ")
roll = int(input("roll number: "))

marks = []
subjects = ["PDS", "Python", "Chemistry", "English", "Physics"]

for sub in subjects:
    marks.append(int(input (f"{sub}marks : ")))
total = sum(marks)
percentage = total / 5
cgpa = percentage / 10

if cgpa <= 3.4: 
    grade = "F"
elif cgpa <= 5.0: 
    grade = "C+"
elif cgpa <= 6.0:
    grade = "B"
elif cgpa <= 7.0:
    grade = "B+"
elif cgpa <= 8.0:
    grade = "A"
elif cgpa <= 9.0:
    grade = "A+"
else:
    grade = "0"


print(" \n --- Grade Sheet ---")
print("Name:", name)
print("Roll number:", roll)
print("percentage is : ", percentage, "%")
print("cgpa :", round(cgpa,1))
print("Grade: ", grade)