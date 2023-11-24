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
