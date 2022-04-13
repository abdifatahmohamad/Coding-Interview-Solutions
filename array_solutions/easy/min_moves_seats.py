def minMovesToSeat(seats, students):
    seats.sort()
    students.sort()
    # res = 0
    # for i in range(len(seats)):
    #     # seats = [1, 4, 5, 9]
    #     # students = [1, 2, 3, 6]
    #     # res = 7
    #     res += abs(seats[i] - students[i])
    # return res

    # fewer line of code
    seats.sort()
    students.sort()
    res = sum(abs(seat - student) for seat, student in zip(seats, students))
    return res


# print(minMovesToSeat([3,1,5], [2,7,4])) # 4
print(minMovesToSeat([4, 1, 5, 9], [1, 3, 2, 6]))  # 7
# print(minMovesToSeat([2,2,6,6], [1,3,2,6])) # 4
