def is_leap(year):
    leap = False
    if year >= 1 and year <= 9999 and year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    return leap


print(is_leap(1986))
