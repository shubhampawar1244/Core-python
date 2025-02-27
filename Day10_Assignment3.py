#program to find duplicate values from a list and display those

# Initialize an empty list to store duplicates
def find_duplicates(input_list):
    duplicates = []  
    
    for i in range(len(input_list)):  
        for j in range(i + 1, len(input_list)): 
            if input_list[i] == input_list[j] and input_list[i] not in duplicates:
 # Add the duplicate to the list
                duplicates.append(input_list[i])
                
 # Return the list of duplicates   
    return duplicates  

#define a list
input_list = [1, 2, 3, 4, 5, 1, 2, 6, 7, 8, 4]
# Call the function to find duplicates
duplicates = find_duplicates(input_list)

# Display the duplicate values
print("Duplicate values:", duplicates)

''' OUTPUT:
 Duplicate values: [1, 2, 4] '''
