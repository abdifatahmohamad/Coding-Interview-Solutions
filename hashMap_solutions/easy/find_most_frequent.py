# Find the most frequent from the nums.
# If there is a tie, return all the values with the highest frequency in any order.
nums = [2, 9, 1, 8, 4, 1, 9, 1, 4, 6, 2, 9, 2]
mapping = {}
for n in nums:
    mapping[n] = mapping.get(n, 0) + 1


max_freq = 0
for n in mapping:
    if mapping.get(n) > max_freq:
        max_freq = mapping.get(n)
res = []
for n in mapping:
    if mapping.get(n) == max_freq:
        res.append(n)
        
print(res) # [2, 9, 1]
