##30/9/2020
import datetime

bigMonth = [1, 3, 5, 7, 8, 10, 12]
smallMonth = [4, 6, 9, 11]

year1 = int(input("Enter year 1 "))
month1 = int(input("Enter month 1 "))
day1 = int(input("Enter day 1 "))

year2 = int(input("Enter year 2 "))
month2 = int(input("Enter month 2 "))
day2 = int(input("Enter day 2 "))


year = year2 - year1
month = month2 - month1
day = day2 - day1

if day < 0:
    month -= 1
    if month in bigMonth:
        day += 31
    elif month in smallMonth:
        day += 30
    else:
        day += 29

print(year, "years, ", month, "months, ", day, "days, ")
        


