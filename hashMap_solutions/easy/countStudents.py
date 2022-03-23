from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while students:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            elif sandwiches[0] not in students:
                break
            else:
                students.append(students.pop(0))
        return len(students)

##########################################################
# The same above solution using dictionary


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        d = Counter(students)
        for sandwich in sandwiches:
            if d[sandwich] == 0:
                break
            d[sandwich] -= 1
        return sum(d.values())
##########################################################


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        d = Counter(students)
        for sandwich in sandwiches:
            if d[sandwich] == 0:
                break
            d[sandwich] -= 1

        total_student = 0
        for k in d:
            total_student += d[k]
        return total_student

##########################################################


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        d = defaultdict(int)
        for student in students:
            d[student] = d.get(student, 0) + 1

        for sandwich in sandwiches:
            if d[sandwich] == 0:
                break
            d[sandwich] -= 1

        total_student = 0
        for k in d:
            total_student += d[k]
        return total_student


##########################################################
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        d = {}
        for student in students:
            d[student] = d.get(student, 0) + 1

        for sandwich in sandwiches:
            if d.get(sandwich, 0) == 0:
                break
            d[sandwich] -= 1

        total_student = 0
        for k in d:
            total_student += d[k]
        return total_student


solution = Solution()
students = [1, 1, 1, 0, 0, 1]
sandwiches = [1, 0, 0, 0, 1, 1]

# students = [1, 1, 0, 0]
# sandwiches = [0, 1, 0, 1]
print(solution.countStudents(students, sandwiches))
