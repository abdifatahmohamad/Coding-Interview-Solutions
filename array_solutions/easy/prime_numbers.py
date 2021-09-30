num = int(input("Enter a number: "))

for n in range(2, num + 1):
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
    if prime:
        print(n, end=",")
