from collections import defaultdict
import heapq


def top_five_average(students):
    mapping = {}

    for student, score in students:
        if student not in mapping:
            mapping[student] = []
        mapping[student].append(score)

    res = []
    for k in mapping:
        avg = getAverage(mapping[k])
        res.append(list((k, avg)))
    return res


def getAverage(nums):
    nums.sort(reverse=True)
    total_grades = 0
    for i in range(5):
        total_grades += nums[i]
    return total_grades // 5

# Solution using priority queue (heap)


def highFive(grades):
    student_grades = defaultdict(list)
    for id, grade in grades:
        heapq.heappush(student_grades[id], grade)
        if len(student_grades.get(id)) > 5:
            heapq.heappop(student_grades.get(id))
    res = []
    for id in student_grades:
        total = sum(student_grades.get(id))
        res.append((id, total // 5))

    return res


print(top_five_average([[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [
      2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]))
# print(top_five_average( [[1,100], [7,100], [1,100], [7,100], [1,100], [7,100], [1,100], [7,100], [1,100], [7,100]]))


# Example 1:
#items = [[1,91], [1,92], [2,93], [2,97], [1,60], [2,77], [1,65], [1,87], [1,100], [2,100], [2,76]]
# Output: [[1,87], [2,88]]


# Example 2:
#items = [[1,100], [7,100], [1,100], [7,100], [1,100], [7,100], [1,100], [7,100], [1,100], [7,100]]

# Output: [[1,100], [7,100]]
