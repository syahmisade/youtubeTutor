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
