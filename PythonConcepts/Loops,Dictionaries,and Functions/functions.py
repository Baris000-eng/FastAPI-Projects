"""
Functions in Python
"""

print("Hello and welcome to functions!")  # print is a built-in function in python


def my_func():
    print("Inside my_func")


my_func()  # calling the function named as 'my_func'.


# single-parameterized function definition in Python.
def print_my_name(name):
    print(f"Hello {name}!")


print_my_name("Baris")


# multiple-parameterized function defintion in Python.
def print_my_name_and_surname(first_name, last_name):
    print(f"Hello {first_name} {last_name}!")


print_my_name_and_surname("Jeff", "Bezos")


def print_color_red():
    color = "Red"
    print(color)


print_color_red()

color = "Blue"
print(color)
print_color_red()


def print_numbers(highest_number, lowest_number):
    print(highest_number)
    print(lowest_number)


print_numbers(10, 3)
print_numbers(lowest_number=3, highest_number=10)  # explicit mentioning of the parameter names and values.


def multiply_numbers(a, b):
    return a * b


mult_solution = multiply_numbers(11, 8)
print(mult_solution)


def print_list(list_of_numbers):
    for number in list_of_numbers:
        print(number)


number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print_list(number_list)


def buy_item(cost_of_item):
    return cost_of_item + add_tax_to_item(cost_of_item)


def add_tax_to_item(cost_of_item):
    current_tax_rate = 0.03
    return cost_of_item * current_tax_rate


final_cost = buy_item(60)
print(final_cost)


def personal_info_dict(firstname, lastname, age):
    user_dict = {'firstname': firstname, 'lastname': lastname, 'age': age}
    return user_dict


print(personal_info_dict("Mike", "Teeve", 19))
