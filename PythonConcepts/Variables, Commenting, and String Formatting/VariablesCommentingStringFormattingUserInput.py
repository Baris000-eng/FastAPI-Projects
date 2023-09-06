print(2 + 2)
print('Hello Mike!')

"""
Variables 
"""
cost = 10  # cost is a variable name which has a value assigned to 10
print(cost)

tax_percentage = 0.25
tax = cost * tax_percentage
price = cost + tax
print(price)

print("-------------------------------------")

print(10)
print(10 + (10 * 0.25))  # cost+tax where the tax percentage is 0.25.

print("---------------------------------------")

username = "ProgrammingWithBaris"
first_name = "Baris"
print(username)
print(first_name)
print(username + " " + first_name)

first_num = 10
second_num = 2

print(first_num)
print(second_num)

first_num = 1
print(first_num)
print(second_num)

first_name = "Mike"
print(first_name)
first_name = "Melissa"  # this assignment will change the value of the string variable called first_name
print(first_name)

# Python Comments

# Going to print 'Hello World'
print("Hello World")

# Going to print 'Hi Mike'
print("Hi Mike")

# These comments are going over
# Multiple
# Lines

# Multiple lines commenting with three double quotations marks at the start and end.
"""
These comments are going over 
multiple 
lines
"""

# Multiple lines commenting with three single quotations marks at the start and end.
'''
These comments are going over 
multiple 
lines
'''

"""
String Formatting 
"""

initial_name = "Eric"
print("Hi " + initial_name)  # without format string

print(f"Hi {initial_name}")  # with format string

sentence = "Hi {}"

print(sentence.format(initial_name))  # usage of format strings by using the format function.

name = "Baris"
surname = "Kaplan"
print(f"Hi {name} {surname}! I hope you are learning!")

# Getting the user input
"""
User Input
"""

f_name = input("Enter your first name: ")
days = input("How many days before your birthday: ")
print(f_name)
print(days)
print(f"Hi {f_name}, only {days} days before your birthday!")



