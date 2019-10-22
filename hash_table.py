# Hash Tables:
# Key-to-value mappings are unique
# Hash tables are typically fast
# For small datasets, arrays/lists are usually more efficient
# Hash tables don't order entries in a predictable way

# Create new hash table
items1 = dict({"key1" : 1, "key2": 2, "key3": 3})

# Create a hash table progressively
items2 = {}
items2["key1"] = 1
items2["key2"] = 2
items2["key3"] = 3

# Replace an item
items2["key2"] = 5

# Iterate the keys and values in the hash table
for key, value in items2.items():
    print("Key: ", key, " value: ", value)
