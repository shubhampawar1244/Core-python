#program to declare a div() function with two parameters then call the function and pass two numbers and display their division
#Declare two parameters
def div(a,b):
    if b==0:
        return "Division by zero is not allowed"
    return a/b
# Call the function 
num1=20
num2=10
#display the result
result= div(num1,num2)
print(f"Division of {num1} by {num2} is:{result}")

''' OUTPUT:
 Division of 20 by 10 is:2.0 '''
