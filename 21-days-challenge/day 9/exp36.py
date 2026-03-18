# Dictionary of students and cities

n = int(input("enter number of students: "))
d={}

for _ in range(n):
    name = input("enter name: ")
    city = input("enter city: ")
    d[name] = city

print("Names : ")
for name in d:
    print(name)

print("Cities: ")
for city in d.values(): 
    print(city)


print("Student Details : ")
for name, city in d.items():
    print(name, "-", city)

city_count = {}
for city in d.values():
    city_count[city] = city_count.get(city, 0) + 1

print ("Students per city: ")
for city, count in city_count.items():
    print(city, ":", count)