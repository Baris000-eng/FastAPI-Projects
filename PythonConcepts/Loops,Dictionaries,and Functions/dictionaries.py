"""
Dictionaries in Python
"""

user_dictionary = {
    'username': 'CodingWithBaris',
    'name': 'Baris',
    'age': 25
}

print(user_dictionary)

print(user_dictionary.get('username'))  # It gets the value that corresponds to the key named 'username'.
print(user_dictionary.get('name'))  # It gets the value that corresponds to the key named 'name'.
print(user_dictionary.get('age'))  # It gets the value in the dictionary that corresponds to the key named 'age':

print(len(user_dictionary))  # It will return the length of the user_dictionary dictionary.
user_dictionary.pop('name')  # It will delete the key being 'name' and value that corresponds to this key.
print(user_dictionary)




user_dictionary.clear()  # It will clear all the content of the dictionary.
print(user_dictionary)

# del user_dictionary : It will delete the user dictionary.

second_user_dict = {
    'username': 'CodingWithMike',
    'name': 'Mike',
    'age': 20
}

# Obtaining keys of the dictionary named 'second_user_dict' and printing them.
for k in second_user_dict.keys():
    print(k)

# Obtaining values of the dictionary named 'second_user_dict' and printing them.
for v in second_user_dict.values():
    print(v)

# Obtaining keys and values of the dictionary named 'second_user_dict' and printing them.
for k, v in second_user_dict.items():
    print(k, v)

second_user_dict.pop("age")  # this will remove both the key being 'age' and the value corresponding to this key.
print(second_user_dict)


# The third_user_dict.pop("name") statement will only affect the dictionary named 'third_user_dict'. It will not affect
# the dictionary named 'second_user_dict'.
third_user_dict = second_user_dict.copy()
third_user_dict.pop("name")  # this will remove both the key being 'name' and the value corresponding to this key.
print(third_user_dict)
print(second_user_dict)
