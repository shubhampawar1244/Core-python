#program to handle a ZeroDivisionError exception when dividing a number by zero

#define method
def safe_division(a, b):
    try:
        
# Perform division        
        result = a / b

#Print the result 
        print(f"Result: {result}")  
    except ZeroDivisionError:

# Handle division by zero
        print("Error: Division by zero is not allowed.")  

#Take numerator form user
num1 = float(input("Enter the numerator: "))

#Take denominator from user
num2 = float(input("Enter the denominator: "))

# Call the function
safe_division(num1, num2)

''' OUTPUT:
 Enter the numerator: 25
Enter the denominator: 5
Result: 5.0  '''
