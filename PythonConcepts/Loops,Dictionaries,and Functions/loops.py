"""
For & While Loops
"""

my_list = [1, 2, 3, 4, 5]

# It is not an optimized way! We manually typed each element in my_list.
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[4])

print("----------------------")

print()
print()

# an optimized way of printing each element in my_list through the usage of a for loop.
for iterator in my_list:
    print(iterator)

print("----------------------")

for x in range(3, 7):
    print(x)

print("----------------------")
sum_with_for_loop = 0

for y in my_list:
    sum_with_for_loop += y

print("Sum of the list is : " + str(sum_with_for_loop) + "")

print("-----------------------------------")

days_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for day in days_list:
    print(f'Happy {day}!')  # format string usage with day names.

j = 0
# while loop will execute whenever j is less than 9.
while j < 9:
    j += 1
    print(j)

print("-------------------------------")
print("The usage of continue statement in Python.")
#  continue statement in python
k = 0
while k < 6:
    k += 1
    if k == 3:
        continue
    print(k)

print("-------------------------------------")

t = 0
while t < 7:
    t += 1
    if t == 5:  # the loop will pass the case where the value of t becomes equal to 5.
        continue
    print(t)
    if t == 6:
        break  # the loop will stop executing when the t becomes equal to 6.
