#program to check whether a number is palindrome or not
#Take input form user
i=int(input("Enter a number: "))
#variable to store a number
rev=0
x=i
while (i>0):
    rev=(rev*10)+i%10
    i=i//10
#print the  number
if(x==rev):
    print("it is palindrome number")
else:
    print("it is not a palindrome number");

''' OUTPUT:
 Enter a number: 525
it is palindrome number

Enter a number: 123
it is not a palindrome number '''
