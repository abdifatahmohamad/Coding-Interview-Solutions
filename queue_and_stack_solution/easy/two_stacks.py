from typing import List


def two_stacks(max_sum: int, st1: List, st2: List) -> int:
    res, st1_count, st2_count, total_sum = 0, 0, 0, 0

    for st1_element in st1:
        if total_sum + st1_element > max_sum:
            break
        total_sum += st1_element
        st1_count += 1
    print(total_sum)
    return st1_count

st1 = [4, 2, 4, 6, 1]
st2 = [2, 1, 8, 5]
max_sum = 11
print(two_stacks(max_sum, st1, st2))
