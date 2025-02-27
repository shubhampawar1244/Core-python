#program to get the largest and smallest number from a list without built in functions
# Initialize largest and smallest with the first element
def find_largest_smallest(lst):
    largest = smallest = lst[0]  
    for num in lst:  
        if num > largest: 
            largest = num
        if num < smallest:  
            smallest = num
# Return the largest and smallest numbers
    return largest, smallest  
# Define the list of numbers
numbers = [3, 1, 8, 2, 6, 7, 5, 4]
# Call the function
largest, smallest = find_largest_smallest(numbers)
# Print the largest number
print("Largest:", largest)
# Print the smallest number
print("Smallest:", smallest)

''' OUTPUT:
 Largest: 8
Smallest: 1 '''

