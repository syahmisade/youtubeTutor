# ---------- Arithmetic Operations ----------
x = 5
y = 2

add = x+y  # *Result: 7
sub = x-y  # *Result: 3
multi = x*y  # *Result: 10
exp = x**y  # *Result: 25
divi = x/y  # *Result: 2.5
floor_divi = x//y  # *Result: 2
mod = x % y  # *Result: 1

# print(add, sub, multi, exp, divi, floor_divi, mod)

# ---------- Comparison Operations ----------
num1 = 5
num2 = 7
a = "Apa khabar"
b = "Malaysia"

equality = num1 == num2  # *Result: False
inequality = a != b  # *Result: True
g_than = num1 > num2  # *Result: False
g_than_equal = num1 >= num2  # *Result: False
l_than = num1 < num2  # *Result: True
l_than_equal = num1 <= num2  # *Result: True

# print(equality, inequality, g_than, g_than_equal, l_than, l_than_equal)


# ---------- Logical Operations ----------
logic_t = True
logic_f = False
example_logic = True

for_and = logic_t and logic_f  # *Result: False
for_or = logic_t or logic_f  # *Result: True
for_not = not example_logic  # *Result: False

# print(for_and, for_or, for_not)


# ---------- Bitwise operations ----------
cth1 = 5  # Binary: 0101
cth2 = 3  # Binary: 0011

cth_and = cth1 & cth2  # Binary result: 0001 (Decimal: 1)
cth_or = cth1 | cth2  # Binary result: 0111 (Decimal: 7)
cth_xor = cth1 ^ cth2  # Binary result: 0110 (Decimal: 6)
cth_not = ~cth1  # Binary result: 1010 (Decimal: -6)
cth_ls = cth1 << 1  # Binary result: 1010 (Decimal: 10)
cth_rs = cth1 >> 1  # Binary result: 0010 (Decimal: 2)

# print(cth_and, cth_or, cth_xor, cth_not, cth_ls, cth_rs)


# ---------- Membership Test ----------
my_list = [1, 2, 3, 4, 5]
my_tuple = ('epal', 'durian', 'pisang')
my_string = "Python"

membership_in = 3 in my_list  # *Result: True
membership_notin = 'anggur' not in my_tuple  # *Result: True
membership_in_string = 'P' in my_string  # *Result: True
membership_notin_string = 'z' not in my_string  # *Result: True

# print(membership_in, membership_notin,
#       membership_in_string, membership_notin_string)


# ---------- Identity Test ----------
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]
string1 = "gwencana"
string2 = "pugoshippo"

identity_is = list1 is list2  # *Result: True
identity_isnot = string1 is not string2  # *Result: True
equality_result = list1 == list2  # *Result: True (values are equal)
identity_result = list1 is list3  # *Result: False (different objects)

# print(identity_is, identity_isnot, equality_result, identity_result)


# ---------- Data Type Operations ----------
# ----- String -----
str1 = "Salam"
str2 = "Sejahtera"
str3 = "Selamat Hari Raya!"
str4 = "Pantang mundur kecuali operasi"
str5 = "Aku dulu sekolah dekat SBPI Rawang"
str6 = "Fazz Ahmad Young Rapper kiyek"

concatenation = str1 + " " + str2  # *Result: "Salam Sejahtera"
repetition = str1 * 3  # *Result: "SalamSalamSalam"
indexing = str2[0]  # *Result: "S"
slicing = str2[2:8]  # *Result: "jahtera"
length = len(str3)  # *Result: 18

# --- String method ---
upper_case = str4.upper()  # *Result: "PANTANG MUNDUR KECUALI OPERASI"
lower_case = str4.lower()  # *Result: "pantang mundur kecuali operasi"
# *Result: "Aku dulu sekolah dekat SEPINTAR"
replace = str5.replace("SBPI Rawang", "SEPINTAR")
position = str6.find("kiyek")  # *Result: 24
count = str6.count("a")  # *Result: 3
split = str6.split()  # *Result: ['Fazz', 'Ahmad', 'Young', 'Rapper', 'kiyek']
join = " ".join(split)  # *Result: "Fazz Ahmad Young Rapper kiyek"

# print(concatenation, repetition, indexing, slicing, length)
# print(upper_case, lower_case, replace, position, count, split, join)
# print(split)


# ----- List -----
example1 = [1, 2, 3]
example2 = [4, 5, 6]
example3 = [10, 20, 30, 40, 50]
example4 = [5, 10, 15]
example5 = [20, 25, 30]
haiwan = ["Panda", "Garuda", "Singa"]
warna = ["Merah", "Biru", "Kuning"]
negeri_borneo = ['Sabah', 'Sarawak', 'KL']
kenderaan = ["Kereta", "Kaki", "Motorsikal", "MRT"]
nombor_berterabur = [4, 7, 1, 3, 5, 2, 9, 6, 8]
anime = ["One Punch Man", "Dragon ball", "Naruto", "One Piece"]

