#program to find largest among three numbers
#Declare three numbers
num1=10
num2=12
num3=14
#Display Operations
if (num1>=num2) and (num1>=num3):
    largest=num1
elif (num2>=num1) and (num2>=num3):
    largest=num2
else:
    largest=num3
#display result
print("The largest number is:",largest)
''' OUTPUT:
 The largest number is: 14 '''
