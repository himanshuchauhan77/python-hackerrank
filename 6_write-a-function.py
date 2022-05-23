def is_leap(year):
    leap = False
    
    # Write your logic here
    # if a year is divided by 4 it will be leap year
    if year%4==0:
        leap=True
        # further if it will be divided by 100, it will not be leap year
        if year%100==0:
            leap=False
            # even if it is divided by 4 and 100, a year can be leap year if it is divided by 400
            if year%400==0:
                leap = True
    return leap

year = int(input())
print(is_leap(year))