"""
Flow Control: If Else Elif
"""

x = 1

# this if statement checks whether the variable x is equal to 1.
if x == 1:
    print("x is 1")

print("Outside of if statement for the integer x")

y = 3
if y > 1:
    print("y is greater than 1")
else:
    print("y is not greater than 1")

print("Outside of the if statement for integer y")

hour = 17

if hour < 15:
    print("Good Morning!")
else:
    print("Good Afternoon!")


second_hour = 13
# If you change the value of second_hour to a value between 15 and 19 (both inclusive), then it will print 'Good Afternoon!'.
# If you change the value of second_hour to a value at least 20, then it will print 'Good Night!'.
if second_hour < 15:
    print("Good Morning!")
elif second_hour < 20:
    print("Good Afternoon!")
else:
    print("Good Night!")



