"""
Boolean and Operators
"""

like_coffee = True
like_tea = False

favorite_food = "Pizza"
favorite_number = 32

print(type(like_coffee))
print(type(like_tea))
print(type(favorite_food))
print(type(favorite_number))

# Comparison Operators in Python

# == (equal to)

print(2 == 3)  # It will return false.
print(5 == 5)  # It will return true.

# != (not equal to)

print(2 != 4)  # It will return true.
print(4 != 4)  # It will return false.

# > (greater than)

print(1 > 3)  # It will return false.
print(3 > 1)  # It will return true.

# >= (greater than or equal to)
print(2 >= 2)  # It will return true.
print(3 >= 2)  # It will return true.
print(2 >= 4)  # It will return false.

# < (less than)

print(1 < 4)  # It will return true.
print(5 < 3)  # It will return false.

# <= (less than or equal to)

print(2 <= 5)  # It will return true.
print(5 <= 2)  # It will return false.

# Logical Operators in Python
print(1 > 3 and 5 < 7)  # Since the first condition is False, it will return False.
print(
    1 > 3 or 5 < 7)  # It will return true since the 2nd condition is true. For the or statement, it is sufficient for 1 condition to be true.

print(not (2 == 2))  # '2 == 2' will return True. Since 'not True' is False, the whole expression will return False.
