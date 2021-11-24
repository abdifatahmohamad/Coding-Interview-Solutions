def compute_closest_to_zero(ts):
    # Base case:
    if len(ts) == 0:
        return 0

    closest = 0
    for i in range(len(ts)):
        if closest == 0:
            closest = ts[i]
        elif ts[i] > 0 and ts[i] <= abs(closest):
            closest = ts[i]
        elif ts[i] < 0 and - ts[i] < abs(closest):
            closest = ts[i]
    return closest


arr1 = [-9, -5, 5, 4, -3]  # Output: -3
arr2 = [-5, 6, -4, -1, 1, 8]  # Output: 1
arr3 = [-5, 6, -4, 0, 8]  # Output: -4
arr4 = [-9, -5, 7, -4]  # Output: -4
print(compute_closest_to_zero(arr4))
