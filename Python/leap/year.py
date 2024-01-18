"""
A year divisible by 4 is a leap year.
If the year is a new century(ends with 0 eg.1900),
It has to be completely divisible by 100 and 400,
Or it is not a leap year.
"""


def is_leap_year(year):
    # A new leap century
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    # A new non_leap century
    elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
        return False
    # A leap year
    elif year % 4 == 0:
        return True
    # A non_leap year
    else:
        return False

# 1997 is not a leap year, but 1996 is. 1900 is not a leap year, but 2000 is.