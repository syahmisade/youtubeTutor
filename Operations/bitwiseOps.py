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
