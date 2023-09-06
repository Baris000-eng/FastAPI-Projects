"""
Standard Libraries in Python
"""

# Random and Math Libraries
import random
import math

types_of_foods = ["Hamburger", "Hot Dog", "Schnitzel", "Salad", "Pasta", "Pizza"]
print(
    random.choice(types_of_foods))  # It will give a randomly selected food type from the list called 'types_of_foods'.
print(
    random.randint(1, 10))  # It will print a random number between 1 and 10, where 1 is inclusive and 10 is exclusive.

square_root = math.sqrt(81)
print(square_root)  # It will give 9. Because the square root of 81 is equal to 9.
