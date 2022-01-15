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
    sum of those single numbers is the lpn"""
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
    month, day, year = input('Please use mm/dd/yyyy Your Birthdate: ').split(
        '/')

    lpn, mn = life_path_number(month, day, year)
    if mn:
        print(f"Your Life Path Number/Master Number: {lpn}/{mn}")
    else:
        print(f"Your Life Path Number: {lpn}")

    birth_card_number = (lpn - 1 + 10)

    print(f'Your Birth Card Number: ', birth_card_number)

    bc_dict = {
        '1': 'The Magician',
        '2': 'The High Priestess',
        '3': 'The Empress',
        '4': 'The Emperor',
        '5': 'The Hierophant',
        '6': 'The Lovers',
        '7': 'The Chariot',
        '8': 'Strength',
        '9': 'The hermit',
        '10': 'Wheel of Fortune',
        '11': 'Justice',
        '12': 'The Hanged Man',
        '13': 'Death',
        '14': 'Temperance',
        '15': 'The Devil',
        '16': 'The Tower',
        '17': 'The Star',
        '18': 'The Moon',
        '19': 'The Sun',
        '20': 'Judgement',
        '21': 'The World'
    }
life_card = input('Please enter your Life Path Number: ')
birth_card = input('Please enter your Birth Card number: ')
print(f'Your Life Path Card is: ', bc_dict[life_card],
      f' & Your Birth Card is: ', bc_dict[birth_card])