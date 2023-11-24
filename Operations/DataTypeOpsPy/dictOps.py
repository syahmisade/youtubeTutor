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
key_exists = 'age' in bio_aku  # *Result: True

# --- Creating dictionaries dynamically ---
nombor = {x: x**2 for x in range(5)}

# --- Handling missing key ---
umur = bio_aku.get('umur', 'N/A')
# Returns 'N/A' kalau 'umur' key is not present
