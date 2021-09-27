# Insert 2D array into a hashmap
students = [['Hassan', 92], ['Abdifatah', 95],
            ['Hassan', 88], ['Abdifatah', 76],
            ['Abdifatah', 81], ['Hassan', 73]]

# Output: {'Hassan':[92], 'Abdifatah':[95]}

mapping = {}

for name, grade in students:
    if name not in mapping:
        mapping[name] = []
    mapping[name].append(grade)

print(mapping)
# Output:

# {
# 'Hassan': [92, 88, 73],
# 'Abdifatah': [95, 76, 81]
# }
