# Arithmetic Operations
x = 5
y = 2

add = x+y  # Result: 7
sub = x-y  # Result: 3
multi = x*y  # Result: 10
exp = x**y  # Result: 25
divi = x/y  # Result: 2.5
floor_divi = x//y  # Result: 2
mod = x % y  # Result: 1

# print(add, sub, multi, exp, divi, floor_divi, mod)

# Comparison Operations
num1 = 5
num2 = 7
a = "hello"
b = "world"

equality = x == y  # Result: False
inequality = a != b  # Result: True
g_than = num1 > num2  # Result: False
g_than_equal = num1 >= num2  # Result: False
l_than = num1 < num2  # Result: True
l_than_equal = num1 <= num2  # Result: True

# print(equality, inequality, g_than, g_than_equal, l_than, l_than_equal)


# Logical Operations
logic_t = True
logic_f = False
example_logic = True

for_and = logic_t and logic_f  # Result: False
for_or = logic_t or logic_f  # Result: True
for_not = not example_logic  # Result: False

# print(for_and, for_or, for_not)

# Bitwise operations
cth1 = 5  # Binary: 0101
cth2 = 3  # Binary: 0011

cth_and = cth1 & cth2  # Binary result: 0001 (Decimal: 1)
cth_or = cth1 | cth2  # Binary result: 0111 (Decimal: 7)
cth_xor = cth1 ^ cth2  # Binary result: 0110 (Decimal: 6)
cth_not = ~cth1  # Binary result: 1010 (Decimal: -6)
cth_ls = cth1 << 1  # Binary result: 1010 (Decimal: 10)
cth_rs = cth1 >> 1  # Binary result: 0010 (Decimal: 2)

# print(cth_and, cth_or, cth_xor, cth_not, cth_ls, cth_rs)


# Membership Test
my_list = [1, 2, 3, 4, 5]
my_tuple = ('apple', 'orange', 'banana')
my_string = "Python"

membership_in = 3 in my_list  # Result: True
membership_notin = 'grape' not in my_tuple  # Result: True
membership_in_string = 'P' in my_string  # Result: True
membership_notin_string = 'z' not in my_string  # Result: True

# print(membership_in, membership_notin,
#       membership_in_string, membership_notin_string)


# Identity Test
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]
string1 = "hello"
string2 = "world"

identity_is = list1 is list2  # Result: True
identity_isnot = string1 is not string2  # Result: True
equality_result = list1 == list2  # Result: True (values are equal)
identity_result = list1 is list3  # Result: False (different objects)

# print(identity_is, identity_isnot, equality_result, identity_result)


# Data Type Operations
