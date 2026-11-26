# Lab 01 Exercise 6: Leap Year Detector
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
leap_year1 = is_leap_year(2024)
print(leap_year1)

leap_year2 = is_leap_year(1900)
print(leap_year2)