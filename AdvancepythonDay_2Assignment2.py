#You have a list of email addresses and you want to extract the domain part (the part after '@') from each email address

#Given Data
emails = ["alice@example.com", "bob@sample.org", "charlie@mydomain.net"]

# Extract the domain part (after '@') from each email address
domains = [email.split("@")[1] for email in emails]

# Print the list 
print(domains)

''' OUTPUT:
 ['example.com', 'sample.org', 'mydomain.net'] '''
