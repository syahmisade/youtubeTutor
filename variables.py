# Variables

num_int = 22  # integer
num_float = 23.58  # float number
sonfruit = "Adam Nayel"  # string

# booleans --------------------------------------------------------------------------------------------------
viewers_tambah = True
subscribe_tambah = True

if viewers_tambah and subscribe_tambah:
    print("Yeayy subs dgn view naik!")
else:
    print("Lain hari ada rezeki!")

# list ------------------------------------------------------------------------------------------------------
siblings = ["Munirah", "Syahmi", "Najmi"]

anak_pertama = siblings[0]
anak_kedua = siblings[1]

# Modifying elements
# siblings[0] = "Munirah Naja"

# Adding elements to the end of the list
siblings.append("Hadi")
siblings.insert(3, "Hadi")

# Removing elements by value
# siblings.remove("Munirah")

# Finding the length of the list
siblings_length = len(siblings)

print(siblings)
print(siblings_length)

# Iterating through the list
for name in siblings:
    print(name)

# Sets ------------------------------------------------------------------------------------------------------
# Creating a set of buah
buah = {"epal", "pisang", "jambu"}

# Adding an element to the set
# buah.add("oren")

# Attempting to add a duplicate element (no change)
# buah.add("epal")

# Removing an element from the set
# buah.remove("pisang")

# Checking for the existence of an element
manggis_ada_tak = "manggis" in buah  # True
# print(manggis_ada_tak)

# Finding the number of unique elements in the set
set_buah = len(buah)
# print(set_buah)

# Iterating through the set
for fruit in buah:
    print(fruit)

# tuples ------------------------------------------------------------------------------------------------------
# coordinates
point1 = (2, 3)
point2 = (-1, 5)

# multiple values
info_individu = ("Syahmi", 22, "Bangi")
tarikh = (17, 8, 2001)

# dictionary ------------------------------------------------------------------------------------------------------
person_info = {
    "name": "Syahmi",
    "age": 20,
    "is_student": False,
    "is_searching_for_job": True
}

# Access and print individual values
print(person_info["name"])
print(person_info["age"])
print(person_info["is_student"])
print(person_info["is_searching_for_job"])

# NoneType --------------------------------------------------------------------------------------------------------
jejaka_tak_tampan = "Waldan"
if jejaka_tak_tampan == "Remy":
    print("Eii kau tak hensem laa Remy!")
else:
    None

# complex number ---------------------------------------------------------------------------------------------------------
# Creating complex numbers
z1 = 3 + 4j
z2 = 1 - 2j

# Basic arithmetic with complex numbers
sum_result = z1 + z2
product_result = z1 * z2

# Displaying the results
print("z1:", z1)
print("z2:", z2)
print("Sum:", sum_result)
print("Product:", product_result)
