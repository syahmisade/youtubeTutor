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
