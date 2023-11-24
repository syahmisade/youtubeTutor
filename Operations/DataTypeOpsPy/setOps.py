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
