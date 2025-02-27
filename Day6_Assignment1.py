#program to reverse a number using a while loop
# Take input from the user
i=int(input("Enter a reverse number: "))
# Variable to store the reversed number
rev=0
#display operation
while (i>0):
    rev=(rev*10)+i%10
    i=i//10
#print the reverse number
print("The reverse number is: ",rev);

''' OUTPUT:
  Enter a reverse number: 289
The reverse number is:  982 '''
