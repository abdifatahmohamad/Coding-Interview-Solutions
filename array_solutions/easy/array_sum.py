size = int(input("Enter size of array: "))
numbers = [0] * size
total = 0
count = 0
avg = 0
for i in range(len(numbers)):
    print("Enter No", (i + 1), ": ", end=" ")
    value = int(input())
    numbers[i] = value
    if numbers[i] > 0:
        total += numbers[i]
        count += 1

avg = total / count
print("The sum of numbers is: ", total)
print("The number of positive integers is: ", count)
print("The average of positive numbers is: ", avg)
