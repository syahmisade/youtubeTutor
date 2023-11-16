from datetime import timedelta
import numpy as np
from datetime import date, timedelta

# Arithmetic (paling penting) ----------------------

x = 5
y = 2

add = x+y
sub = x-y
multi = x*y
divi = x/y
floor_divi = x//y
mod = x % y
exp = x**y

# Ni kalau extra ---------------------------------------------------------------------

# ADD -------------------------------------------

contoh1 = "Salam"
contoh2 = " Malaysia!"
contoh3 = contoh1 + contoh2

# Set & Dictionary have the same method in MULTI


# SUB --------------------------------------------------------------------

# list
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4]
result_list = [item for item in list1 if item not in list2]

# Date
today = date(2023, 1, 1)
yesterday = today - timedelta(days=1)

# Dictionary
dict1 = {'a': 1, 'b': 2, 'c': 3}
keys_to_remove = {'b', 'c'}
result_dict = {key: value for key,
               value in dict1.items() if key not in keys_to_remove}

# String
original_string = "Python is great!"
substring_to_replace = "is"
replacement_string = "can be"
modified_string = original_string.replace(
    substring_to_replace, replacement_string)  # Using the replace method
# print("Original string:", original_string)
# print("Modified string:", modified_string)


# DIVI --------------------------------------------------------------------

# List slicing
original_list = [1, 2, 3, 4, 5, 6, 7, 8]
partitioned_lists = [original_list[i:i+3]
                     for i in range(0, len(original_list), 3)]

# String Splitting
sentence = "This is a sample sentence."
words = sentence.split()

# Date difference
start_date = date(2023, 1, 1)
end_date = date(2023, 1, 10)
duration = end_date - start_date

# List Chunking
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chunk_size = 3
chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

# Dictionary Partitioning
original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
keys_to_keep = {'a', 'c'}
partitioned_dict = {key: original_dict[key] for key in keys_to_keep}


# MULTI -----------------------------------------------------------------------------

# String
text = "Python"
repeated_text = text * 3  # Repeats the string three times

# List
elements = [1, 2, 3]
repeated_elements = elements * 2  # Repeats the list twice

# Tuples
tuple_elements = ('a', 'b')
repeated_tuple = tuple_elements * 4  # Repeats the tuple four times

# Set Union
set1 = {1, 2}
set2 = {2, 3}
union_set = set1 | set2  # Combines elements from both sets

# Dictionary Merging
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
# Merges the dictionaries, values from dict2 overwrite those in dict1 for common keys
dict1.update(dict2)


# MOD -------------------------------------------------------

# String length modulus
word = "example"
length_modulus = len(word) % 3

# List length modulus
my_list = [1, 2, 3, 4, 5]
length_modulus = len(my_list) % 2

# Date modulus
today = date.today()
days_since_monday = (today.weekday() - 0) % 7

# List index modulus
my_list = [10, 20, 30, 40, 50]
index = 8
value = my_list[index % len(my_list)]

# Enumeration with modulus
words = ["apple", "banana", "cherry", "date"]
for i, word in enumerate(words):
    if i % 2 == 0:
        # print(word) # Uncomment this and comment None
        None


# EXP -----------------------------------------------

# List Comprehension
base_list = [2] * 4
squared_list = [x**2 for x in base_list]

# Matrix Power with NumPy
matrix = np.array([[1, 2], [3, 4]])
result_matrix = np.linalg.matrix_power(matrix, 2)

# Datetime Duration Multiplication
duration = timedelta(days=1)
multiplied_duration = duration * 3
