#program to create a new list that contains the names of employees who work in the 'Sales' department, all in uppercase

#Given Data
employees = [
    {"name": "John Doe", "department": "Sales"},
    {"name": "Jane Smith", "department": "Marketing"},
    {"name": "Emily Johnson", "department": "Sales"},
    {"name": "Michael Brown", "department": "HR"}
]

# Creating a new list containing names of employees in the 'Sales' department, converted to uppercase
sales_employees = [emp["name"].upper() for emp in employees if emp["department"] == "Sales"]

# Print the final list
print(sales_employees)

''' OUTPUT:
 ['JOHN DOE', 'EMILY JOHNSON'] '''
