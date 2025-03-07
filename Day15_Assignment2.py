#Write a function in Python to count and display the total number of words in a text file “ABC.txt”


#Creating function
def Word_count():
    
#counter variable    
    count = 0

#handeling error    
    try:                 
        with open("ABC.txt" ,"r") as file_open:
            for line in file_open:
#counting number of words
                count += len(line.split())



    except FileNotFoundError:

#if file not found gives message
        print("file not found")        
    return count

#calling function and storing value
result = Word_count()                   
print(f"the numbers of words count is: {result}")    

''' OUTPUT:

 the numbers of words count is: 4'''
