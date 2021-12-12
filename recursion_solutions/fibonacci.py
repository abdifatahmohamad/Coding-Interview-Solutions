import time


# Iteratively
def fib_iteratively(idx):
    seq = [0, 1]
    for i in range(idx):
        seq.append(seq[-1] + seq[-2])
    return seq[-2]


# Recursively
def fib_recursively(idx):
    # Base case
    if idx <= 1:
        return idx
    else:
        return fib_recursively(idx - 1) + fib_recursively(idx - 2)


# Knowing which one is more efficient
print("******** Recursion ********")
rec = time.time()
fib_recursively(8)
print("Speed: " + str(time.time() - rec))

print()

print("******** Iteratively ********")
it = time.time()
fib_iteratively(8)
print("Speed: " + str(time.time() - it))
