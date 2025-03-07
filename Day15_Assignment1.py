#Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen


#Creating Function
def Read_file_line():
    try:
        
# Handeling file using try catch block
        with open("ABC.txt" ,"r") as ope_file:
            for line in ope_file:
                
#printing output line after line                
                print(line , end="")

# handeling Error by except block                
    except FileNotFoundError:          
        print("file not found")

#Calling Function
Read_file_line()

''' OUTPUT:

 HELLO, THIS IS SHUBHAM.'''

