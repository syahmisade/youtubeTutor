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
slicing = str2[2:8]  # *Result: "jahter"
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
