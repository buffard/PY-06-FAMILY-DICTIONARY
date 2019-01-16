# 1. Define a dictionary that contains information about several members of your family. Use the following example as a template.

my_family = {
  'wife': {
    'name': 'Hanalyn',
    'age': 30
  },
  'mother': {
    'name': 'Andrea',
    'age':50
  },
  'father': {
    'name': 'Linden',
    'age':56
  }
}

# 2. Using a dictionary comprehension, produce output that looks like the following example.
# ie Krista is my sister and is 42 years old
# Helpful hint: To convert an integer into a string in Python, it's str(integer_value)

family_tree = {f"{member_values['name']} is my {family_member} and is {str(member_values['age'])} years old" for (family_member, member_values) in my_family.items()}

# print(my_family.items())
print(family_tree)