concatenation_list = example1 + example2  # *Result: [1, 2, 3, 4, 5, 6]
repetition_list = example1 * 3   # *Result: [1, 2, 3, 1, 2, 3, 1, 2, 3]
indexing_list = example3[3]  # *Result: 40
slicing_list = example3[1:3]  # *Result: [20, 30, 40]

# --- List Method ---
haiwan.append("Penguin")  # *Result: ["Panda", "Garuda", "Singa", "Penguin"]
example4.extend(example5)  # *Result: [5, 10, 15, 20, 25, 30]
warna.insert(2, "Putih")  # *Result: ['Merah', 'Biru', 'Putih', 'Kuning']
negeri_borneo.remove('KL')  # *Result: ['Sabah', 'Sarawak']
non_kenderaan = kenderaan.pop(1)  # *Result: ['Kereta', 'Motorsikal', 'MRT']
nombor_berterabur.sort()  # *Result: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# *Result: ['One Piece', 'Naruto', 'Dragon ball', 'One Punch Man']
anime.reverse()


# ----- Sets ----- (INGAT! nilai sentiasa tak ikut tururan)
add_cth = {1, 2, 3, 4, 5}
rmv_cth = {2, 4, 6, 8, 10}
dscd_cth = set([6, 7, 8, 9, 10])
clear_cth = {11, 12, 13, 14, 15}
set_a = {1, 2}
set_b = {1, 2, 3, 4}

add_cth.add(6)  # *Result: {1, 2, 3, 4, 5, 6}
rmv_cth.remove(6)  # *Result: {2, 4, 8, 10}
dscd_cth.discard(10)  # *Result: {6, 7, 8, 9}
# .discard() takkan bagi error kalau nombor yang kita pilih tak ada dalam set
# tapi still, functionality dia still sama mcm .remove()

# --- Set Method ---
union_set = add_cth | dscd_cth  # *Result: {1, 2, 3, 4, 5, 6, 7, 8, 9}
intersection_set = add_cth & rmv_cth  # *Result: {2, 4}
difference_set = add_cth - rmv_cth  # *Result: {1, 3, 5, 6}
symmetric_difference_set = add_cth ^ rmv_cth  # *Result: {1, 3, 5, 6, 8, 10}
clear_cth.clear()  # *Result: set()
set_copy = add_cth.copy()  # *Result: {1, 2, 3, 4, 5, 6}
squared_set = {x**2 for x in range(1, 6)}  # *Result: {1, 4, 9, 16, 25}
is_subset = set_a.issubset(set_b)  # *Result: True (boleh jugak guna <=)
is_superset = set_b.issuperset(set_a)  # *Result: True (boleh jugak guna >=)


# ----- Dictionary -----
bio_aku = {'nama': 'Syahmi', 'umur': 22, 'bandar': 'Bangi'}

access_data = bio_aku['nama']  # *Result: 'Syahmi'

# --- Modify data: Adding and Deleting Data ---
# bio_aku['umur'] = 22.3
# bio_aku['pekerjaan'] = 'Software Engineer'
# del bio_aku['bandar']
# popped_value = bio_aku.pop('umur')

# --- Retrieving keys, values, key-value pairs (item), copying and clear data ---
keys = bio_aku.keys()  # *Result: dict_keys(['nama', 'umur', 'bandar'])
values = bio_aku.values()  # *Result: dict_values(['Syahmi', 22, 'Bangi'])
items = bio_aku.items()
# *Result: dict_items([('nama', 'Syahmi'), ('umur', 22), ('bandar', 'Bangi')])
copy_dict = bio_aku.copy()
# bio_aku.clear()
key_exists = 'age' in bio_aku  # *Result: False

# --- Creating dictionaries dynamically ---
nombor = {x: x**2 for x in range(5)}
# *Result: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# --- Handling missing key ---
umur = bio_aku.get('umur', 'N/A')
# Returns 'N/A' kalau 'umur' key is not present


# ----- Tuple -----
cth_tuple = (2, 3, 'kucing', 'berlari', 'kucing')
tuple1 = (1, 2, 3)
tuple2 = ('kiri', 'kanan')

indexing = cth_tuple[0]  # *Result: 2
slicing = cth_tuple[1:4]  # *Result: (3, 'kucing', 'berlari')
concatenated_tuples = tuple1 + tuple2  # *Result: (1, 2, 3, 'kiri', 'kanan')
repeated_tuple = cth_tuple * 2
# *Result: (2, 3, 'kucing', 'berlari', 'kucing', 2, 3, 'kucing', 'berlari', 'kucing')
count_tuple = cth_tuple.count('kucing')  # *Result: 2
index_tuple = cth_tuple.index('berlari')  # *Result: 3
tuple_length = len(cth_tuple)  # *Result: 5
element_present = 'kucing' in cth_tuple  # *Result: True

# cth_tuple[0] = 10  # return error sbb tuple immutable

# --- Packing and Unpacking ---
packed_tuple = 'Saya', 'Suka', 'Nasi Ayam'  # *Result: (1, 'apple', 3.14)
x, y, z = packed_tuple  # *Result: x = 1, y = 'apple', z = 3.14
