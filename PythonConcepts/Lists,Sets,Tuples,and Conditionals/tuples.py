my_tuple = (1, 2, 3, 4, 5, 6)
print(my_tuple)
print(len(my_tuple))  # finds the length of the tuple

print(my_tuple[0])  # prints the first element of the tuple
print(my_tuple[1])  # prints the second element of the tuple
print(my_tuple[2])  # prints the third element of the tuple
print(my_tuple[3])  # prints the fourth element of the tuple
print(my_tuple[4])  # prints the fifth element of the tuple
print(my_tuple[5])  # prints the sixth element of the tuple

# tuples are immutable. We cannot change tuples.
# So the below assignment will give an error.
my_tuple[2] = 999
print(my_tuple)