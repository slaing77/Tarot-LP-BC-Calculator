#!/usr/bin/python
def sum_digits(number):
    "iterate through each digit and sum the result"
    return sum([int(digit) for digit in str(number)])


def sum_until_len(number, length=1):
    "keep summing until the result is same as length"
    while len(str(number)) != length:
        number = sum_digits(number)
    return int(number)


def life_path_number(day, month, year):
    """Life Path number from birth day
    sum_digits to get single number from d,m,y
    sum of those single numbers is the LPN"""
    day_sum = sum_until_len(day)
    month_sum = sum_until_len(month)
    year_sum = sum_until_len(year)
    lpn = day_sum + month_sum + year_sum
    # check for master number
    if master_number_check(lpn):
        return sum_until_len(lpn), lpn
    else:
        return sum_until_len(lpn), None


def master_number_check(number):
    """lets consider master numbers are just 11, 22, 33"""
    master_numbers = [11, 22, 33]
    if number in master_numbers:
        return True
    else:
        return None


if __name__ == '__main__':
    month, day, year = input('Please use mm/dd/yyyy Your Birthdate: ').split('/')

    lpn, mn = life_path_number(day, month, year)
    if mn:
        print(f"Your Life Path Number/Master Number: {lpn}/{mn}")
    else:
        print(f"Life Path Number: {lpn}")
        print('Your Birth Card Number: ',(lpn-1 + 10))
