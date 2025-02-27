#program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer

#declare 
def get_integer():
    """Prompt the user for an integer and raise a ValueError if input is invalid."""
    try:

# Prompt user for an integer
        return int(input("Enter an integer: "))  
    except ValueError:

# Raise error if input is not an integer
        raise ValueError("Invalid input! Please enter a valid integer.")  


try:

# Get a valid integer from the user
    num = get_integer()

#Print the entered integer    
    print(f"You entered: {num}")  
except ValueError as e:

#Print the error message if input is invalid
    print(e)

''' OUTPUT:
 Enter an integer: 45
You entered: 45 '''
