# Convert string words into a list without using built-in fucntion split()
words = "dog cat cat fish"
res = []
curr = ""
for ch in words:
    if ch == " ":
        res.append(curr)
        curr = ""
    else:
        curr += ch
res.append(curr)
print(res)
