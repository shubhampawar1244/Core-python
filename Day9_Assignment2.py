# Assignment - Write a Python program to remove duplicate characters of a given string.

#Given String
input_string = "String and String Function"

#separated string
saperate_string = input_string.split()

#creating new list to store
string_list = []

#iterate over each item in list
for item in saperate_string:
    
# if not in list adding string to it
    if item not in string_list:         
        string_list.append(item)
        
#join the list using join() into normal string
new_string = ' '.join(string_list)

#printing the string
print(new_string)                      

''' OUTPUT: 
 String and Function'''
