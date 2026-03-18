#  Check whether a given year is a leap year or not 

year=  int(input("enter year: "))
if (year % 100 == 0) or (year % 4 ==0 and year %100 != 0):
    print("leap year")
else:
    print("not a leap year")  