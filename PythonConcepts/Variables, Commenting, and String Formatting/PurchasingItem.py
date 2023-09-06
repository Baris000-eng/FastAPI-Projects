"""
 - You have 50 dollars.
 - You buy an item that is 15 dollars.
 - With a tax of 3%.
 - print how much money you have left.
"""

initial_money = 50
item_price = 15
tax_percentage = 0.03
remaining_money = initial_money - item_price * (1 + tax_percentage)
print(remaining_money)
