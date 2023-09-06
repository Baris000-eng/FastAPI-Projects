"""
Sets are similar to lists but are unordered and
cannot contain duplications.
"""

my_set = {2, 3, 4, 2, 9, 8, 9, 9, 7, 1, 1, 2, 0}
print(my_set)  # prints my_set and gets rid of duplications
print(len(my_set))  # finds the length of my_set

# Usage of for loop in python
for y in my_set:
    print(y)

my_set.discard(4)  # if it is present, the element with the value 4 is deleted from my_set after the discard operation.
print(my_set)  # prints the updated set called my_set.

my_set.clear()  # removes all elements from the set.
print(my_set)

my_set.add(11)  # adds 11 to the set
print(my_set)

my_set.update([8, 9, 10])  # adds 8,9, and 10 to the set called my_set.
print(my_set)
