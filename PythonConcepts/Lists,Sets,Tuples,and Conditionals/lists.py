"""
Lists are the collections of data
"""

my_list = [77, 91, 65, 100, 4]
print(my_list)
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[4])
# print(my_list[5]) This will give an index out of bounds error.

list_of_people = ["Mike", "David", "Harry"]
print(list_of_people)
print("The first element of the people list: " + str(list_of_people[0]))
print("The second element of the people list: " + str(list_of_people[1]))
print("The third element of the people list: " + str(list_of_people[2]))

list_of_people[1] = "Karl"
print("The updated people list: " + str(list_of_people) + "")

# usage of len function on the list to find the length of the list
print("There are " + str(len(list_of_people)) + "")

# slicing the list
first_two_elements = list_of_people[0:2]  # this will get the first two elements from the list called 'list_of_people'
print(first_two_elements)
print("--------------------------------------------------------")
print(my_list)
my_list.append(10000)
print(my_list)
my_list.insert(3, 1000)  # It will insert 1000 to the 3rd index and shift other list elements accordingly
print(my_list)
my_list.remove(65)  # It will remove 65 from the list.
print(my_list)
my_list.pop(0)  # it will remove the element at index 0 from the list.
print(my_list)

my_list.sort()  # usage of sort() function to sort the list in an ascending order.
print(my_list)
