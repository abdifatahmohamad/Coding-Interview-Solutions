def get_heaviest_package(w0, w1, w2):
    hash_map = {}
    hash_map[w0] = 0
    hash_map[w1] = 1
    hash_map[w2] = 2
    largest = hash_map[w0]
    for key in hash_map:
        if key > largest:
            largest = key
    return hash_map[largest]


w0 = 85
w1 = 100
w2 = 90
print(get_heaviest_package(w0, w1, w2))
