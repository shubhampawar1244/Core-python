#program to check leap year or not

year=int(input("Enter a year:"))
#Perform operation
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#Display result
    print(f"{year} is a leap year.")
#Display result
else:
    print(f"{year} is not a leap year.")
''' OUTPUT:
 Enter a year:2000
2000 is a leap year. '''
